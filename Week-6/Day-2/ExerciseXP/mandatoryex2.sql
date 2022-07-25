--  1 In the dvdrental database write a query to select all the columns from the “customer” table.

-- select * from customer;

--  2 Write a query to display the names (first_name, last_name) using an alias named “full_name”.

-- select concat(first_name , ' ' , last_name) as full_name from customer ;

--  3 Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
 
--  select distinct create_date from customer;
 
--  4 Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

-- select * from customer order by first_name desc;

--  5 Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate asc;

--  6 Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

-- select address, phone from address where district = 'Texas';

--  7 Write a query to retrieve all movie details where the movie id is either 15 or 150.

-- select * from film where film_id in (15, 150);

--  8 Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

-- select film_id, title, description, length, rental_rate from film where title ilike 'Star Wars';  

--  9 No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
  
-- select film_id, title, description, length rental_rate from film where title ilike 'St%';  
  
--  10 Write a query which will find the 10 cheapest movies.

-- select * from film order by replacement_cost asc limit 10; 

--  11 Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
--  Bonus: Try to not use LIMIT.
 
-- select * from film order by replacement_cost asc offset 10 limit 10;

--  12 Write a query which will join the data in the customer table and the payment table. You want to get the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

-- select customer.customer_id, payment.amount,payment.payment_date, payment.payment_id
-- from payment
-- inner join customer
-- on payment.customer_id = customer.customer_id;

--  13 You need to check your inventory. Write a query to get all the movies which are not in inventory.

-- select concat(film.film_id, ': ', film.title) as missing_from_inventory
-- from film
-- inner join inventory
-- on film.film_id != inventory.film_id;

-- select distinct film_id from inventory order by film_id asc;

--  14 Write a query to find which city is in which country.

-- select city.city, country.country
-- from city
-- inner join country
-- on city.country_id = country.country_id;

-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.