import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File, Depends
from app.services.transcriber import Transcriber
from app.services.llm_handler import LLMHandler
from app.deps import get_current_user
from app.database import SessionLocal
from app.models import Meeting

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
