from tables3 import Sailor, Boat, Employee, Payment, Reservation, Base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, aliased

engine = create_engine(
    'mysql+pymysql://root:password@127.0.0.1:3306/ECE464_PS1', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def check(mysql_query, orm_table):
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

    return orm_list == mysql_list


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

# simple test


def test():
    sql_query = "SELECT E1.eid, E1.ename FROM employees E1 WHERE E1.eid IN (SELECT P.eid from payments P WHERE P.amount = 200)"
    subq = session.query(Payment.eid).filter(
        Payment.amount == 200).subquery()
    orm_query = session.query(
        Employee.eid, Employee.ename).filter(Employee.eid.in_(subq))
    print_output(sql_query, orm_query)
    # assert check(sql_query, orm_query) #pytest


test()
