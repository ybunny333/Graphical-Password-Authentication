import cv2
import os
from tkinter import Tk, simpledialog, messagebox
from utils import generate_hash, combine_data
from config import DB_PATH, GRID_SIZE
from home import open_home   # ✅ NEW

root = Tk()
root.withdraw()

points = []
words = []
img = None

def resize_image(img):
    screen_width = 1200
    screen_height = 700

    h, w = img.shape[:2]

    if w <= screen_width and h <= screen_height:
        return img

    scale = min(screen_width / w, screen_height / h)

    new_w = int(w * scale)
    new_h = int(h * scale)

    return cv2.resize(img, (new_w, new_h))

def setup_environment():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    if not os.path.exists(DB_PATH):
        open(DB_PATH, 'w').close()

def click_event(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_LBUTTONDOWN:
        temp = img.copy()
        cv2.circle(temp, (x, y), 10, (0, 255, 0), 2)
        cv2.imshow("Login", temp)
        cv2.waitKey(300)
        cv2.imshow("Login", img)

        word = simpledialog.askstring(
            "Secure Input",
            f"Enter word for ({x},{y})",
            show="*"   # 🔒 HIDDEN INPUT
        )

        if word:
            points.append((x, y))
            words.append(word)

def login():
    global img, points, words
    points = []
    words = []

    setup_environment()

    try:
        with open(DB_PATH, "r") as f:
            lines = f.readlines()
            if len(lines) < 2:
                messagebox.showwarning("Warning", "No user registered!")
                return
            image_path = lines[0].strip()
            stored_hash = lines[1].strip()
    except:
        messagebox.showwarning("Warning", "No user registered!")
        return

    img = cv2.imread(image_path)

    if img is None:
        messagebox.showerror("Error", "Image load failed!")
        return

    img = resize_image(img)

    cv2.namedWindow("Login", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Login", 1200, 700)
    cv2.imshow("Login", img)
    cv2.setMouseCallback("Login", click_event)

    while True:
        key = cv2.waitKey(1)

        if key == 13:
            break
        elif key == 27:
            cv2.destroyAllWindows()
            return

        if cv2.getWindowProperty("Login", cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()

    combined = combine_data(points, words, GRID_SIZE)
    hashed = generate_hash(combined)

    if hashed == stored_hash:
        messagebox.showinfo("Success", "Login Successful!")
        open_home()   # 🚀 REDIRECT
    else:
        messagebox.showerror(
            "Access Denied",
            "Access Denied!\nReason: Incorrect graphical password (wrong points or text)"
        )