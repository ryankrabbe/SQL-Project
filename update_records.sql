-- update records in the authors data set to blank where last name is Rowling
update authors
SET last = ''
where last = 'Rowling';

-- update records in the books data set to reflect Books Made into Movies in the 2000s
UPDATE books
SET title = 'Books Made into Movies in the 2000s'
WHERE year_published IN ('1925', '1813', '1954', '1997');