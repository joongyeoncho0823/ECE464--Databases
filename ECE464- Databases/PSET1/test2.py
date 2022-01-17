# Joongyeon Cho
# ECE464- Problem Set 1
# Question 2
# Test for Question 2

import pytest
from tables2 import Base, Sailor, Boat, Reservation
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker, aliased

engine = create_engine(
    'mysql+pymysql://root:password@127.0.0.1:3306/ECE464_PS1', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def check(mysql_query, orm_table):
    mysql_list = []
    orm_list = []
    with engine.connect() as connection:
        mysql_table = connection.execute(mysql_query)
        for row in mysql_table:
            mysql_list.append(row)
        for row in orm_table:
            orm_list.append(row)

    assert mysql_list == orm_list


def print_output(mysql_query, orm_table):
    mysql_list = []
    orm_list = []
    with engine.connect() as connection:
        mysql_table = connection.execute(mysql_query)
        for row in mysql_table:
            mysql_list.append(row)
            print(row)
        print("\n")
        for row in orm_table:
            orm_list.append(row)
            print(row)


def test1():
    sql_query = "SELECT B.bid, B.bname, COUNT(*) '# of Reserves' FROM boats B, reserves R WHERE B.bid = R.bid GROUP BY B.bid ORDER BY B.bid;"
    orm_query = session.query(Boat.bid, Boat.bname, func.count(
        '*').label('# of Reserves')).filter(Boat.bid == Reservation.bid).group_by(Boat.bid).order_by(Boat.bid)
    print_output(sql_query, orm_query)
    # check(sql_query, orm_query), "It doesn't work!"     # pytest


def test4():
    sql_query = "SELECT B.bid, COUNT(*) as Num_Res FROM boats B, reserves R WHERE B.bid = R.bid GROUP BY B.bid ORDER BY Num_Res DESC LIMIT 1"
    orm_query = session.query(Reservation.bid, func.count("*")).group_by(
        Reservation.bid).group_by(Reservation.bid).order_by(desc(func.count("*"))).limit(1)
    print_output(sql_query, orm_query)
    # check(sql_query, orm_query)  # pytest


test1()
test4()
