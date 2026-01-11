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



🚀 What HearAI Does

HearAI acts as the AI brain for your applications.

Audio / Text
      ↓
HearAI Backend
      ↓
Whisper / LLM / Custom Models
      ↓
Transcripts, Summaries, Actions


You can connect:

Mobile apps (React Native, Flutter)

Web apps

Desktop clients

to this single backend and run everything locally.

🧩 Tech Stack

FastAPI — REST API

Whisper / Speech Models — Speech-to-Text

Local LLMs (LLaMA, Mistral, etc.)

MySQL — Conversations, transcripts, memory

Python 3.12

Conda — Environment isolation

⚙️ Installation
1️⃣ Create Conda Environment
conda create --name HearAI python=3.12 -y
conda activate HearAI

2️⃣ Install Dependencies
pip install -r requirement.txt

3️⃣ Setup MySQL Database

Login to MySQL:

mysql -u root -p


Create database:

CREATE DATABASE voice_ai;

4️⃣ Configure Database URL

Open database.py and set:

mysql+pymysql://jay:StrongPassword123@localhost:3306/voice_ai


(Change username and password as needed)

▶️ Running HearAI

Start the backend:

uvicorn app.main:app --reload


On Ubuntu or Linux, HearAI will run on:

http://127.0.0.1:8000


To allow mobile devices on your Wi-Fi network:

uvicorn app.main:app --host 0.0.0.0 --port 8000

📡 API Purpose

HearAI is not a single-task API.

It is a general inference engine that can run:

Speech models (Whisper)

LLMs (LLaMA, Mistral, etc.)

Classification models

Summarizers

Action & intent engines

All locally, privately, and in real time.

🔒 Why HearAI?
Feature	Benefit
Runs locally	No cloud, no data leaks
Works offline	Airplane mode compatible
Supports multiple AI models	Speech, LLM, NLP
One backend for all apps	Mobile, Web, Desktop
Developer-friendly	FastAPI, REST, Python
🧠 Vision

HearAI is designed to be the core AI brain for: