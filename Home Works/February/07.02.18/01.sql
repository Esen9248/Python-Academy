CREATE DATABASE `Cars`
	DEFAULT CHARSET utf8
	COLLATE utf8_general_ci; 

use 'Cars';

CREATE TABLE `my_cars` (
	`id` INT AUTO_INCREMENT NOT NULL,
	`model` VARCHAR(30) NOT NULL,
	`year` INT NOT NULL,
	`color` VARCHAR(20) NOT NULL,
	`volume` FLOAT(2,1) NOT NULL,
	`wtf_date` DATE NOT NULL,
	PRIMARY KEY(`id`)
) ENGINE=InnoDB;

INSERT INTO `my_cars` (
	`model`,
	`year`,
	`color`,
	`volume`,
	`wtf_date`
	) VALUES("Lamborghini Aventador", 2017, "white", 8.4, );

SELECT * from `my_cars`;