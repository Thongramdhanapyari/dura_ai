# dura_ai
dura_ai is a simple ai that can talk to people when it is called (using ollama)

# Dura AI: Voice-Activated Agentic Assistant 

Dura is a locally-hosted, voice-activated AI assistant designed to act as a friendly and responsive companion. Built with Python and powered by **Llama 3.2 (1b)** via Ollama, it integrates real-time Speech-to-Text (STT) and Text-to-Speech (TTS) capabilities.

##  Features
- **Voice Recognition:** Uses Google Speech Recognition for high-accuracy Indian English (`en-in`) processing.
- **Local LLM:** Powered by Llama 3.2:1b for private, offline intelligence.
- **Natural TTS:** Implements `pyttsx3` for immediate vocal feedback.
- **Optimized Performance:** Configured with a `30m` keep-alive to ensure instant responses during active sessions.

##  Tech Stack
- **Language:** Python 3.10+
- **AI Model:** Llama 3.2:1b (via Ollama)
- **Voice Stack:** SpeechRecognition, Pyttsx3
- **Environment:** Isolated `.venv` for dependency management

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Thongramdhanapyari/dura_ai
   cd jarvis
   ```
   
2. **Set up Virtual Environment:**
```Bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. **Install Dependencies:**
```Bash
pip install -r requirements.txt
Install & Run Ollama:
```

4. **Download Ollama from ollama.com.**
```bash
Pull the model: ollama pull llama3.2:1b
```
5. **Usage**
Run the assistant:
```Bash
python main.py
Wake Word: "Dura"
```
Example: "Dura, how does a linked list work?"

Exit: Say "Goodbye Dura" or "Stop" to shut down.

