import sys
import cv2
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel,
    QVBoxLayout, QWidget, QSlider, QHBoxLayout, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from ultralytics import YOLO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yüksek Gerilim İzalatörlerinde Hata Tespiti")
        self.setGeometry(200, 200, 650, 550)

   
        self.setStyleSheet("""
            QWidget {
                background-color: #2c2c2c;
                color: #f0f0f0;
                font-family: Arial;
            }
            QPushButton {
                background-color: #4a4a4a;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #555555;
            }
            QPushButton:hover {
                background-color: #555555;
            }
            QPushButton:pressed {
                background-color: #3a3a3a;
            }
            QPushButton:disabled {
                background-color: #333333;
                color: #888888;
                border-color: #222222;
            }
            QLabel#video_label {
                border: 2px solid #555555;
                border-radius: 10px;
                background-color: #1a1a1a;
            }
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: #3a3a3a;
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #00aaff;
                border: 1px solid #0055ff;
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }
        """)

       
        self.model = YOLO("best.pt")

   
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

   
        self.video_label = QLabel("Kamera başlatılmadı")
        self.video_label.setObjectName("video_label")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setFixedSize(600, 450)

        self.conf_label = QLabel("Confidence: 0.50")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.update_conf)

        self.start_btn = QPushButton("Kamerayı Başlat")
        self.start_btn.clicked.connect(self.start_camera)

        self.capture_btn = QPushButton("Fotoğraf Çek")
        self.capture_btn.clicked.connect(self.capture_photo)
        self.capture_btn.setEnabled(False)

        self.load_btn = QPushButton("Görsel Ekle")
        self.load_btn.clicked.connect(self.load_image)

        self.use_btn = QPushButton("Kullan ve Analiz Et")
        self.use_btn.clicked.connect(self.use_photo)
        self.use_btn.setEnabled(False)

        self.retry_btn = QPushButton("Tekrar Çek")
        self.retry_btn.clicked.connect(self.retry_photo)
        self.retry_btn.setEnabled(False)

     
        layout = QVBoxLayout()
        layout.addWidget(self.video_label)

        conf_layout = QHBoxLayout()
        conf_layout.addWidget(self.conf_label)
        conf_layout.addWidget(self.slider)
        layout.addLayout(conf_layout)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.capture_btn)
        btn_layout.addWidget(self.load_btn)
        layout.addLayout(btn_layout)

        action_layout = QHBoxLayout()
        action_layout.addWidget(self.use_btn)
        action_layout.addWidget(self.retry_btn)
        layout.addLayout(action_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Değişkenler
        self.current_frame = None
        self.captured_frame = None
        self.conf_threshold = 0.5
        self.camera_is_on = False

    def update_conf(self):
        self.conf_threshold = self.slider.value() / 100
        self.conf_label.setText(f"Confidence: {self.conf_threshold:.2f}")

    def start_camera(self):
        if self.camera_is_on:
            self.cap.release()
            self.timer.stop()
            self.video_label.setText("Kamera başlatılmadı")
            self.start_btn.setText("Kamerayı Başlat")
            self.capture_btn.setEnabled(False)
            self.load_btn.setEnabled(True)
            self.use_btn.setEnabled(False)
            self.retry_btn.setEnabled(False)
            self.camera_is_on = False
            return

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            QMessageBox.critical(self, "Hata", "Kamera açılamadı!")
            return
        
        self.timer.start(30)
        self.start_btn.setText("Kamerayı Durdur")
        self.capture_btn.setEnabled(True)
        self.load_btn.setEnabled(False)
        self.video_label.clear()
        self.camera_is_on = True

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.current_frame = frame
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            
            scaled_pixmap = QPixmap.fromImage(qimg).scaled(
                self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.video_label.setPixmap(scaled_pixmap)

    def capture_photo(self):
        if self.current_frame is not None:
            self.captured_frame = self.current_frame.copy()
            self.timer.stop()
            self.camera_is_on = False
            self.start_btn.setText("Kamerayı Başlat")
            self.capture_btn.setEnabled(False)
            self.load_btn.setEnabled(True)
            self.use_btn.setEnabled(True)
            self.retry_btn.setEnabled(True)
            
        
            rgb = cv2.cvtColor(self.captured_frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_pixmap = QPixmap.fromImage(qimg).scaled(
                self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.video_label.setPixmap(scaled_pixmap)

    def load_image(self):
        if self.camera_is_on:
            self.cap.release()
            self.timer.stop()
            self.camera_is_on = False
            self.start_btn.setText("Kamerayı Başlat")

        fname, _ = QFileDialog.getOpenFileName(
            self, "Görsel Seç", ".", "Image Files (*.png *.jpg *.jpeg)"
        )
        if fname:
            image = cv2.imread(fname)
            if image is None:
                QMessageBox.critical(self, "Hata", "Görsel yüklenemedi!")
                return
            
            self.captured_frame = image.copy()
            
            
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb.shape
            qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
            
            scaled_pixmap = QPixmap.fromImage(qimg).scaled(
                self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.video_label.setPixmap(scaled_pixmap)

            self.capture_btn.setEnabled(False)
            self.load_btn.setEnabled(True)
            self.use_btn.setEnabled(True)
            self.retry_btn.setEnabled(True)
            self.retry_btn.setEnabled(False)

    def use_photo(self):
        if self.captured_frame is not None:
            results = self.model.predict(self.captured_frame, conf=self.conf_threshold)
            annotated = results[0].plot()

            if len(results[0].boxes) == 0:
                QMessageBox.warning(self, "Sonuç", "⚠️ Nesne tanınmadı")
            else:
                rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb.shape
                qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)

                scaled_pixmap = QPixmap.fromImage(qimg).scaled(
                    self.video_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
                self.video_label.setPixmap(scaled_pixmap)

    def retry_photo(self):
        self.start_btn.setEnabled(True)
        self.load_btn.setEnabled(True)
        self.capture_btn.setEnabled(False)
        self.use_btn.setEnabled(False)
        self.retry_btn.setEnabled(False)
        self.video_label.setText("Kamera başlatılmadı")

        if self.cap and self.cap.isOpened():
            self.timer.start(30)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()