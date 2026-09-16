from pydantic import BaseModel, Field, EmailStr

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=0, lt=100)
    email: EmailStr
    department: str = Field(..., min_length=2, max_length=100)


class StudentUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., gt=0, lt=100)
    email: EmailStr
    department: str = Field(..., min_length=2, max_length=100)


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    department: str

    class Config:
        from_attributes = True