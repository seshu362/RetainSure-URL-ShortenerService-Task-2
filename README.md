
# 🔗 URL Shortener Service

## Overview

A simple URL shortening service similar to Bitly or TinyURL. This Flask-based application supports shortening long URLs, redirection using short codes, and basic analytics such as click counts and timestamps. It uses **in-memory thread-safe storage**, making it ideal for learning and testing.


## 📁 Project Structure

```

url-shortener/
├── app/
│ ├── init.py # Flask app initialization
│ ├── main.py # Routes and API logic
│ ├── utils.py # URL validation and short code generator
│ └── storage.py # Thread-safe in-memory storage
│
├── tests/
│ └── test_api.py # Pytest test cases
│
├── requirements.txt # Python dependencies (Flask, pytest)
├── CHANGES.md # Change log (optional)
└── README.md # This file
```

## 🚀 Features

- Shorten long URLs into 6-character alphanumeric short codes
- Redirect short codes to original URLs
- Track click count and creation timestamp for each short URL
- Basic error handling
- URL validation using regex
- Thread-safe in-memory storage
- Clean architecture and modular code
- Includes test cases using pytest


## ✅ Requirements

- Python 3.8 or above
- Flask
- Pytest

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```
### 2. (Optional) Create and Activate a Virtual Environment

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
```
    python -m venv venv
    .\venv\Scripts\activate
```

### 3. Install Dependencies

```
    python -m flask --app app.main run
```

## ▶️ Running the Application

### Option 1: Using Flask CLI (recommended)
```
    python -m flask --app app.main run
```
### Option 2: Run main.py directly
```
    python app/main.py
```
- App runs at: http://localhost:5000

### 🧪 Running Tests
```
    pytest
