# duosql

An easy way to demo database transactions.

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
connect: mysql -ujohnlinp -psecret duosql

# create table and populate data
left: CREATE TABLE IF NOT EXISTS person (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255) NOT NULL, PRIMARY KEY (id));
left: INSERT INTO person (name) VALUES ('John Lin');

# start left transaction
left: BEGIN;
left: SELECT COUNT(*) FROM person FOR UPDATE;

# start right transaction
right: BEGIN;
right: SELECT COUNT(*) FROM person FOR UPDATE;
```

2. Run `duosql <script-file>`.

3. Watch.
