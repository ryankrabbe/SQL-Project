-- Insert the data below into the authors data set
insert into authors (author_id, first_name, last_name) values
('10f88232-1ae7-4d88-a6a2-dfcebb22a596', 'Harper', 'Lee'),
('c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70', 'George', 'Orvill'),
('e0b75863-866d-4db4-85c7-df9bb8ee6dab', 'F. Scott', 'Fizz'),
('7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d', 'Aldous', 'CoolGuy'),
('ba5bb514-146f-4d45-b83d-0dcebb22a596', 'J.K.', 'Growling'),
('de1e8f17-6a3b-49f4-bb75-4baaacff8a10', 'Douglas', 'Adams'),
('3b6e3f0d-bc87-4b73-94a7-0841a3f446c8', 'Mark', 'Spark'),
('4b4a7a5b-3563-499e-83b7-5b8b4a6c1e6b', 'Edgar', 'Allen Purr'),
('5c3f8f2e-d8a3-4faa-88f1-5b8b4a6c1e6b', 'Charles', 'Dickens'),
('1b3f5d8e-1a3d-4efa-ba9e-5b8b4a6c1e6b', 'Roald', 'Dahl'),
('a7b8b9c1-d1a1-4ea5-a5b8-5b8b4a6c1e6b', 'Terry', 'Pratchett');

-- inserts the data below into the books data set
insert into books (book_id, title, year_published, author_id) values
('10f88232-1ae7-4d88-a6a2-dfcebb22a596', 'To Kill a bird', 1955, 'f88232-1ae7-4d88-a6a2-dfcebb22a596'),
('c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70', '1987', 1952, 'a47e85-2a6b-4196-a7a8-8b55d8fc1f70'),
('e0b75863-866d-4db4-85c7-df9bb8ee6dab', 'The Great Gratsby', 1927, 'b75863-866d-4db4-85c7-df9bb8ee6dab'),
('7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d', 'Brave old World', 1936, '144e32-7ff4-4b58-8eb0-e63d3c9f9b8d'),
('ba5bb514-146f-4d45-b83d-0dcebb22a596', 'Animal Farm: A Fairy Tale', 1945, 'ba5bb514-146f-4d45-b83d-0dcebb22a596'),
('f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2', 'The Great Gutsby', 1925, 'de1e8f17-6a3b-49f4-bb75-4baaacff8a10'),
('38e530f1-228f-4d6e-a587-2ed4d6c44e9c', 'Brave New Whirl', 1932, '3b6e3f0d-bc87-4b73-94a7-0841a3f446c8'),
('c2a62a4b-cf5c-4246-9bf7-b2601d542e6d', 'The Catcher in the Hay', 1951, '4b4a7a5b-3563-499e-83b7-5b8b4a6c1e6b'),
('3a1d835c-1e15-4a48-8e8c-b12239604e98', 'Fahrenheit 451 Degrees', 1953, '5c3f8f2e-d8a3-4faa-88f1-5b8b4a6c1e6b'),
('c6e67918-e509-4a6b-bc3a-979f6ad802f0', 'Pride and Prejudice and Poodles', 1817, '1b3f5d8e-1a3d-4efa-ba9e-5b8b4a6c1e6b'),
('be951205-6cc2-4b3d-96f1-7257b8fc8c0f', 'The Hobbit: An Unexpected Napping', 1937, 'a7b8b9c1-d1a1-4ea5-a5b8-5b8b4a6c1e6b');