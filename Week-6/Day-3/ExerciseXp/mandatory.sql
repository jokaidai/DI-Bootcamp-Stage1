-- select name from language;

-- select f.title, f.description, l.name
-- from film as f 
-- inner join language as l
-- on f.language_id = l.language_id

-- select f.title, f.description, l.name
-- from film as f 
-- left join language as l
-- on f.language_id = l.language_id

-- select f.title, f.description, l.name
-- from film as f 
-- full join language as l
-- on f.language_id = l.language_id

-- create table new_film(
-- nf_id serial primary key,
-- nf_name = varchar(100)
-- );

-- insert into new_film
-- values
-- (default, 'Star Wars Episode I The Phantom Menace'),
-- (default, 'Star Wars Episode II Attack of the Clones'),
-- (default, 'Star Wars Episode III Revenge of the Sith'),
-- (default, 'Star Wars Episode IV A New Hope'),
-- (default, 'Star Wars Episode V The Empire Strikes Back'),
-- (default, 'Star Wars Episode VI  Return of the Jedi');

-- select * from new_film;

-- create table customer_review (
--     review_id serial not null primary key,
--     nf_id integer not null,
--     language_id integer not null,
--     title varchar(100),
--     score int check (score between 1 and 10),
--     review_text text,
--     last_update date,
--     foreign key (nf_id) references new_film(nf_id) on delete cascade,
--     foreign key (language_id) references language(language_id)
-- );

-- insert into customer_review
-- values
--   (default,
--   (select nf_id from new_film where nf_name = 'Star Wars Episode III Revenge of the Sith'), 
--   (select language_id from language where name = 'English'),
--   'The fall of Anakin', 9,
--   'Great movie all and all give young a wrong feeling that its gonna be boring at the beggining but more then make up for it by the middle and of course the extraordinary dramatical ending ... i cried like a baby :( i warmly recomend !!!',
--    '2022-07-27'),
   
--   (default,
--   (select nf_id from new_film where nf_name = 'Star Wars Episode V The Empire Strikes Back'), 
--   (select language_id from language where name = 'English'),
--   'Darth Vader identity reveal !!!', 10,
--   'Probably the best movie in the saga !!! there is so much happening Luke finally training like a real jedi meeting an old friend of ours ... and of course the big fight !! round 1 between Vader and Luke !! and as a matter of fact Vader as a lot to say to Luke more then you can imagine ....  I warmly recomend !!!',
--    '2022-07-27');

-- delete from new_film where nf_name = 'Star Wars Episode III Revenge of the Sith';

-- select * from new_film;

-- select * from customer_review;

