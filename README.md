# KeyLogger Project

> Capture and forward keystrokes in real time from a client machine to a local Flask server via HTTP POST. Utilises Python’s `pynput`, `requests`, and `Flask` for seamless logging. Ideal for research or auditing—use responsibly.

---

## 🚀 Overview

This project comprises two main components:

1. **Keylogger Source** (`keylog.py`, `post.py`):
   - Captures keystrokes on the client machine using `pynput`.
   - Buffers and sends strokes to a remote server via `post.py`.
   - Appends captured input to `strokes.txt` locally for backup.

2. **Server Trial** (`server.py`, `postingdata.py`):
   - Hosts a lightweight Flask server to receive keystroke payloads.
   - Processes and logs incoming data to `strokes.txt` in real time.

```bash
KeyLoggerProject/
├─ keylogger_source_code/
│  ├─ keylog.py
│  └─ post.py
├─ server_trial/
│  ├─ server.py
│  ├─ postingdata.py
│  └─ strokes.txt
└─ README.md

## 🔍 Key Features
- **Real-time Keystroke Capture**: Uses `pynput` to listen to and record every key press.
- **HTTP Forwarding**: Sends buffered strokes via `requests` POST to a Flask server endpoint.
- **Persistent Logging**: Appends all captured and received keystrokes to `strokes.txt` on both client and server.
- **Modular Design**: Separate scripts for capture (`keylog.py`), transmission (`post.py`), and reception (`server.py`/`postingdata.py`).
- **Lightweight Dependencies**: Only `pynput`, `requests`, and `Flask`.

## 💡 Uses
- **Security Audits**: Monitor authorized machines for compliance testing.
- **Usability Research**: Analyze typing patterns and keyboard ergonomics.
- **Debugging & QA**: Track user input flows during software testing.
- **Educational Demos**: Demonstrate networked I/O and Python scripting.

## ⚙️ Installation
1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/keylogger-project.git
   cd keylogger-project
