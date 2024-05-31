-- delete records from the authors data set where last name is blank
DELETE FROM authors
WHERE last = 'Rowling';

-- delete records from the books data set where the title was Books Made into Movies in the 2000s
DELETE FROM books
WHERE title = 'Books Made into Movies in the 2000s';