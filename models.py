from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class Gender(Enum):
    male = "male"
    female = "female"


class Roles(Enum):
    student = "student"
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Roles]


class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Roles]]


