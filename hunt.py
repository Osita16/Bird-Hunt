import cv2
import cvzone
import numpy as np
from random import randint

print("OpenCV Version:", cv2.__version__)

# ---------------- CONFIG ----------------
width, height = 1280, 720
BIRD_SCALE = 0.4
SCORE_PER_HIT = 50
# ----------------------------------------

# -------- COLOR RANGE (PINK / MAGENTA) --------
# Tuned for pink pen
lower_color = np.array([140, 80, 80])
upper_color = np.array([170, 255, 255])

# ---------------- LOAD IMAGES ----------------
backGround = cv2.imread("park.jpg")
bird_R = cv2.imread("bird_R.png", cv2.IMREAD_UNCHANGED)
bird_L = cv2.imread("bird_L.png", cv2.IMREAD_UNCHANGED)

if backGround is None or bird_R is None or bird_L is None:
    print("ERROR: Images not found")
    exit()

backGround = cv2.resize(backGround, (width, height))
bird_R = cv2.resize(bird_R, None, fx=BIRD_SCALE, fy=BIRD_SCALE)
bird_L = cv2.resize(bird_L, None, fx=BIRD_SCALE, fy=BIRD_SCALE)

bird_R_copy = bird_R.copy()
bird_L_copy = bird_L.copy()

h_bird, w_bird, _ = bird_R.shape

# ---------------- WEBCAM ----------------
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# ---------------- GAME VARIABLES ----------------
bird_x = randint(100, width - 200)
bird_y = randint(100, height - 300)
bird_dx = randint(4, 7)
bird_dy = randint(3, 6)
bird_dir = "R"

score = 0
hit_anim = False
angle = 0

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cam.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # -------- MASK FOR PINK --------
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Clean mask (VERY IMPORTANT)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img = backGround.copy()

    # -------- MOVE BIRD --------
    if not hit_anim:
        bird_x += bird_dx
        bird_y += bird_dy

        if bird_x <= 0 or bird_x >= width - w_bird:
            bird_dx *= -1
            bird_dir = "L" if bird_dir == "R" else "R"

        if bird_y <= 0 or bird_y >= height - h_bird - 100:
            bird_dy *= -1

    bird_img = bird_R if bird_dir == "R" else bird_L
    img = cvzone.overlayPNG(img, bird_img, (bird_x, bird_y))

    # -------- DETECT PINK PEN --------
    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > 300:   # Lowered for pen tip
            x, y, w, h = cv2.boundingRect(largest)
            cx = x + w // 2
            cy = y + h // 2

            # Crosshair
            cv2.circle(img, (cx, cy), 8, (0, 0, 255), -1)
            cv2.line(img, (cx - 20, cy), (cx + 20, cy), (0, 255, 0), 2)
            cv2.line(img, (cx, cy - 20), (cx, cy + 20), (0, 255, 0), 2)

            # -------- HIT CHECK --------
            if (bird_x < cx < bird_x + w_bird and
                bird_y < cy < bird_y + h_bird and
                not hit_anim):

                hit_anim = True
                angle = 0
                score += SCORE_PER_HIT

    # -------- HIT ROTATION --------
    if hit_anim:
        angle += 12
        rotated = cvzone.rotateImage(bird_img, angle)
        img = cvzone.overlayPNG(img, rotated, (bird_x, bird_y))

        if angle >= 90:
            hit_anim = False
            bird_x = randint(100, width - 200)
            bird_y = randint(100, height - 300)
            bird_dx = randint(4, 7)
            bird_dy = randint(3, 6)
            bird_R = bird_R_copy.copy()
            bird_L = bird_L_copy.copy()

    # -------- UI --------
    cv2.putText(img, "BIRD HUNT",
                (450, 60),
                cv2.FONT_HERSHEY_COMPLEX,
                1.8, (255, 0, 255), 4)

    cv2.putText(img, f"SCORE : {score}",
                (50, height - 40),
                cv2.FONT_HERSHEY_COMPLEX,
                1.5, (0, 255, 0), 3)

    cv2.imshow("BIRD HUNT", img)
    cv2.imshow("MASK (PINK)", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()