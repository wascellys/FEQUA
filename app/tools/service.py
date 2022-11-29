from sqlalchemy.orm import Session

from app.tools.models import ToolsModel, TagsModel
from app.tools.schemas import Tools, Tags


def get_tools(db: Session):
    return db.query(ToolsModel).all()


def create_tools(db: Session, tool: Tools):
    tools_dict = tool.dict()
    tags = tools_dict.pop("tags")
    db_tools = ToolsModel(**tools_dict)
    db.add(db_tools)
    db.commit()
    db.refresh(db_tools)
    for tag in tags:
        db_tags = TagsModel(name=tag, tool=db_tools.id)
        db.add(db_tags)
        db.commit()
        db.refresh(db_tags)
    return db_tools


def create_tags(db: Session, tags: Tags):
    db_tags = TagsModel(**tags.dict())
    db.add(db_tags)
    db.commit()
    db.refresh(db_tags)
    return db_tags


def get_tags(db: Session):
    return db.query(TagsModel).all()
