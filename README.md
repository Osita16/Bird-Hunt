# 🎯 Bird Hunt – OpenCV Shooting Game

A fun, interactive computer vision game inspired by the classic 90’s *duck hunting arcade games* 🎮 — where you aim and shoot birds using a real-world object (blue pen) instead of a mouse!

---

## 🕹️ Inspiration

This project is inspired by the nostalgic 90’s bird shooting games where a dog would bring down the birds after you shot them.

Instead of using a controller, this version uses **computer vision** to track a colored object (blue pen) and turn it into a real-time aiming system.

> Bringing retro gaming + modern AI vision together 🚀

---

## Demo
https://github.com/user-attachments/assets/580f06b5-0940-41f2-b1d2-6f3ea8e1c64e


## 🚀 Features

* 🎯 Real-time object tracking using OpenCV (HSV color detection)
* 🔫 Aim using a **blue pen**
* 🐦 Moving bird with physics-like motion
* 💥 Hit detection with animation
* 📈 Score tracking system
* ⚡ Smooth gameplay with live webcam feed

---

## 🧠 Tech Stack

* Python 🐍
* OpenCV 👁️
* CvZone
* NumPy

---

## 📸 How It Works

1. Webcam captures live video
2. Frame converted to HSV color space
3. Blue object is detected using thresholding
4. Largest contour = pen tip position
5. Crosshair follows pen
6. If crosshair hits bird → score increases 🎉

---

## 🛠️ Installation

```bash
git clone git@github.com:your-username/bird-hunt.git
cd bird-hunt
pip install -r requirements.txt
python main.py
```

---

## 🎮 Controls

* Move blue pen → Aim
* Hit bird → Score increases
* Press **Q** → Quit game

---

## ⚙️ Customization

You can tweak:

```python
lower_color = np.array([100, 150, 100])
upper_color = np.array([140, 255, 255])
```

👉 Adjust based on lighting conditions

---

## 💡 Future Improvements

* 🔊 Gunshot sound effects
* 🐦 Multiple birds
* ⏱️ Timer mode (30 sec challenge)
* 🎯 Difficulty levels
* 🤖 Hand tracking instead of color detection
* 🧠 AI-based object detection (YOLO)

---

## 🌟 Why This Project Matters

This project demonstrates:

* Real-time computer vision
* Interactive system design
* Game logic implementation
* Practical OpenCV skills

---

## 👩‍💻 Author

**Osita Bharti**

Robotics enthusiast | Future AI + Vision Engineer 🚀

---

## ⭐ Show Some Love

If you like this project, give it a ⭐ on GitHub!

---
