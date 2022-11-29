from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Edy Wascellys",
                "username": "edywascellys",
                "password": "12345"
            }
        }
        orm_mode = True


class UserLoginSchema(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "edywascellys",
                "password": "12345"
            }
        }
        orm_mode = True
