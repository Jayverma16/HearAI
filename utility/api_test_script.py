import requests
from pydub import AudioSegment
import os
import uuid
import time 

BASE_URL = "http://localhost:8000"
EMAIL = "jay@gmail.com"
PASSWORD = "1234"
AUDIO_FILE = "/home/jay/Downloads/NVIDIA CEO Jensen Huang's Vision for the Future - Cleo Abram.mp3"   # 1 hour audio

CHUNK_LENGTH_MS = 60 * 1000   # 1 minute

# -------------------------------
# 1. Login
# -------------------------------
res = requests.post(f"{BASE_URL}/login", json={
    "email": EMAIL,
    "password": PASSWORD
})

token = res.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}
print("Logged in")

# -------------------------------
# 2. Start meeting
# -------------------------------
res = requests.post(f"{BASE_URL}/start_meeting", headers=headers)
session_id = res.json()["session_id"]
print("Session:", session_id)

# -------------------------------
# 3. Load and split audio
# -------------------------------
audio = AudioSegment.from_file(AUDIO_FILE)
chunks = audio[::CHUNK_LENGTH_MS]

# print("Total chunks:", len(chunks))

# -------------------------------
# 4. Stream chunks
# -------------------------------
for i, chunk in enumerate(chunks):
    fname = f"chunk_{i}.wav"
    chunk.export(fname, format="wav")

    with open(fname, "rb") as f:
        files = {"file": f}
        data = {"session_id": session_id}

        r = requests.post(
            f"{BASE_URL}/stream_chunk",
            headers=headers,
            files=files,
            data=data
        )
    
    os.remove(fname)
    time.sleep(1)
    # print(f"Chunk {i+1}/{len(chunks)} sent")

# -------------------------------
# 5. End meeting
# -------------------------------
res = requests.post(
    f"{BASE_URL}/end_meeting",
    headers=headers,
    params={"session_id": session_id}
)

print("\nFINAL SUMMARY:\n")
print(res.json()["summary"])
