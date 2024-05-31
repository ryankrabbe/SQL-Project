SELECT
    COUNT(book_id) AS total_books,
    AVG(year_published) AS average_year_published,
    MIN(year_published) AS min_year_published
FROM
    books;