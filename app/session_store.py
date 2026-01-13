import uuid

ACTIVE_SESSIONS = {}

def start_session(user_id):
    session_id = str(uuid.uuid4())
    ACTIVE_SESSIONS[session_id] = {
        "user_id": user_id,
        "chunks": []
    }
    return session_id

def add_chunk(session_id, text):
    ACTIVE_SESSIONS[session_id]["chunks"].append(text)

def get_full_text(session_id):
    return " ".join(ACTIVE_SESSIONS[session_id]["chunks"])

def close_session(session_id):
    return ACTIVE_SESSIONS.pop(session_id)
