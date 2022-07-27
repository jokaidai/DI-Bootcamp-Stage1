-- select first_name as FirstName, last_name as LastName from employees

-- select distinct department_id from employees order by department_id asc;

-- select * from employees order by first_name desc;

-- select first_name, last_name, salary, salary * 0.15 as PF from employees;

-- select sum(salary) as payday  from employees;

-- select min(salary) as min_salary, max(salary) as max_salary from employees; 

-- select avg(salary) as average_salary from employees;

-- select count(*) as num_of_employees from employees;

-- select upper(first_name) from employees;

-- select substring(first_name, 1, 3) from employees;

-- select first_name ||' '|| last_name as full_name from employees;

-- select first_name, last_name, length(first_name ||''|| last_name) as LengthOfFullName from employees;

-- select first_name from employees where first_name  like '%[^0-9]%'

-- select * from employees limit 10; 

-- select first_name, last_name, salary from employees where salary between 10000 and 15000; 

-- select first_name last_name, hire_date from employees where hire_date between '1987-01-01' and  '1988-01-01';

-- select * from employees where first_name ilike '%c%e%';


-- select e.last_name, j.job_title, e.salary
-- from employees as e
-- inner join jobs as j
-- on e.job_id = j.job_id
-- where job_title not in ('Programmer', 'Shipping Clerk') and salary not in(4500, 10000, 15000);

-- select * from employees where last_name like '______';

-- select * from employees where last_name like '__e%';

-- select e.first_name, e.last_name, j.job_title 
-- from employees as e
-- inner join jobs as j
-- on e.job_id = j.job_id

-- select * from employees where last_name in ('Ford', 'Jones', 'Blake', 'Scott', 'King');
