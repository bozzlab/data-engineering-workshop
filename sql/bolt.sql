#Lesson 2

SELECT * FROM movies
WHERE id = 6

SELECT * FROM movies
WHERE year BETWEEN 2000 AND 2010;

SELECT * FROM movies
WHERE year NOT BETWEEN 2000 AND 2010;

SELECT title, year FROM movies
WHERE year <= 2003;

#Lesson 3

SELECT * FROM movies
WHERE title LIKE "Toy Story%";

SELECT * FROM movies
WHERE director LIKE "John Lasseter;

SELECT * FROM movies
WHERE director NOT LIKE "John Lasseter";

SELECT * FROM movies
WHERE title LIKE "WALL-%;";

#Lesson 4

SELECT DISTINCT director FROM movies
ORDER BY director;

SELECT title FROM movies
ORDER BY year DESC LIMIT 4;

SELECT title FROM movies
ORDER BY title ASC LIMIT 5;

SELECT title FROM movies
ORDER BY title ASC LIMIT 5 OFFSET 5;

#Review

SELECT city, population 
FROM north_american_cities
WHERE country = "Canada";

SELECT city 
FROM north_american_cities 
WHERE country ="United States"
ORDER BY latitude DESC;

SELECT city, longitude 
FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;

SELECT city, population 
FROM north_american_cities
WHERE country = "Mexico"
ORDER BY population DESC
LIMIT 2;

SELECT city, population 
FROM north_american_cities
WHERE country = "United States"
ORDER BY population DESC
LIMIT 2 OFFSET 2;

#Lesson 6

SELECT m.title, b.domestic_sales, b.international_sales
FROM boxoffice b
JOIN movies m
ON b.movie_id = m.id;

SELECT m.title, b.domestic_sales, b.international_sales
FROM boxoffice b
JOIN movies m
ON b.movie_id = m.id
WHERE b.domestic_sales < b.international_sales;

SELECT m.title, b.Rating
FROM boxoffice b
JOIN movies m
ON b.movie_id = m.id
ORDER BY b.Rating DESC;
