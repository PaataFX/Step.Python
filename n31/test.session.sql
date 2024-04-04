
-- @block
-- select * from customers;
-- select * from customers where creditLimit > 23000;
-- select * from customers where creditLimit < 23000;
-- select * from customers where creditLimit = 23000;
-- select * from customers where creditLimit != 23000;
-- select * from customers where creditLimit between 21000 and 23000;
-- select * from customers where creditLimit BETWEEN 11000 and 33000 ORDER BY creditLimit, contactFirstName  LIMIT 3;
-- SELECT * FROM customers WHERE contactFirstName like "%a " OR contactFirstName like "%a";


-- @block
SELECT * from customers;

-- @block

update customers set contactLastName = "changed" where contactLastName = "lee";