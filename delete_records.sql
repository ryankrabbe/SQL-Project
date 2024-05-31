-- delete records from the authors data set where last name is blank
delete from authors
where last = ''

-- delete records from the books data set where the title was Books Made into Movies in the 2000s
delete from books
where title = 'Books Made into Movies in the 2000s'