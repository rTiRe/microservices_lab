from datetime import date

from pydantic import BaseModel

from src.schemas.phone import Phone


class Contact(BaseModel):
    id: int
    username: str
    given_name: str
    family_name: str
    phone: list[Phone]
    email: list[str]
    birthdate: date