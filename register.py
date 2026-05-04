import cv2
import shutil
import os
from tkinter import Tk, filedialog, simpledialog, messagebox
from utils import generate_hash, combine_data
from config import ASSETS_PATH, DB_PATH, GRID_SIZE

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
    os.makedirs(ASSETS_PATH, exist_ok=True)
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    if not os.path.exists(DB_PATH):
        open(DB_PATH, 'w').close()

def select_image():
    root.lift()
    root.attributes('-topmost', True)
    return filedialog.askopenfilename(title="Select Image")

def click_event(event, x, y, flags, param):
    global img

    if event == cv2.EVENT_LBUTTONDOWN:

        # 🔒 LIMIT MAX 5
        if len(points) >= 5:
            messagebox.showwarning("Limit Reached", "Maximum 5 points allowed!")
            return

        temp = img.copy()
        cv2.circle(temp, (x, y), 10, (0, 0, 255), 2)
        cv2.imshow("Registration", temp)
        cv2.waitKey(300)
        cv2.imshow("Registration", img)

        word = simpledialog.askstring(
            "Secure Input",
            f"Enter word for ({x},{y})",
            show="*"
        )

        if word:
            points.append((x, y))
            words.append(word)

def register():
    global img, points, words
    points = []
    words = []

    setup_environment()

    messagebox.showwarning("Warning",
        "Do NOT use personal images (family/friends)")

    image_path = select_image()
    if not image_path:
        return

    saved_path = os.path.join(ASSETS_PATH, "user_image.jpg")
    shutil.copy(image_path, saved_path)

    img = cv2.imread(saved_path)
    if img is None:
        messagebox.showerror("Error", "Image load failed!")
        return

    img = resize_image(img)

    cv2.namedWindow("Registration", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Registration", 1200, 700)
    cv2.imshow("Registration", img)
    cv2.setMouseCallback("Registration", click_event)

    while True:
        key = cv2.waitKey(1)

        if key == 13:
            break
        elif key == 27:
            cv2.destroyAllWindows()
            return

        if cv2.getWindowProperty("Registration", cv2.WND_PROP_VISIBLE) < 1:
            break

    cv2.destroyAllWindows()

    # 🔥 VALIDATION
    if len(points) < 2:
        messagebox.showerror("Error", "Minimum 2 points required!")
        return

    if len(points) > 5:
        messagebox.showerror("Error", "Maximum 5 points allowed!")
        return

    combined = combine_data(points, words, GRID_SIZE)
    hashed = generate_hash(combined)

    with open(DB_PATH, "w") as f:
        f.write(saved_path + "\n")
        f.write(hashed)

    messagebox.showinfo("Success", "Registration Successful!")