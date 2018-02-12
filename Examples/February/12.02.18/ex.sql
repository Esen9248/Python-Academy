CREATE DATABASE `library2`
	DEFAULT CHARSET utf8
	COLLATE utf8_general_ci;

USE `library2`;

CREATE TABLE `writers`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`id`),

) ENGINE=InnoDB;

CREATE TABLE `books`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`title` VARCHAR(255) NOT NULL,
	`author_id` INT NOT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB;

CREATE TABLE `genres`(
	`id` INT AUTO_INCREMENT NOT NULL,
	`genre` VARCHAR(255) NOT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB;

INSERT INTO `writers` (`name`)
VALUES ("Ali"), ("Esen"), ("Dan"), ("Marat");

INSERT INTO `books` (`title`, `author_id`)
VALUES("book 1", 1), 
("book 2", 1), 
("book 3", 2),
("book 4", 2),
("book 5", 3),
("book 6", 4),
("book 7", 9);

ALTER TABLE `books`
	ADD FOREIGN KEY(`author_id`) 
	REFERENCES `writers`(`id`)
	ON DELETE CASCADE;

SELECT writers.name, books.title
FROM `books`
LEFT JOIN `writers`
ON writers.id = books.author_id;

CREATE TABLE `books_genres`(
	`book_id` INT NOT NULL,
	`genre_id` INT NOT NULL,
	FOREIGN KEY(`book_id`) REFERENCES `books`(`id`) ON DELETE CASCADE,
	FOREIGN KEY(`genre_id`) REFERENCES `genres`(`id`) ON DELETE CASCADE
) ENGINE=InnoDB;

SHOW CREATE TABLE `books_genres`;

INSERT INTO `genres`(`genre`) VALUES("Horror"),
("Fantasy"), ("Dramatic");

INSERT INTO `books_genres` (`book_id`, `genre_id`)
VALUES 
	(15,1),
	(17,2),
	(18,2),
	(19,3),
	(16,3),
	(19,1),
	(15,2);

SELECT writers.name, books.title, genres.genre
FROM books
LEFT JOIN writers
	ON writers.id=books.author_id
LEFT JOIN books_genres
	ON books_genres.book_id=books.id
RIGHT JOIN genres 
	ON genres.id=books_genres.genre_id
# выборка
WHERE  books_genres.genre_id= 1;