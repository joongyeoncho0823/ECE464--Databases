# Joongyeon Cho
# ECE464 - Problem Set 1
# Question 2
# Make ORM Tables


from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
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
        return "<Sailor(id=%s, name='%s', rating=%s, age=%s)>" % (self.sid, self.sname, self.rating, self.age)


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

    def __repr__(self):
        return "<Boat(id=%s, name='%s', color=%s, length=%s)>" % (self.bid, self.bname, self.color, self.length)


Base.metadata.create_all(engine)
