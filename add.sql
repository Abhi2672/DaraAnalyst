create database DataAnalytics;

use DataAnalytics;

create table Person(
    personId INT,
    person_name varchar(255),
    last_name varchar(255),
    address varchar(255),
    city varchar(255)

);

INSERT into Person values( 1 , "Abhishek", "More","Pune", "Maharashtra");
INSERT into Person values( 2 , "Kaushik", "Sai","Hyd", "Andrapradesh");
INSERT into Person values( 3 , "Shrihari", "Itha","Karnul", "Andrapradesh");


select * from person;

delete from Person where personId = 2;

update Person set last_name = "More" where personId = 3;


create table users(
   UserID  int auto_increment primary key ,
   UserName varchar(255) unique not null ,
   Email varchar(255) unique not null,
   passwords varchar(255) not null ,
   first_name varchar(255),
   last_name varchar(255),
   DateOfBirth date ,		
   CreatedAt datetime,
   lastlogin datetime,
   Status enum('Active','Inactive','Suspended'),
   index(Email)
);

desc users;

insert into users values (1,"Abhishek2672","abhsihekmore2672@gmail.com","Abhi@2672","Abhishek","More",'2002-07-26', now(),now(),'Active');

select * from users


create table student(
  student_id int primary key ,
  name varchar(255),
  age int ,
  check(age>18)
);

create table enrollements(
		enrollID int primary key,
        student_id int , 
        course_id int ,
        foreign key(student_id) references student(student_id)
);

insert into student values (1,"Virat", 20);
insert into enrollements values (11,2, 46);


select * from student;
select * from enrollements;

