from pydantic import BaseModel


class Phone(BaseModel):
    type_id: int
    country_code: int
    operator: int
    number: int
