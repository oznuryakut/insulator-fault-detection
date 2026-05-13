# ⚡ High Voltage Insulator Fault Detection

A desktop application that detects physical damage on high voltage insulators in real-time using a YOLOv8 deep learning model and a PySide6 interface.

---

## 🖥️ Interface Features

- Real-time object detection on live camera stream
- Photo capture and local image upload support
- Adjustable confidence threshold (via slider)
- Detection results visualized as **polygon masks**
- Dark theme with an intuitive button layout

---

## 📁 Project Structure

```
├── best.pt          # Trained YOLOv8 segmentation model weights
├── app.py           # PySide6 desktop application
└── README.md
```

---

## 🗂️ Dataset

- **Number of images:** ~3,000
- **Annotation type:** Polygon (instance segmentation)
- **Target:** Physical damage on high voltage insulators

---

## 🧠 Model Training

The model was trained on **Google Colab** using the YOLOv8 segmentation architecture.

```python
from ultralytics import YOLO
model = YOLO("yolov8n-seg.pt")
model.train(data="data.yaml", epochs=100, imgsz=640)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10+
- CUDA-compatible GPU (optional, also works on CPU)

### Steps

```bash
# Clone the repository
git clone https://github.com/oznuryakut/yuksek-gerilim-izolator-hata-tespiti.git
cd yuksek-gerilim-izolator-hata-tespiti

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install ultralytics PySide6 opencv-python
```

---

## ▶️ Usage

```bash
python app.py
```

1. **Start Camera** → Launches the webcam stream
2. **Take Photo** → Freezes the current frame
3. **Upload Image** → Loads an image from disk
4. **Analyze** → Runs model inference and displays polygon masks
5. **Retake** → Resets the view

The confidence threshold can be adjusted between 0.10 and 1.00 using the slider.

---

## 🤖 Model

- Architecture: **YOLOv8 Segmentation**
- Annotation type: **BBOX and Polygon (instance segmentation)**
- Training environment: Google Colab

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| YOLOv8-seg (Ultralytics) | Instance segmentation |
| PySide6 | Desktop GUI |
| OpenCV | Image processing |
| Google Colab | Model training |
| Python 3.10+ | Core language |

---

## 👩‍💻 Developer

**Öznur Yakut**  
[![GitHub](https://img.shields.io/badge/GitHub-oznuryakut-181717?style=flat&logo=github)](https://github.com/oznuryakut)

---

> © 2025 Öznur Yakut


---
<img width="628" height="657" alt="7B0AC5A9-C859-4B2A-BEF6-A12CE09C34A1_1_201_a" src="https://github.com/user-attachments/assets/073e5101-4582-48de-95c5-24c65666ee1e" />
<img width="622" height="646" alt="3CF5D77C-E52A-4BAD-A385-DC1B3331FB0E_1_201_a" src="https://github.com/user-attachments/assets/489e7d68-8a2c-44cf-9b4f-1fd7a4b54862" />







