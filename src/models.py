import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    first_name : Mapped[str] = mapped_column(nullable=False)
    last_name :  Mapped[str] = mapped_column(nullable=True)
    email : Mapped[str] = mapped_column(nullable=False)

class Follower(Base):
    __tablename__ = "Follower"

    user_from_id : Mapped[int] = Column(Integer, ForeignKey(User.id), primary_key = True, nullable=False)
    user_to_id : Mapped[int] = Column(Integer, ForeignKey(User.id), nullable=False)

    def to_dict(self):
        return {
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }

class Post(Base):
    __tablename__ = "Post"

    id : Mapped[int] = Column(Integer, primary_key = True)
    user_id : Mapped[int] = Column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }

class MediaType(enum.Enum):
    PHOTO = 1
    VIDEO = 2
    TEXT = 3

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id : Mapped[int] = Column(Integer, primary_key = True)
    type: Mapped[MediaType] = Column(Enum(MediaType), nullable=False)
    url: Mapped[str] = Column(String, nullable=False)
    post_id : Mapped[int] = Column(Integer, ForeignKey(Post.id))

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }
    
class Comment(Base):
    __tablename__ = "Comment"

    id : Mapped[int] = mapped_column(primary_key = True)
    author_id : Mapped[int] = Column(Integer, ForeignKey(User.id))

    def to_dict(self):
        return {
            "id": self.id,
            "author_id": self.author_id
        }


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
