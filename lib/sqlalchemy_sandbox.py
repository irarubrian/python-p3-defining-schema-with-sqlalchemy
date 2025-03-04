#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import (create_engine, desc, CheckConstraint, primary_key_constraint, unique_constraint, index, Column, datetime, Integer, String)
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import sesssionmaker

Base = declarative_base()
    

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer(), primary_key=True)
    name = Column(String())


if __name__ == '__main__':


    engine = create_engine('sqlite:///student.db')
    Base.metadata.create_all(engine)