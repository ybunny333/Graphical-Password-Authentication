 🔐 Graphical Password Authentication System

 📌 Overview

This project implements a graphical password authentication system where users select specific points (Points of Interest - POI) on an image instead of entering traditional text-based passwords.

 🚀 Features

* Graphical password using image-based input
* POI (Point of Interest) selection
* Tolerance radius for flexible click validation
* Coordinate normalization for resolution independence
* Secure password storage using SHA-256 hashing
* User-friendly GUI interface

 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* SHA-256 Hashing

 🔍 How It Works

1. User selects multiple points on an image
2. Each point is stored as coordinates
3. Coordinates are normalized
4. Data is hashed using SHA-256
5. During login, input is matched within a tolerance radius

 🔐 Security Advantages

* Resistant to shoulder surfing attacks
* Harder to guess than text passwords
* Secure storage using hashing
* No plain-text password storage

 ⚠️ Limitations

* Requires precise clicking
* Usability depends on image complexity
* Vulnerable if tolerance radius is too large

 📈 Future Improvements

* Add salting to hashing
* Implement database (SQLite/MySQL)
* Add login attempt limits
* Enhance UI/UX

 👨‍💻 Author

Yandrathi Bunny
