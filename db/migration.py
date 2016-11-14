import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
	"""Create people table
	"""
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False)
	needs_ac = Column(String)
	designation = Column(String, nullable=False)
	office = Column(String, nullable=False)
	l_space = Column(String)


class Room(Base):
	"""Create the rooms table
	"""
	__tablename__ = 'room'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String, nullable=False)
	r_type = Column(String, nullable=False)
	capacity = Column(Integer, nullable=False)
	members = Column(Text)

class DatabaseCreator(object):
    """
    Creates a db connection object
    """

    def __init__(self, db_name=None):
        self.db_name = db_name
        if self.db_name:
            self.db_name = db_name + '.sqlite'
        else:
            self.db_name = 'main.sqlite'
        self.engine = create_engine('sqlite:///' + self.db_name)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)
