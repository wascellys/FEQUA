from typing import Optional

from pydantic import BaseModel


class Tools(BaseModel):
    id: Optional[int]
    title: str
    link: str
    description: str
    tags: list

    class Config:
        orm_mode = True


class Tags(BaseModel):
    id: Optional[int]
    name: str
    tool: int

    class Config:
        orm_mode = True
