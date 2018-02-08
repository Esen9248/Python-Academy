show databases

CREATE DATABASE `test_class`
	DEFAULT CHARSET utf8
	COLLATE utf8_general_ci; 

use 'test_class';

show tables;

CREATE TABLE `users` (
	`id` INT AUTO_INCREMENT NOT NULL,
	`first_name` VARCHAR(20) NOT NULL,
	`age` INT NOT NULL,
	`biografy` TEXT,
	PRIMARY KEY(`id`)
) ENGINE=InnoDB;

SELECT id, first_name from `users`;

INSERT INTO `users` (
	`first_name`,
	`biografy`,
	`age`
	) VALUES("ESEN", "my biografy", 16);

SELECT * from `users`;

SELECT * FROM `users` WHERE `id` = 3; # !=, =>, >

SELECT * FROM `users` WHERE `id` = 3 AND `age` < 30;

SELECT * FROM `users` WHERE `id` = 3 OR `age` < 30;

SELECT * FROM `users` WHERE `age` BETWEEN 17 AND 30;

UPDATE `users` SET `age` = 10, `bio` = "New Bio" WHERE `id` = 3;

DELETE from `users` WHERE `id` = 3;

DROP TABLE `users`;