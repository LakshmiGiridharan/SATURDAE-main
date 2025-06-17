📝 Overview
- SATURDAE (Simulated Automation Tool Using Recognizable DevOps Audio Execution) is a voice-controlled infrastructure layout simulator built in Python. Designed to mimic Infrastructure-as-Code (IaC) concepts through intuitive voice commands, the tool uses Turtle Graphics to visually render dynamic room and furniture layouts on a grid. It leverages speech recognition and text-to-speech for hands-free DevOps simulation, making it accessible to learners and non-programmers alike.

- This project blends visual programming, automation, and human-computer interaction to simulate smart space provisioning — similar to defining cloud infrastructure using tools like Terraform or Kubernetes, but made fun and educational.

❗ Problem Statement
- While Infrastructure-as-Code is a standard practice in DevOps, it remains abstract for beginners and difficult to visualize. Tools like Terraform or Ansible require knowledge of YAML or HCL, making them inaccessible for non-technical users. Furthermore, most existing simulators lack interactive or voice-driven capabilities that support experiential learning.

🎯 Why This Problem?
- As someone deeply engaged in both DevOps automation and technical education, I wanted to create a tool that demystifies IaC for students and hobbyists. The idea was to allow users to "speak" their infrastructure needs — much like giving instructions to a cloud assistant — and see them rendered dynamically.

- This project bridges DevOps and voice-driven interfaces in a gamified environment, promoting accessibility, hands-on learning, and creativity.

💡 Proposed Solution
- SATURDAE provides a unique voice-first interface for infrastructure simulation using:

✅ Speech-to-Command Interpretation
- Users can say things like “Add a bed to room 1” or “Create a new kitchen,” and the system interprets and executes the command using SpeechRecognition.

✅ 2D Layout Drawing with Turtle
- Infrastructure layouts are drawn in real-time on a 2D grid using Turtle Graphics. Each room and object has its own rendering logic.

✅ Collision Detection with NumPy
- NumPy arrays track the simulation grid and detect object overlap, avoiding furniture collisions or misplacement.

✅ Text-to-Speech Feedback with pyttsx3
- The simulator verbally confirms actions using TTS feedback — “Bed added to Bedroom 1,” “Object placement failed due to collision.”

✅ Modular Architecture
- Separate modules for furniture.py, rooms.py, and main.py promote reusability and clean code organization.

🏗️ Architecture & Features
```
Voice Input → SpeechRecognition → NLP Command Parsing
       ↓
Command Dispatch → Object Rendering (Turtle)
       ↓
NumPy Grid → Collision Check
       ↓
TTS Response (via pyttsx3) → Visual Update
```

✅ Core Functionalities
- Room provisioning (e.g., Bedroom, Kitchen)

- Furniture placement (e.g., Chair, Table, Bed)

- Grid-based layout management using arrays

- Feedback through both visual UI and audio

- Numba-accelerated logic for performance

🛠 Tech Stack
-Technology
```
Voice Input           SpeechRecognition, pyaudio
Graphics Rendering    Turtle
Grid Logic            NumPy, Numba
Voice Feedback        pyttsx3
Language              Python 3.8+
```
⚙️ Setup Instructions
🧪 Prerequisites
- Python 3.8+

- Microphone enabled on your system

- pyaudio installed (may require portaudio binaries)

📦 Installation
```
# Clone the repository
git clone https://github.com/LakshmiGiridharan/SATURDAE-main.git
cd SATURDAE-main

# Install dependencies
pip install -r requirements.txt
```

If you encounter issues with pyaudio, install via system-level package manager (e.g., brew install portaudio or use wheels for Windows)

🚀 Run the App
```
python main.py
```
The voice assistant will activate. Speak your infrastructure instructions clearly. Use keyboard/mouse to reset if needed.

📂 Project Structure
```
SATURDAE-main/
│
├── main.py                  # Entry point - voice engine + render loop
├── furniture.py             # Modular logic for furniture objects
├── rooms.py                 # Logic for different room types
├── assets/                  # Optional: icons or templates
├── utils/                   # Helper functions (grid, collision, TTS)
├── requirements.txt         # Python dependencies
└── README.md
```
🎮 Sample Commands to Try
- “Create a bedroom”

- “Add a table to kitchen”

- “Place a chair in room two”

- “Draw a bathroom”

- “Add a sofa to the hall”

🔭 Future Enhancements
🎨 3D Rendering with OpenGL
- Upgrade the UI from 2D Turtle Graphics to 3D rendering for immersive layouts.

📄 Export to IaC Format (Terraform)
- Convert visual layouts to Terraform YAML/JSON to teach actual provisioning syntax.

💾 Auto-save User Sessions
- Save current layout state and reload from previous simulation sessions.

🗣️ Multilingual Voice Support
Accept infrastructure commands in languages like Hindi, Spanish, or Tamil.

🌐 Web Version with Web Speech API
Make the simulator browser-based using WebSockets and JS voice APIs.
