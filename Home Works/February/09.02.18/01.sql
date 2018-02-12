CREATE DATABASE `Library`
	DEFAULT CHARSET utf8
	COLLATE utf8_general_ci;

USE `Library`;


CREATE TABLE `writers` (
	`id` INT AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(100) NOT NULL,
	PRIMARY KEY(`id`)
) ENGINE=InnoDB;

INSERT INTO `writers` (
	`name`
) VALUES ("Чынгыз Айтматов"),
  	("Александр Пушкин"),
  	("Стивен Кинг");


CREATE TABLE `books`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`title` VARCHAR(200) NOT NULL,
	`autor` VARCHAR(100) NOT NULL,
	`year_of_publishing` INT NOT NULL,
	PRIMARY KEY(`id`)
) ENGINE=InnoDB;

INSERT INTO `books` (
	`title`, `autor`, `year_of_publishing`
) VALUES ("Джамиля", "Чынгыз Айтматов", 1958),
  	("Белый пароход","Чынгыз Айтматов", 1970),
  	("Материнское поле","Чынгыз Айтматов", 1963),
  	("Когда падают горы", "Чынгыз Айтматов", 2006),
  	("Руслан и Людмила", "Александр Пушкин", 1970),
  	("Евгений Онегин", "Александр Пушкин", 1823),
  	("Капитанская дочка", "Александр Пушкин", 1963),
  	("Оно", "Стивен Кинг", 1999),
  	("Темная Башня", "Стивен Кинг", 1958);

CREATE TABLE `chronology`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`year` INT NOT NULL,
	PRIMARY KEY(`id`)
) ENGINE=InnoDB;

INSERT INTO `chronology` (`year`) VALUES (1958),
	 (1970), (1963), (2006), (1823), (1999);

SELECT * from `writers`;
SELECT * from `books`;
SELECT * from `chronology`;

SELECT writers.name, books.title
FROM `writers`
INNER JOIN `books`
ON writers.name = books.autor;

SELECT chronology.year, books.title
FROM `chronology`
INNER JOIN `books`
ON chronology.year = books.year_of_publishing;

SELECT writers.name, books.title
FROM `books`
LEFT JOIN `writers`
ON writers.name = books.autor
where books.autor = "Чынгыз Айтматов";

SELECT chronology.year, books.title
FROM `books`
LEFT JOIN `chronology`
ON chronology.year = books.year_of_publishing
where books.year_of_publishing = 1970;
