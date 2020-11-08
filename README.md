# duosql

An easy way to demonstrate database transactions.

<img src="https://raw.githubusercontent.com/johnlinp/duosql/master/images/duosql-demo.gif" width="640" height="385" />


## Prerequisite

- Python 3.5+
- tmux


## Install

```
pip3 install duosql
```


## Usage

1. Create a .duo script file. For example:

```yaml
# connect command
connect: sqlite3 demo.sqlite3

# create table and populate data
left: DROP TABLE IF EXISTS person;
left: CREATE TABLE person (id INTEGER, name VARCHAR(255) NOT NULL, age INTEGER NOT NULL, PRIMARY KEY (id));
left: INSERT INTO person (name, age) VALUES ('Alice', 30);

# start left transaction and update a row
left: BEGIN;
left: UPDATE person SET age = 31 WHERE id = 1;

# update the same row on the right side and then stuck
right: PRAGMA busy_timeout = 100000;
right: UPDATE person SET age = 40 WHERE id = 1;

# continue left transaction and finally rollback so the right side can finish
left: UPDATE person SET age = 32 WHERE id = 1;
left: UPDATE person SET age = 33 WHERE id = 1;
left: ROLLBACK;
```

2. Run `duosql <script-file>`.

3. Watch.
