# 🖱️ VisionMouse: Real-Time Gesture Interface

A lightweight, high-performance **Human-Computer Interaction (HCI)** tool that transforms any physical colored object into a touchless mouse. Using **OpenCV** and **HSV Color Space mapping**, this project enables OS-level cursor control via a standard webcam—no specialized hardware required.

---

## 🚀 Features
* **Touchless Navigation:** Control your system cursor across any screen resolution using real-time spatial tracking.
* **Zero-Latency Tracking:** Optimized for high FPS processing, ensuring smooth and responsive movement.
* **Robust Color Masking:** Utilizes **HSV (Hue, Saturation, Value)** filtering to isolate tracking objects from complex backgrounds.
* **Noise Reduction:** Implements **Morphological Transformations** (Erosion & Dilation) to eliminate jitter and background noise.
* **Dynamic Coordinate Mapping:** Uses **Linear Interpolation** to translate low-res camera coordinates to high-res display outputs.

---

## 🛠️ Technical Stack
* **Language:** Python 3.8
* **Computer Vision:** OpenCV (`cv2`)
* **Numerical Processing:** NumPy
* **GUI Automation:** PyAutoGUI

---

## 📦 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sharma-rajat-02/Computer-Vision.git
   cd Computer-Vision
