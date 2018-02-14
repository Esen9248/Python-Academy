CREATE DATABASE `onetoone` 
	DEFAULT CHARSET utf8
	COLLATE utf8_general_ci;

use `onetoone`;

create table `users`(
	`id` int auto_increment not null,
	`login` varchar(100) not null,
	`pass` varchar(100) not null,
	primary key(`id`)
) engine=InnoDB;

create table `profiles`(
	`id` int not null unique,
	`first name` varchar(100) not null,
	`last name` varchar(100),
	foreign key(`id`) references `users`(`id`) 
) engine=InnoDB;

insert into users (login, pass) values("User1", "his pass"),
	("User2", "second pass");

insert into `profiles`(`id`, `first name`, `last name`)
	values(1,"Name of user 1", "some last name");

select count(*) as COUNT from users;
# where id >3;

select avg(id) avarage_id, min(id) as min, max(id) as max from users;

select sum(id*2) as sum from users;

group by;

select `login`, avg(id) as id from users group by `login`
having id > 1;

select `login`,`pass`, avg(id) as id from users group by `login`, `pass`;

select * from users order by login asc #desc limit 3;

select distinct(login) from users;

select * from users where login like "%er1%";
