CREATE DATABASE IF NOT EXISTS ECE464_PS1;
USE ECE464_PS1;

CREATE TABLE IF NOT EXISTS sailors(
    sid int PRIMARY KEY,
    sname varchar(30),
    rating int,
    age int
);

CREATE TABLE IF NOT EXISTS reserves(
    sid int,
    bid int,
    day date,
	PRIMARY KEY (sid, bid, day)
);

CREATE TABLE IF NOT EXISTS boats(
    bid int PRIMARY KEY,
	bname char(20),
	color char(10),
	length int
);

CREATE TABLE IF NOT EXISTS employees(
	eid int PRIMARY KEY,
    ename varchar(30),
    salary int,
    eposition varchar(30)
);

CREATE TABLE IF NOT EXISTS payments(
	pid int PRIMARY KEY,
    eid int,
    startdate date,
    enddate date,
    amount int
);

insert into sailors values (22,'dusting',7,45);
insert into sailors values (29,'brutus',1,33);
insert into sailors values (31,'lubber',8,55);
insert into sailors values (32,'andy',8,25);
insert into sailors values (58,'rusty',10,35);
insert into sailors values (64,'horatio',7,16);
insert into sailors values (71,'zorba',10,35);
insert into sailors values (74,'horatio',9,25);
insert into sailors values (85,'art',3,25);
insert into sailors values (95,'bob',3,63);
insert into sailors values (23,'emilio',7,45);
insert into sailors values (24,'scruntus',1,33);
insert into sailors values (35,'figaro',8,55);
insert into sailors values (59,'stum',8,25);
insert into sailors values (60,'jit',10,35);
insert into sailors values (61,'ossola',7,16);
insert into sailors values (62,'shaun',10,35);
insert into sailors values (88,'dan',9,25);
insert into sailors values (89,'dye',3,25);
insert into sailors values (90,'vin',3,63);

insert into reserves values (23,104,'1998/10/10');
insert into reserves values (24,104,'1998/10/10');
insert into reserves values (35,104,'1998/8/10');
insert into reserves values (59,105,'1998/7/10');
insert into reserves values (23,105,'1998/11/10');
insert into reserves values (35,105,'1998/11/6');
insert into reserves values (59,106,'1998/11/12');
insert into reserves values (60,106,'1998/9/5');
insert into reserves values (60,106,'1998/9/8');
insert into reserves values (88,107,'1998/9/8');
insert into reserves values (89,108,'1998/10/10');
insert into reserves values (90,109,'1998/10/10');
insert into reserves values (89,109,'1998/8/10');
insert into reserves values (60,109,'1998/7/10');
insert into reserves values (59,109,'1998/11/10');
insert into reserves values (62,110,'1998/11/6');
insert into reserves values (88,110,'1998/11/12');
insert into reserves values (88,110,'1998/9/5');
insert into reserves values (88,111,'1998/9/8');
insert into reserves values (61,112,'1998/9/8');
insert into reserves values (22,101,'1998/10/10');
insert into reserves values (22,102,'1998/10/10');
insert into reserves values (22,103,'1998/8/10');
insert into reserves values (22,104,'1998/7/10');
insert into reserves values (31,102,'1998/11/10');
insert into reserves values (31,103,'1998/11/6');
insert into reserves values (31,104,'1998/11/12');
insert into reserves values (64,101,'1998/9/5');
insert into reserves values (64,102,'1998/9/8');
insert into reserves values (74,103,'1998/9/8');

insert into boats values (101,'Interlake','blue', 45);
insert into boats values (102,'Interlake','red', 45);
insert into boats values (103,'Clipper','green', 40);
insert into boats values (104,'Clipper','red', 40);
insert into boats values (105,'Marine','red', 35);
insert into boats values (106,'Marine','green', 35);
insert into boats values (107,'Marine','blue', 35);
insert into boats values (108,'Driftwood','red', 35);
insert into boats values (109,'Driftwood','blue', 35);
insert into boats values (110,'Klapser','red', 30);
insert into boats values (111,'Sooney','gren', 28);
insert into boats values (112,'Sooney','red', 28);

insert into employees values (101, "John Clark", 50000, "Intern");
insert into employees values (102, "John Smith", 500000, "CEO");
insert into employees values (103, "John Ho Jr", 100, "Janitor");
insert into employees values (104, "John Ho Sr", 200, "Executive Janitor");
insert into employees values (105, "Janna Doon", 5000, "Front Desk");
insert into employees values (106, "Hannah Lee", 10000, "Maintanence person");

insert into payments values (001, 101, '2021/8/1', '2021/9/1', 100);
insert into payments values (002, 102, '2021/8/1', '2021/9/1', 200);
insert into payments values (003, 103, '2021/8/1', '2021/9/1', 50000);
insert into payments values (004, 104,'2021/8/1', '2021/9/1', 500000);
insert into payments values (006, 105,'2021/8/1', '2021/9/1', 5000);
insert into payments values (007, 106,'2021/8/1', '2021/9/1', 10000);
