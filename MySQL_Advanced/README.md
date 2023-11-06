# MySQL Advanced
## Usage
The ``*init.sql`` files are meant to be run before their corresponding exercise.

Please run db-init.sql before testing the exercises.

```
$ sudo mysql
...
mysql> SOURCE db-init.sql;
...
mysql>
```

To run or test the exercises,
first run the ``#-init.sql`` file if it exists,
then the ``<exercise>.sql`` file (the exercise names are listed in the **Exercises** header in the README, below here), which should be the exercise file, then the ``#-main.sql`` file if it exists, to test that the exercise works.

```
mysql> SOURCE #-init.sql;
...
mysql> SOURCE #-...sql;

mysql> SOURCE #-main.sql;
<expected output here>
mysql>
```
## Exercises
### CREATE a TABLE with specific requests
- 0-uniq_users.sql
- 1-country_users.sql
### Rank results from a table of metal bands
- 2-fans.sql
- 3-glam_rock.sql
### CREATE TRIGGERs
- 4-store.sql - Count stock when orders are inserted
- 5-valid_email.sql
### CREATE PROCEDUREs
- 6-bonus.sql - Create a new bonus project, and give it to some students
- 7-average_score.sql - Calculate the average score of a student
### INDEX a TABLE!
- 8-index_my_names.sql
- 9-index_name_score.sql
### CREATE a FUNCTION!
- 10-div.sql
### CREATE a VIEW
- 11-need_meeting.sql
