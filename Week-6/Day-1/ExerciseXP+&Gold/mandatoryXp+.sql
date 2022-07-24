-- create table students(
--  student_id serial primary key,
--  first_name varchar (100) not null,
--  last_name varchar(100) not null,
--  birth_date date not null
-- )

-- insert into students(first_name, last_name, birth_date)
-- values
-- ('Mark', 'Benichou', '1998-11-02'),
-- ('Yoan', 'Cohen', '2010-12-03'),
-- ('Lea', 'Benichou', '1987-07-27'),
-- ('Amelia', 'Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'),
-- ('Omer', 'Simpson', '1980-10-03');

-- insert into students(first_name, last_name, birth_date)
-- values ('Elie', 'Allouche', '1993-03-29');

-- select student_id from students where first_name = 'Elie'

-- select * from students

-- select first_name, last_name from students 

-- select first_name, last_name from students where student_id = 2

-- select first_name, last_name from students where first_name = 'Mark' and last_name = 'Benichou'

-- select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Mark'

-- select first_name, last_name from students where first_name ilike '%a%'

-- select first_name, last_name from students where first_name ilike 'a%'

-- select first_name, last_name from students where first_name ilike '%a'

-- select first_name, last_name from students where first_name like '%a_'

-- select first_name, last_name from students where student_id = 1 or student_id = 3

-- select * from students where birth_date >= '2000-01-01'

-- select * from students where student_id <= 4 order by last_name ASC

-- select * from students where birth_date = (select max(birth_date) from students)

-- select * from students offset 2 limit 3