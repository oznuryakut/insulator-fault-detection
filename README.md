# ⚡ Yüksek Gerilim İzolatörlerinde Hata Tespiti

Derin öğrenme tabanlı YOLOv8 modeli ve PySide6 arayüzü ile yüksek gerilim izolatörlerindeki fiziksel hasarları gerçek zamanlı olarak tespit eden masaüstü uygulaması.

---

## 🖥️ Arayüz Özellikleri

- Gerçek zamanlı kamera akışı üzerinde anlık nesne tespiti
- Fotoğraf çekme ve yerel görsel yükleme desteği
- Ayarlanabilir confidence threshold (slider ile)
- Tespit sonuçlarının **polygon maskesi** olarak görselleştirilmesi
- Koyu tema, sezgisel buton düzeni

---

## 📁 Proje Yapısı

```
├── best.pt          # Eğitilmiş YOLOv8 segmentasyon model ağırlıkları
├── app.py           # PySide6 masaüstü arayüzü
└── README.md
```

---

## 🗂️ Veri Seti

- **Görsel sayısı:** ~3.000 adet
- **Etiketleme türü:** Polygon (instance segmentation)
- **Hedef:** Yüksek gerilim izolatörlerindeki fiziksel hasarlar

---

## 🧠 Model Eğitimi

Model **Google Colab** üzerinde YOLOv8 segmentasyon mimarisi kullanılarak eğitilmiştir.

```python
from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")
model.train(data="data.yaml", epochs=100, imgsz=640)
```

---

## 🚀 Kurulum

### Gereksinimler

- Python 3.10+
- CUDA destekli GPU (opsiyonel, CPU ile de çalışır)

### Adımlar

```bash
# Repoyu klonla
git clone https://github.com/oznuryakut/yuksek-gerilim-izolator-hata-tespiti.git
cd yuksek-gerilim-izolator-hata-tespiti

# Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install ultralytics PySide6 opencv-python
```

---

## ▶️ Kullanım

```bash
python app.py
```

1. **Kamerayı Başlat** → Webcam akışını başlatır
2. **Fotoğraf Çek** → Mevcut kareyi dondurur
3. **Görsel Ekle** → Diskten görsel yükler
4. **Kullan ve Analiz Et** → Model çıkarımı yapar, polygon maskelerini gösterir
5. **Tekrar Çek** → Sıfırlar

Confidence eşiği slider ile 0.10 – 1.00 arasında ayarlanabilir.

---

## 🤖 Model

- Mimari: **YOLOv8 Segmentation**
- Etiket türü: **BBOX ve Polygon (instance segmentation)**
- Eğitim ortamı: Google Colab


---

## 🛠️ Teknolojiler

| Teknoloji | Kullanım |
|-----------|----------|
| YOLOv8-seg (Ultralytics) | Instance segmentation |
| PySide6 | Masaüstü GUI |
| OpenCV | Görüntü işleme |
| Google Colab | Model eğitimi |
| Python 3.10+ | Ana dil |

---
<img width="628" height="657" alt="7B0AC5A9-C859-4B2A-BEF6-A12CE09C34A1_1_201_a" src="https://github.com/user-attachments/assets/073e5101-4582-48de-95c5-24c65666ee1e" />
<img width="622" height="646" alt="3CF5D77C-E52A-4BAD-A385-DC1B3331FB0E_1_201_a" src="https://github.com/user-attachments/assets/489e7d68-8a2c-44cf-9b4f-1fd7a4b54862" />







