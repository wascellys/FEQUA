import uvicorn

from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT
from sqlalchemy.orm import Session
from fastapi import FastAPI, Body, Depends

from app.auth.models import UserLoginSchema, UserSchema
from app.db.database import Base, engine, SessionLocal
from app.tools import service
from app.tools.schemas import Tags, Tools

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


users = []


@app.get("/tools/", dependencies=[Depends(JWTBearer())])
def get_tools(db: Session = Depends(get_db)):
    return service.get_tools(db=db)


@app.post("/tools/")
def create_tools(tool: Tools, db: Session = Depends(get_db)):
    tools = service.create_tools(db, tool=tool)
    return tools


@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    users.append(user)
    return signJWT(user.username)


@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.username)
    return {
        "error": "Wrong login details!"
    }


def check_user(data: UserLoginSchema):
    for user in users:
        if user.username == data.username and user.password == data.password:
            return True
    return False


if __name__ == "__main__":
    uvicorn.run(app, port=3000)
