/* 182. Duplicate Emails

URL: https://leetcode.com/problems/duplicate-emails/

Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

*/

-- shema for testing

CREATE TABLE person (
  id integer auto_increment NOT NULL,
  email text NOT NULL,
  primary key (id)
);

INSERT INTO person (email) VALUES
  ('alfred@gmail.com'),
  ('alfred@gmail.com'),
  ('alfred@gmail.com'),
  ('mama@gmail.com'),
  ('mama@gmail.com'),
  ('mamat@gmail.com'),
  ('lala@mail.ru')
;

-- sql solution
SELECT Email FROM erson GROUP BY Email HAVING count(Email) > 1;
