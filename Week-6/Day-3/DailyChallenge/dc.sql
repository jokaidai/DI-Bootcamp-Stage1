-- insert into customer_profile(customer_id, isloggedin)
-- values 
-- ((select customer_id from customer where first_name = 'John' and last_name = 'Doe'),
-- true),
-- ((select customer_id from customer where first_name = 'Jerome' and last_name = 'Lalu'),
-- null);

-- select customer.first_name
-- from customer
-- inner join customer_profile
-- on customer.customer_id = customer_profile.customer_id
-- and customer_profile.isloggedin = true; 

-- select customer.first_name, customer_profile.isLoggedIn
-- from customer
-- left join customer_profile
-- on customer.customer_id = customer_profile.customer_id;

-- select count(*) as Offline_Customer
-- from customer
-- inner join customer_profile
-- on customer.customer_id = customer_profile.customer_id
-- and customer_profile.isloggedin = false;

-- create table book(
-- book_id serial primary key,
-- title varchar(100) not null,
-- author varchar(100) not null
-- );

-- insert into book(title, author)
-- values 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student(
-- student_id serial primary key,
-- student_name varchar(100) not null unique,
-- age int check(age between 0 and 15)
-- );

-- insert into student(student_name, age)
-- values 
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table library (
--   book_fk_id int not null,
--   student_fk_id int not null,
--   borowed_date date,
--   primary key (book_fk_id, student_fk_id),
--   foreign key (book_fk_id) references book(book_id) on delete cascade on update cascade,
--   foreign key (student_fk_id) references student(student_id) on delete cascade on update cascade
-- );

-- insert into library(book_fk_id, student_fk_id, borowed_date)
-- values 
-- ((select book_id from book where title = 'Alice In Wonderland'), 
-- (select student_id from student where student_name = 'John'),
--  '2022-02-15'),

-- ((select book_id from book where title = 'To kill a mockingbird'), 
-- (select student_id from student where student_name = 'Bob'),
--  '2021-03-03'),
 
--  ((select book_id from book where title = 'Alice In Wonderland'), 
-- (select student_id from student where student_name = 'Lera'),
--  '2021-05-03'),
 
--  ((select book_id from book where title = 'Harry Potter'), 
-- (select student_id from student where student_name = 'Bob'),
--  '2021-08-12');

-- select * from library;

-- select student.student_name, book.title as borowed_book
-- from library
-- inner join student
-- on library.student_fk_id = student.student_id
-- inner join book
-- on library.book_fk_id = book.book_id;

-- select avg (student.age) as average_age_alice
-- from library
-- inner join student
-- on library.student_fk_id = student.student_id
-- inner join book
-- on library.book_fk_id = book.book_id
-- where book.book_id = (select book_id from book where title = 'Alice In Wonderland')

-- delete from student where  student_id = 4;
-- select * from library;
-- select * from student;
