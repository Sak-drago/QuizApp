from fastapi import APIRouter

router = APIRouter()

@router.post("/login", tags=["admin"])
async def login():
    return {"message": "Login successful"}

@router.get("/quizzes", tags=["admin"])
async def list_quizzes():
    return {"message": "List of quizzes"}

@router.post("/quizzes", tags=["admin"])
async def create_quiz():
    return {"message": "Quiz created"}

@router.post("/quizzes/{quiz_id}/questions", tags=["admin"])
async def add_question(quiz_id: int):
    return {"quiz_id": quiz_id, "message": "Question added"}

@router.get("/quizzes/{quiz_id}/participants", tags=["admin"])
async def list_participants(quiz_id: int):
    return {"quiz_id": quiz_id, "message": "List of participants"}

@router.get("/quizzes/{quiz_id}/responses/{user_id}", tags=["admin"])
async def list_responses(quiz_id: int):
    return {"quiz_id": quiz_id, "message": "List of responses"}
