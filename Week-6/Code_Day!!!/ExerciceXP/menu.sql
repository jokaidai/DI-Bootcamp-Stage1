-- create table menu(
--     item_id serial primary key,
--     item_name varchar(100) not null,
--     item_price int not null
-- );

-- update menu set item_name = 'Burger', item_price = 35 where item_name = 'Pizza';  

truncate menu restart identity;

-- select * from menu;