SELECT year_published, COUNT(*) AS book_count
FROM books
GROUP BY year_published
ORDER BY year_published DESC;