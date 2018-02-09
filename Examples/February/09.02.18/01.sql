ALTER TABLE `my_cars` ADD `owner` VARCHAR(100) NOT NULL; # добавить колону в таблицу

ALTER TABLE `my_cars` 	MODIFY COLUMN `MODEL` VARCHAR(100); # изменить колону в таблице

ALTER TABLE `my_cars` DROP COLUMN `COLUMN_NAME`

SELECT students.name, my_cars.model
FROM `students`
INNER JOIN `my_cars` # RIGHT JOIN, LEFT JOIN
ON students.name = my_cars.owner;

SELECT students.name, my_cars.model
FROM `students`
INNER JOIN `my_cars`
ON students.name = my_cars.owner

union

select students.name, my_cars.model 
from `students` 
INNER JOIN `my_cars` 
ON students.name = my_cars.owner;


SELECT students.name, my_cars.model 
FROM `my_cars` LEFT JOIN `students`  
ON students.name = my_cars.owner 
where my_cars.owner = "ESEN";


SELECT students.name, my_cars.model
FROM `my_cars`
LEFT JOIN `students`
ON students.name = my_cars.owner 
where cars.owner = "ESEN";