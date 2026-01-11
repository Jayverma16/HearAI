# 🧠 HearAI  
### Local AI Inference Backend for Speech & LLM Applications

HearAI is a **general-purpose local inference backend** designed to run AI models **entirely on your own machine**.  
It enables speech-to-text, meeting summarization, and local LLM-powered applications **without sending any data to the cloud**.

---

## ✨ Features

- 🎙️ **Speech-to-Text** using Whisper  
- 🧠 **Local LLMs** (LLaMA, Mistral, etc.)  
- 📄 **Meeting Summaries & Action Items**  
- 🔒 **100% Private — Runs Fully Offline**  
- ⚡ **FastAPI-based High-Performance API**  
- 📱 Works with **Mobile, Web & Desktop Apps**

---

## 🏗 Architecture

Mobile / Web / Desktop Apps
↓
HearAI API
↓
Whisper / LLM / AI Models
↓
Transcripts, Summaries, Actions


HearAI acts as the **AI brain** for all your local applications.

---

## 🛠 Tech Stack

- **FastAPI** – REST API  
- **Whisper** – Speech Recognition  
- **Local LLMs** – LLaMA, Mistral, etc.  
- **MySQL** – Memory, transcripts, sessions  
- **Python 3.12**  
- **Conda** – Environment management  

---

## 🚀 Setup

### 1️⃣ Create Environment

```bash
conda create --name HearAI python=3.12 -y
conda activate HearAI

2️⃣ Install Dependencies
pip install -r requirement.txt

3️⃣ Setup Database

Login to MySQL:

mysql -u root -p


Create database:

CREATE DATABASE voice_ai;

4️⃣ Configure Database

Open database.py and update:

mysql+pymysql://jay:StrongPassword123@localhost:3306/voice_ai


(Replace username and password if needed.)

▶️ Run the Backend

For local use:

uvicorn app.main:app --reload


For access from mobile or other devices on your Wi-Fi:

uvicorn app.main:app --host 0.0.0.0 --port 8000


The API will be available at:

http://localhost:8000


or

http://<your-local-ip>:8000

📡 What HearAI Is For

HearAI is not a single-purpose API.
It is a general AI inference engine that can power:

Voice assistants

Meeting & call summarizers

Offline ChatGPT-like apps

Smart note-taking apps

Enterprise AI tools

All running locally.

🔒 Why HearAI?
Feature	Benefit
Local execution	No cloud, no data leaks
Offline capable	Works without internet
Multi-model support	Speech + LLM + NLP
One backend	Multiple client apps
FastAPI	Easy integration
🧠 Vision

HearAI is built to be the core AI engine for private, offline, and secure intelligent applications.

Your voice.
Your data.
Your AI.


---

If you want, next I can help you add:

• API endpoint docs  
• Screenshots section  
• Logo & branding  
• Deployment guide  

Just say 😎
