import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File, Depends
from app.services.transcriber import Transcriber
from app.services.llm_handler import LLMHandler
from app.deps import get_current_user
from app.database import SessionLocal
from app.models import Meeting
from app.models import TranscriptChunk
from app.session_store import add_chunk
from app.models import TranscriptChunk
from app.session_store import get_full_text, close_session
from app.session_store import start_session, add_chunk, get_full_text, close_session
from fastapi import Form, File, UploadFile, Depends

router = APIRouter()

UPLOAD_DIR = "temp"
os.makedirs(UPLOAD_DIR, exist_ok=True)   # 🔥 ensure folder exists

transcriber = Transcriber("small")
llm = LLMHandler("gemma3:1b")

@router.post("/analyze")
async def analyze(file: UploadFile = File(...), user=Depends(get_current_user)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    temp_path = os.path.join(UPLOAD_DIR, filename)

    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    transcript = transcriber.transcribe(temp_path)
    summary = llm.summarize(transcript)

    db = SessionLocal()
    meeting = Meeting(
        user_id=user.id,
        transcript=transcript,
        summary=summary
    )
    db.add(meeting)
    db.commit()

    os.remove(temp_path)

    return {"summary": summary}

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...), user=Depends(get_current_user)):
    filename = f"{uuid.uuid4()}_{file.filename}"
    temp_path = os.path.join(UPLOAD_DIR, filename)

    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    transcript = transcriber.transcribe(temp_path)

    os.remove(temp_path)

    return {
        "user": user.email,
        "transcription": transcript
    }

@router.post("/start_meeting")
def start_meeting(user=Depends(get_current_user)):
    session_id = start_session(user.id)
    return {"session_id": session_id}




@router.post("/stream_chunk")
async def stream_chunk(
    session_id: str = Form(...),
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):
    temp = f"temp/{uuid.uuid4()}.wav"
    with open(temp, "wb") as f:
        shutil.copyfileobj(file.file, f)

    text = transcriber.transcribe(temp)
    os.remove(temp)

    # 1️⃣ RAM
    add_chunk(session_id, text)

    # 2️⃣ DB
    db = SessionLocal()
    db.add(TranscriptChunk(
        user_id=user.id,
        session_id=session_id,
        text=text
    ))
    db.commit()

    return {"chunk_text": text}


@router.post("/end_meeting")
def end_meeting(session_id: str, user=Depends(get_current_user)):
    full_text = get_full_text(session_id)

    summary = llm.summarize(full_text)

    # Save final meeting
    db = SessionLocal()
    db.add(Meeting(
        user_id=user.id,
        transcript=full_text,
        summary=summary
    ))
    db.commit()

    close_session(session_id)

    return {"summary": summary}
