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
connect: mysql -ujohnlinp -psecret somedb

# create table and populate data
left: DROP TABLE IF EXISTS person;
left: CREATE TABLE person (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id));
left: INSERT INTO person (name, age) VALUES ('John Lin', 29);

# start left transaction
left: SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
left: BEGIN;
left: SELECT age FROM person WHERE id = 1;

# start right transaction
right: BEGIN;
right: UPDATE person SET age = 30 WHERE id = 1;

# continue left transaction
left: SELECT age FROM person WHERE id = 1;

# continue right transaction
right: ROLLBACK;
```

2. Run `duosql <script-file>`.

3. Watch.
