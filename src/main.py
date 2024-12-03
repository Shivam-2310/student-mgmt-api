from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from fastapi.responses import RedirectResponse
from .models import StudentCreate, StudentUpdate
from .crud import StudentCRUD

app = FastAPI(
    title="Student Management System",
    description="Backend API for Student Management"
)

student_crud = StudentCRUD()



@app.post("/students", status_code=201)
def create_students(student: StudentCreate):
    id = student_crud.create_students(student)
    return {"id": id}

@app.get("/students")
def list_students(
    country: Optional[str] = Query(None),
    age: Optional[int] = Query(None)
):
    students = student_crud.list_students(country, age)
    return {"data": students}

@app.get("/students/{id}")
def get_student(id: str):
    student = student_crud.get_student(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.patch("/students/{id}", status_code=204)
def update_student(id: str, student_update: StudentUpdate):
    success = student_crud.update_student(id, student_update)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}

@app.delete("/students/{id}")
def delete_student(id: str):
    success = student_crud.delete_student(id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {}
