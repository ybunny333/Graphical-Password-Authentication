import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 📁 Paths
ASSETS_PATH = os.path.join(BASE_DIR, "assets")
DB_PATH = os.path.join(BASE_DIR, "database", "users.txt")

# ⚙️ Settings
GRID_SIZE = 20
TOLERANCE = 20