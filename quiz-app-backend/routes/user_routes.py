from fastapi import Depends, APIRouter
from controllers import user_controller
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/login", tags=["users"])
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(form_data)
    return user_controller.login(form_data.username, form_data.password)



@router.get("/my-quizzes", tags=["users"])
async def list_my_quizzes():
    return {"message": "List of quizzes"}

@router.post("/quizzes/{quiz_id}/start", tags=["users"])
async def start_quiz(quiz_id: int):
    return {"quiz_id": quiz_id, "message": "Quiz started"}

@router.post("/quizzes/{quiz_id}/submit", tags=["users"])
async def submit_quiz(quiz_id: int):
    return {"quiz_id": quiz_id, "message": "Quiz submitted"}

@router.get("/quizzes/{quiz_id}/response", tags=["users"])
async def get_quiz_response(quiz_id: int):
    return {"quiz_id": quiz_id, "message": "Quiz response"}

