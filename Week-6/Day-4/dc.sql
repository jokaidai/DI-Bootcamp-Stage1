-- create table items(
--     item_id serial primary key,
--     item_type varchar(100),
--     price integer not null
-- );

-- create table product_orders(
--     order_id serial primary key,
--     item_id integer not null,
--     order_date date,
--     delivered boolean default false,
--     foreign key(item_id) references items(item_id)
-- );

-- insert into items 
-- values
-- (default, 'Sony PS5', 2580),
-- (default, 'Mycrosoft Xbox Serie X', 2099),
-- (default, 'Nintendo Switch', 1365);

-- insert into product_orders
-- values
-- (default, (select item_id from items where item_type = 'Sony PS5'), '2022-03-29', false),
-- (default, (select item_id from items where item_type = 'Sony PS5'), '2022-04-17', false),
-- (default, (select item_id from items where item_type = 'Nintendo Switch'), '2022-05-10', false),
-- (default, (select item_id from items where item_type = 'Sony PS5'), '2022-05-30', false),
-- (default, (select item_id from items where item_type = 'Sony PS5'), '2022-06-02', false),
-- (default, (select item_id from items where item_type = 'Mycrosoft Xbox Serie X'), '2022-06-22', false),
-- (default, (select item_id from items where item_type = 'Nintendo Switch'), '2022-07-26', false);

-- create or replace function get_price_by_id(given_id int)
--  returns int as $priceOfOrder$
-- begin
--  return( select i.price
--     from product_orders as p
--     inner join items as i
--     on p.item_id = i.item_id
--     where p.order_id = given_id);
-- end;
-- $priceOfOrder$ language plpgsql;

-- select * from get_price_by_id(1);

-- create table users(
--     user_id serial primary key,
--     order_id integer not null,
--     first_name varchar(50),
--     last_name varchar(50),
--     foreign key(order_id) references product_orders(order_id)
-- );

insert into users 
values
(default,
 (Select order_id from product_orders where item_id = (select item_type from items where item_type = 'Sony PS5'))
 ,'Elie', 'Allouche'),
 
 (default,
 (Select order_id from product_orders where item_id = (select item_type from items where item_type = 'Mycrosoft Xbox Serie X'))
 ,'Roy', 'Benisti'),

(default,
 (Select order_id from product_orders where item_id = (select item_type from items where item_type = 'Nintendo Switch'))
 ,'Tal', 'Shlamovitch');