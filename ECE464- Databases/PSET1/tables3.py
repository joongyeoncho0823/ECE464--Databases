# Joongyeon Cho
# ECE464: Problem Set 1
# Question 3
# Make ORM Tables w/ extra features

from sqlalchemy import create_engine
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
import getpass


engine = create_engine(
    'mysql+pymysql://root:password@127.0.0.1:3306/ECE464_PS1')
Base = declarative_base()


class Sailor(Base):
    __tablename__ = 'sailors'

    sid = Column(Integer, primary_key=True)
    sname = Column(String(30))
    rating = Column(Integer)
    age = Column(Integer)

    def __repr__(self):
        return "<Sailor(id=%s, name='%s', rating=%s, age = %s)>" % (self.sid, self.sname, self.rating, self.age)


class Reservation(Base):
    __tablename__ = 'reserves'
    __table_args__ = (PrimaryKeyConstraint('sid', 'bid', 'day'), {})

    sid = Column(Integer, ForeignKey('sailors.sid'))
    bid = Column(Integer, ForeignKey('boats.bid'))
    day = Column(DateTime)

    sailor = relationship('Sailor')

    def __repr__(self):
        return "<Reservation(sid=%s, bid=%s, day=%s)>" % (self.sid, self.bid, self.day)


class Boat(Base):
    __tablename__ = 'boats'

    bid = Column(Integer, primary_key=True)
    bname = Column(String(20))
    color = Column(String(10))
    length = Column(Integer)

    reservations = relationship("Reservation", backref='boats')

    def __repr__(self):
        return "<Boat(id=%s, name='%s', color=%s, length=%s)>" % (self.bid, self.bname, self.color, self.length)


class Employee(Base):
    __tablename__ = 'employees'

    eid = Column(Integer, primary_key=True)
    ename = Column(String(20))
    salary = Column(Integer)
    eposition = Column(String(20))

    def __repr__(self):
        return "<Employee(id=%s, name='%s', salary = %s, position='%s')>" % (self.eid, self.ename, self.salary, self.eposition)


class Payment(Base):
    __tablename__ = 'payments'

    pid = Column(Integer, primary_key=True)
    eid = Column(Integer, ForeignKey('employees.eid'))
    startdate = Column(DateTime)
    enddate = Column(DateTime)
    amount = Column(Integer)

    employees = relationship('Employee')

    def __repr__(self):
        return "<Payment(id=%s, eid=%s, startdate=%s, enddate=%s, amount=%s)>" % (self.pid, self.eid, self.startdate, self.enddate, self.amount)


Base.metadata.create_all(engine)
