import tkinter as tk
import time
import threading
import math

def open_home():
    home = tk.Tk()
    home.title("Secure System Access")
    home.geometry("1000x600")
    home.configure(bg="black")

    # 🔥 TITLE
    title = tk.Label(home,
                     text=">> ACCESS GRANTED <<",
                     font=("Courier", 22, "bold"),
                     fg="#00FF00",
                     bg="black")
    title.pack(pady=5)

    # MAIN FRAME
    main_frame = tk.Frame(home, bg="black")
    main_frame.pack(fill="both", expand=True)

    # =========================
    # 🧠 LEFT TERMINAL
    # =========================
    left_panel = tk.Frame(main_frame, bg="black")
    left_panel.pack(side="left", fill="y", padx=5)

    terminal = tk.Text(left_panel,
                       width=40,
                       bg="black",
                       fg="#00FF00",
                       font=("Courier", 10),
                       borderwidth=0)
    terminal.pack(fill="y", expand=True)

    logs = [
        "[+] Initializing secure session...",
        "[+] Verifying graphical credentials...",
        "[+] Hash match confirmed.",
        "[+] Access level: ADMIN",
        "[+] Loading system modules...",
        "[+] Establishing encrypted channel...",
        "[+] Scanning network ports...",
        "[+] Monitoring traffic...",
        "[+] No threats detected.",
        "[+] System stable.",
        "[+] Welcome, Agent."
    ]

    def run_terminal():
        while True:
            for log in logs:
                terminal.insert(tk.END, log + "\n")
                terminal.see(tk.END)
                time.sleep(0.3)

    threading.Thread(target=run_terminal, daemon=True).start()

    # =========================
    # 🌍 CENTER CYBER AREA
    # =========================
    center_panel = tk.Frame(main_frame, bg="black")
    center_panel.pack(side="left", fill="both", expand=True)

    canvas = tk.Canvas(center_panel, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    width = 700
    height = 500
    center_x = width // 2
    center_y = height // 2
    radius = 180

    # GRID BACKGROUND
    for i in range(0, width, 40):
        canvas.create_line(i, 0, i, height, fill="#003300")

    for j in range(0, height, 40):
        canvas.create_line(0, j, width, j, fill="#003300")

    # SPHERE POINTS
    points = []
    for i in range(0, 360, 10):
        for j in range(-80, 80, 10):
            x = radius * math.cos(math.radians(i)) * math.cos(math.radians(j))
            y = radius * math.sin(math.radians(j))
            z = radius * math.sin(math.radians(i)) * math.cos(math.radians(j))
            points.append([x, y, z])

    def rotate_y(point, angle):
        x, y, z = point
        new_x = x * math.cos(angle) - z * math.sin(angle)
        new_z = x * math.sin(angle) + z * math.cos(angle)
        return [new_x, y, new_z]

    def draw_scene():
        angle = 0
        while True:
            canvas.delete("globe")

            for p in points:
                rp = rotate_y(p, angle)
                x, y, z = rp

                scale = 400 / (400 + z)
                x2d = x * scale + center_x
                y2d = y * scale + center_y

                canvas.create_oval(x2d, y2d, x2d+3, y2d+3,
                                   fill="#00FF00",
                                   outline="",
                                   tags="globe")

            angle += 0.05
            time.sleep(0.03)

    threading.Thread(target=draw_scene, daemon=True).start()

    # =========================
    # 📊 RIGHT PANEL
    # =========================
    right_panel = tk.Frame(main_frame, bg="black")
    right_panel.pack(side="right", fill="y", padx=10)

    def label(text):
        return tk.Label(right_panel,
                        text=text,
                        font=("Courier", 10),
                        fg="#00FF00",
                        bg="black",
                        anchor="w")

    label("[ SYSTEM STATUS ]").pack(anchor="w", pady=5)
    label("User: ADMIN").pack(anchor="w")
    label("Access: FULL").pack(anchor="w")
    label("Firewall: ACTIVE").pack(anchor="w")
    label("Encryption: ENABLED").pack(anchor="w")

    label("\n[ NETWORK ]").pack(anchor="w", pady=5)
    label("IP: 192.168.0.101").pack(anchor="w")
    label("Status: SECURE").pack(anchor="w")

    label("\n[ GLOBAL NETWORK MAP ]").pack(anchor="w", pady=5)
    label("● USA").pack(anchor="w")
    label("● INDIA").pack(anchor="w")
    label("● EUROPE").pack(anchor="w")
    label("● JAPAN").pack(anchor="w")
    label("● AUSTRALIA").pack(anchor="w")

    # =========================
    # 🔘 LOGOUT BUTTON
    # =========================
    logout_btn = tk.Button(home,
                           text="LOG OUT",
                           command=home.destroy,
                           bg="black",
                           fg="#00FF00",
                           activeforeground="red",
                           font=("Courier", 12, "bold"),
                           borderwidth=2)
    logout_btn.pack(pady=5)

    home.mainloop()