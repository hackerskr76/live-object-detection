# Live Object Detection Pipeline 🚀

A streamlined, end-to-end computer vision project implementing **YOLOv8** for real-time object detection. This repository provides a modular pipeline for both batch image processing and live video stream inference using Python and OpenCV.

## 📋 Features
- **Real-Time Inference:** High-performance detection using YOLOv8 via webcam.
- **Batch Processing:** Easily run inference on large datasets of images.
- **Custom Training Ready:** Pre-configured setup for training models on custom datasets.
- **Scalable Structure:** Clean organization for data, models, and source code.

## 🛠️ Tech Stack
- **Framework:** [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- **Language:** Python
- **Vision Library:** OpenCV
- **Environment:** Virtual Environments (venv)

## 🚀 Getting Started

### 1. Installation
Clone the repository and set up your environment:
```bash
git clone [https://github.com/hackerskr76/live-object-detection.git](https://github.com/hackerskr76/live-object-detection.git)
cd live-object-detection
python -m venv venv
.\venv\Scripts\activate
pip install ultralytics opencv-python
2. Running Inference
For Real-Time Detection (Webcam):

Bash
  python src/realtime.py
For Batch Inference:

Bash
  python src/batch_inference.py
📁 Project Structure
Plaintext
├── data/           # Dataset storage
├── models/         # Trained .pt weight files
├── src/            # Core scripts (inference, real-time pipeline)
└── data.yaml       # Dataset configuration
📈 Performance
The current pipeline is optimized for real-time performance, achieving ~30 FPS on standard CPUs.

Developed by Sahil Raut
