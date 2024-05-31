SELECT
    COUNT(book_id) AS total_books,
    AVG(year_published) AS average_year_published,
    SUM(year_published) AS sum_year_published
FROM
    books;