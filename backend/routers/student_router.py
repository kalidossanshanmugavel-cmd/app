from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from auth import get_current_user
from schemas.student_schema import StudentCreate, StudentResponse
from services.student_service import StudentService

router = APIRouter()
service = StudentService()

@router.get("/students", response_model=list[StudentResponse])
def get_students(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.get_students(db)

@router.post("/students", response_model=StudentResponse)
def create_student(
    request: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.insert_student(db, request)

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    request: StudentCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    student = service.update_student(db, student_id, request)

    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return student

@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    success = service.delete_student(db, student_id)

    if not success:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return {"message": "Student Deleted Successfully"}