# 🛡️ Python Keylogger with Remote Logging

This is a Python-based keylogger that captures keystrokes on one machine and forwards the data to a remote server using HTTP POST requests. Built with `pynput`, `Flask`, and `requests`, it demonstrates how real-time input can be tracked, transmitted, and logged remotely for analysis or auditing.

---

## 🔑 Project Highlights
- Captures keystrokes using `pynput` listener.
- Sends keystrokes via `requests.post()` to a remote server.
- Stores captured data in `strokes.txt` on both machines.
- Uses a Flask app (`server.py`) to handle incoming POST data.
- Structured with separate modules for clean logic and scalability.

---

## 🔍 Key Features
- **Real-time Keystroke Capture**: Uses `pynput` to listen to and record every key press.
- **HTTP Forwarding**: Sends buffered strokes via `requests` POST to a Flask server endpoint.
- **Persistent Logging**: Appends all captured and received keystrokes to `strokes.txt` on both client and server.
- **Modular Design**: Separate scripts for capture (`keylog.py`), transmission (`post.py`), and reception (`server.py`/`postingdata.py`).
- **Lightweight Dependencies**: Only `pynput`, `requests`, and `Flask`.

---

## 💡 Uses
- **Security Audits**: Monitor authorized machines for compliance testing.
- **Usability Research**: Analyze typing patterns and keyboard ergonomics.
- **Debugging & QA**: Track user input flows during software testing.
- **Educational Demos**: Demonstrate networked I/O and Python scripting.

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/keylogger-project.git
cd keylogger-project
