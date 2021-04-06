import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    type = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    post_id = Column(String(250), nullable=False)
    

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, ForeignKey('user.id'), primary_key=True)
    media = relationship(Media)
    user_id = Column(Integer, ForeignKey('media.id'))
    media = relationship(Media)

class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(Post)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=True)
    comment = Column(Integer, ForeignKey('comment.id'))
    comment = relationship(Comment)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')