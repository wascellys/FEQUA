from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class ToolsModel(Base):
    __tablename__ = "tools"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    link = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    tags = relationship("TagsModel", backref="tags")

    def __repr__(self):
        return f'{self.title}'


class TagsModel(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    tool = Column(Integer, ForeignKey("tools.id"))

    def __repr__(self):
        return f'{self.name}'
