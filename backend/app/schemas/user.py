from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):

    email: EmailStr
    full_name: str
    password: str


class UserUpdate(BaseModel):

    full_name: str | None = None
    email: EmailStr | None = None


class UserResponse(BaseModel):

    id: UUID
    email: EmailStr
    full_name: str
    created_at: datetime

    model_config = {
        'from_attributes': True
    }
