# datafun-05-sql

#### I created a new repo in Github
#### I added the README.md file when creating the new repo
#### I opened the Documents folder in File Explorer since that is where I wanted this project to be stored
#### I cloned the new repo to the Documents folder with the following command
```shell

git clone site_URL

```
## Opening project and adding files in VS Code

#### I opened the new project in VS Code
#### I added a .py file to write my code in
#### I added a .gitignore file
#### I added a requirements.txt file

#### I created a virtual environment using the code below

```shell
py -m venv .venv
.venv\Scripts\Activate

```
## Install packages in Virtual Envvironment

#### The code below installs pandas and pyarrows in the requirements.txt file
```shell

pip install pandas pyarrow
python -m pip freeze > requirements.txt

```

## Implement Different SQL Operations

#### Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements.

1. create_tables.sql - create your database schema using sql

```shell

CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT,
    last TEXT,
);

```

2. insert_records.sql - insert at least 10 additional records into each table.

```shell

insert into authors (author_id, first_name, last_name) values

insert into books (book_id, title, year_published, author_id) value

```

3. update_records.sql - update 1 or more records in a table.

```shell

update authors
SET last = ''
where last = 'Rowling';

UPDATE books
SET title = 'Books Made into Movies in the 2000s'
WHERE year_published IN ('1925', '1813', '1954', '1997');

```

4. delete_records.sql

```shell

delete from authors
where last = ''

delete from books
where title = 'Books Made into Movies in the 2000s'

```

