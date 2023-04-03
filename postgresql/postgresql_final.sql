-- Write a query to select the first ten items in the user tables, return the following columns: first_name, last_name, title, address1, address2, city, state, zip, and department, with a department value of 100 or 200.
SELECT
    CONCAT(users.first_name, ' ', users.last_name) AS full_name,
    users.title,
    users.address1,
    users.address2,
    users.city,
    users.state,
    users.zip,
    users.department
FROM
    users
WHERE
    users.department IN (100, 200)
LIMIT 10;
