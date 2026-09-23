from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

from routers.student_router import router as student_router
from routers.auth_router import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student CRUD with JWT Auth")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(student_router)


@app.get("/")
def home():
    return {
        "message": "FastAPI is running"
    }