use it_step;
update customers set contactLastName = "changed" where contactLastName = "lee";


CREATE DATABASE info;
USE info;
CREATE TABLE homeworks (
	HomewrokNumber int not null auto_increment,
    CourseName varchar(45) not null,
    Grade varchar(3) not null,
    PRIMARY KEY (HomewrokNumber)
);
insert into homeworks (CourseName, Grade)
values
("Astronomy", "A"),
("Psichology","A+"),
("IT", "A");
CREATE TABLE Students (
	StudentID int not null auto_increment,
    StudentName varchar(45) not null,
    StudentLastName varchar(45) not null,
    GPA varchar(5) not null,
    PRIMARY KEY (StudentID)
);
select * from Students;
insert into Students (StudentName, StudentLastName, GPA)
values
("Paata", "Kurtiashvili", 3.55),
("Ketevan", "khoperia", 3.30),
("Ioane", "Kapianidze", 2.90);
select * from homeworks;
select * from Students;
DROP TABLE homeworks;
DROP TABLE students;
DROP DATABASE info;