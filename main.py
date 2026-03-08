#!/usr/bin/env python3
"""
ERToS - EXE Runner Tool on System
Windows .exe dosyalarını Linux'ta çalıştırmak için GUI araç
"""

import sys
import os
import subprocess
import shutil
from pathlib import Path
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFileDialog, 
                             QTextEdit, QProgressBar, QMessageBox, QTabWidget,
                             QFrame, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPalette, QColor, QLinearGradient


class WineInstaller(QThread):
    progress = pyqtSignal(str)
    finished = pyqtSignal(bool)
    
    def run(self):
        try:
            self.progress.emit("Wine kontrol ediliyor...")
            
            # Wine kurulu mu kontrol et
            if shutil.which('wine'):
                self.progress.emit("Wine zaten kurulu!")
                self.finished.emit(True)
                return
            
            self.progress.emit("Wine kurulumu başlatılıyor...")
            self.progress.emit("pacman ile wine yükleniyor...")
            
            # Arch Linux için wine kurulumu
            result = subprocess.run(['pkexec', 'pacman', '-S', '--noconfirm', 'wine'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                self.progress.emit("Wine başarıyla kuruldu!")
                self.finished.emit(True)
            else:
                self.progress.emit(f"Hata: {result.stderr}")
                self.finished.emit(False)
                
        except Exception as e:
            self.progress.emit(f"Kurulum hatası: {str(e)}")
            self.finished.emit(False)


class ExeRunner(QThread):
    output = pyqtSignal(str)
    finished = pyqtSignal(int)
    
    def __init__(self, exe_path):
        super().__init__()
        self.exe_path = exe_path
    
    def run(self):
        try:
            self.output.emit(f"Çalıştırılıyor: {self.exe_path}\n")
            
            process = subprocess.Popen(['wine', self.exe_path],
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT,
                                     text=True)
            
            for line in process.stdout:
                self.output.emit(line)
            
            process.wait()
            self.finished.emit(process.returncode)
            
        except Exception as e:
            self.output.emit(f"Hata: {str(e)}\n")
            self.finished.emit(1)


class ERToSMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.exe_path = None
        self.init_ui()
        self.apply_styles()
        self.check_wine()
    
    def init_ui(self):
        self.setWindowTitle("ERToS - EXE Runner Tool on System")
        self.setGeometry(100, 100, 900, 650)
        
        # Ana widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        central_widget.setLayout(layout)
        
        # Header Frame
        header_frame = QFrame()
        header_frame.setObjectName("headerFrame")
        header_layout = QVBoxLayout()
        header_frame.setLayout(header_layout)
        
        # Başlık
        title = QLabel("ERToS")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("titleLabel")
        title_font = QFont()
        title_font.setPointSize(32)
        title_font.setBold(True)
        title.setFont(title_font)
        header_layout.addWidget(title)
        
        subtitle = QLabel("🚀 Windows .exe dosyalarını Linux'ta çalıştırın")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setObjectName("subtitleLabel")
        subtitle_font = QFont()
        subtitle_font.setPointSize(11)
        subtitle.setFont(subtitle_font)
        header_layout.addWidget(subtitle)
        
        layout.addWidget(header_frame)
        
        # Tab widget
        tabs = QTabWidget()
        tabs.setObjectName("mainTabs")
        layout.addWidget(tabs)
        
        # Ana tab
        main_tab = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_tab.setLayout(main_layout)
        
        # Dosya seçme frame
        file_frame = QFrame()
        file_frame.setObjectName("fileFrame")
        file_layout = QVBoxLayout()
        file_frame.setLayout(file_layout)
        
        file_label_title = QLabel("📁 Seçili Dosya")
        file_label_title.setObjectName("sectionLabel")
        file_layout.addWidget(file_label_title)
        
        self.file_label = QLabel("Henüz dosya seçilmedi...")
        self.file_label.setObjectName("filePathLabel")
        self.file_label.setWordWrap(True)
        file_layout.addWidget(self.file_label)
        
        select_btn = QPushButton("🔍 EXE Dosyası Seç")
        select_btn.setObjectName("selectButton")
        select_btn.setCursor(Qt.PointingHandCursor)
        select_btn.clicked.connect(self.select_exe)
        select_btn.setMinimumHeight(45)
        file_layout.addWidget(select_btn)
        
        main_layout.addWidget(file_frame)
        
        # Çalıştır butonu
        self.run_btn = QPushButton("▶️ Çalıştır")
        self.run_btn.setObjectName("runButton")
        self.run_btn.setCursor(Qt.PointingHandCursor)
        self.run_btn.setEnabled(False)
        self.run_btn.clicked.connect(self.run_exe)
        self.run_btn.setMinimumHeight(50)
        main_layout.addWidget(self.run_btn)
        
        # Çıktı alanı
        output_label = QLabel("📋 Program Çıktısı")
        output_label.setObjectName("sectionLabel")
        main_layout.addWidget(output_label)
        
        self.output_text = QTextEdit()
        self.output_text.setObjectName("outputText")
        self.output_text.setReadOnly(True)
        main_layout.addWidget(self.output_text)
        
        tabs.addTab(main_tab, "🏠 Ana")
        
        # Ayarlar tab
        settings_tab = QWidget()
        settings_layout = QVBoxLayout()
        settings_layout.setSpacing(15)
        settings_layout.setContentsMargins(20, 20, 20, 20)
        settings_tab.setLayout(settings_layout)
        
        settings_title = QLabel("⚙️ Wine Ayarları")
        settings_title.setObjectName("sectionLabel")
        settings_layout.addWidget(settings_title)
        
        wine_config_btn = QPushButton("🔧 Wine Yapılandırması")
        wine_config_btn.setObjectName("settingsButton")
        wine_config_btn.setCursor(Qt.PointingHandCursor)
        wine_config_btn.clicked.connect(self.open_wine_config)
        wine_config_btn.setMinimumHeight(45)
        settings_layout.addWidget(wine_config_btn)
        
        wine_tricks_btn = QPushButton("🎯 Winetricks")
        wine_tricks_btn.setObjectName("settingsButton")
        wine_tricks_btn.setCursor(Qt.PointingHandCursor)
        wine_tricks_btn.clicked.connect(self.open_winetricks)
        wine_tricks_btn.setMinimumHeight(45)
        settings_layout.addWidget(wine_tricks_btn)
        
        reinstall_wine_btn = QPushButton("🔄 Wine'ı Yeniden Kur")
        reinstall_wine_btn.setObjectName("dangerButton")
        reinstall_wine_btn.setCursor(Qt.PointingHandCursor)
        reinstall_wine_btn.clicked.connect(self.reinstall_wine)
        reinstall_wine_btn.setMinimumHeight(45)
        settings_layout.addWidget(reinstall_wine_btn)
        
        settings_layout.addStretch()
        
        tabs.addTab(settings_tab, "⚙️ Ayarlar")
        
        # Hakkında tab
        about_tab = QWidget()
        about_layout = QVBoxLayout()
        about_layout.setSpacing(15)
        about_layout.setContentsMargins(20, 20, 20, 20)
        about_tab.setLayout(about_layout)
        
        about_frame = QFrame()
        about_frame.setObjectName("aboutFrame")
        about_frame_layout = QVBoxLayout()
        about_frame.setLayout(about_frame_layout)
        
        about_text = QLabel(
            "<h2 style='color: #2196F3;'>ERToS v1.0</h2>"
            "<p style='font-size: 14px;'><b>EXE Runner Tool on System</b></p>"
            "<p style='font-size: 12px; color: #666;'>Windows .exe dosyalarını Linux'ta Wine kullanarak çalıştırmanızı sağlar.</p>"
            "<p style='font-size: 12px; color: #666;'>Arch Linux için optimize edilmiştir.</p>"
            "<br>"
            "<p style='font-size: 13px;'><b>✨ Özellikler:</b></p>"
            "<ul style='font-size: 12px;'>"
            "<li>🚀 Otomatik Wine kurulumu</li>"
            "<li>🎨 Modern ve kullanıcı dostu arayüz</li>"
            "<li>📦 AppImage formatı (portable)</li>"
            "<li>⚙️ Wine yapılandırma araçları</li>"
            "<li>🔧 Arch Linux için optimize edilmiş</li>"
            "</ul>"
        )
        about_text.setWordWrap(True)
        about_frame_layout.addWidget(about_text)
        
        about_layout.addWidget(about_frame)
        about_layout.addStretch()
        
        tabs.addTab(about_tab, "ℹ️ Hakkında")
    
    def apply_styles(self):
        """Modern ve renkli stil uygula"""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e, stop:1 #16213e);
            }
            
            QWidget {
                background-color: transparent;
                color: #ffffff;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            
            #headerFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 10px;
            }
            
            #titleLabel {
                color: #ffffff;
                font-weight: bold;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            #subtitleLabel {
                color: #f0f0f0;
                font-size: 11pt;
            }
            
            QTabWidget::pane {
                border: 2px solid #2196F3;
                border-radius: 10px;
                background-color: rgba(255, 255, 255, 0.05);
                padding: 5px;
            }
            
            QTabBar::tab {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2c3e50, stop:1 #34495e);
                color: #ecf0f1;
                padding: 12px 20px;
                margin-right: 5px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                font-weight: bold;
                font-size: 11pt;
            }
            
            QTabBar::tab:selected {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #3498db, stop:1 #2980b9);
                color: white;
            }
            
            QTabBar::tab:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #34495e, stop:1 #2c3e50);
            }
            
            #fileFrame, #aboutFrame {
                background-color: rgba(255, 255, 255, 0.08);
                border: 2px solid rgba(33, 150, 243, 0.3);
                border-radius: 12px;
                padding: 20px;
            }
            
            #sectionLabel {
                color: #64B5F6;
                font-size: 14pt;
                font-weight: bold;
                margin-bottom: 5px;
            }
            
            #filePathLabel {
                color: #B0BEC5;
                font-size: 11pt;
                padding: 10px;
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 8px;
                border-left: 4px solid #2196F3;
            }
            
            #selectButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 13pt;
                font-weight: bold;
            }
            
            #selectButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #764ba2, stop:1 #667eea);
            }
            
            #selectButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #5a3d7f, stop:1 #4e5fb8);
            }
            
            #runButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #11998e, stop:1 #38ef7d);
                color: white;
                border: none;
                border-radius: 12px;
                padding: 15px;
                font-size: 15pt;
                font-weight: bold;
            }
            
            #runButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #38ef7d, stop:1 #11998e);
            }
            
            #runButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #0e7a6f, stop:1 #2bc765);
            }
            
            #runButton:disabled {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #555555, stop:1 #666666);
                color: #999999;
            }
            
            #settingsButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #4facfe, stop:1 #00f2fe);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 12pt;
                font-weight: bold;
                text-align: left;
            }
            
            #settingsButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #00f2fe, stop:1 #4facfe);
            }
            
            #settingsButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3a8acc, stop:1 #00c0cc);
            }
            
            #dangerButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #f857a6, stop:1 #ff5858);
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 12pt;
                font-weight: bold;
                text-align: left;
            }
            
            #dangerButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff5858, stop:1 #f857a6);
            }
            
            #dangerButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #c64585, stop:1 #cc4646);
            }
            
            #outputText {
                background-color: rgba(0, 0, 0, 0.4);
                color: #00ff00;
                border: 2px solid rgba(33, 150, 243, 0.3);
                border-radius: 10px;
                padding: 10px;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 10pt;
            }
            
            QMessageBox {
                background-color: #2c3e50;
            }
            
            QMessageBox QLabel {
                color: #ecf0f1;
            }
            
            QMessageBox QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                min-width: 80px;
            }
            
            QMessageBox QPushButton:hover {
                background-color: #2980b9;
            }
        """)
    
    def check_wine(self):
        if not shutil.which('wine'):
            reply = QMessageBox.question(self, 'Wine Bulunamadı',
                                        'Wine kurulu değil. Şimdi kurmak ister misiniz?',
                                        QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.install_wine()
        else:
            self.output_text.append("Wine kurulu ve hazır!\n")
    
    def install_wine(self):
        self.output_text.append("Wine kurulumu başlatılıyor...\n")
        self.installer = WineInstaller()
        self.installer.progress.connect(self.on_install_progress)
        self.installer.finished.connect(self.on_install_finished)
        self.installer.start()
    
    def on_install_progress(self, message):
        self.output_text.append(message + "\n")
    
    def on_install_finished(self, success):
        if success:
            QMessageBox.information(self, "Başarılı", "Wine başarıyla kuruldu!")
        else:
            QMessageBox.warning(self, "Hata", "Wine kurulumu başarısız oldu.")
    
    def select_exe(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "EXE Dosyası Seç", "", "EXE Files (*.exe);;All Files (*)"
        )
        if file_path:
            self.exe_path = file_path
            self.file_label.setText(f"✅ {os.path.basename(file_path)}\n📂 {os.path.dirname(file_path)}")
            self.run_btn.setEnabled(True)
            self.output_text.append(f"✅ Dosya seçildi: {file_path}\n")
    
    def run_exe(self):
        if not self.exe_path:
            return
        
        self.output_text.clear()
        self.run_btn.setEnabled(False)
        
        self.runner = ExeRunner(self.exe_path)
        self.runner.output.connect(self.on_runner_output)
        self.runner.finished.connect(self.on_runner_finished)
        self.runner.start()
    
    def on_runner_output(self, text):
        self.output_text.append(text)
    
    def on_runner_finished(self, code):
        if code == 0:
            self.output_text.append(f"\n✅ Program başarıyla sonlandı (kod: {code})\n")
        else:
            self.output_text.append(f"\n⚠️ Program hata ile sonlandı (kod: {code})\n")
        self.run_btn.setEnabled(True)
    
    def open_wine_config(self):
        subprocess.Popen(['winecfg'])
    
    def open_winetricks(self):
        if shutil.which('winetricks'):
            subprocess.Popen(['winetricks'])
        else:
            QMessageBox.information(self, "Bilgi", 
                                   "Winetricks kurulu değil. 'sudo pacman -S winetricks' ile kurabilirsiniz.")
    
    def reinstall_wine(self):
        reply = QMessageBox.question(self, 'Wine Yeniden Kurulum',
                                    'Wine yeniden kurulacak. Devam edilsin mi?',
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.install_wine()


def main():
    app = QApplication(sys.argv)
    window = ERToSMainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
