-- create a database to store sales data
CREATE DATABASE hwone;
-- I need to use the database I just created
USE hwone;
-- Let's create a table to store sales details
CREATE TABLE sales (
    id INT AUTO_INCREMENT,
    seller VARCHAR(50),
    product VARCHAR(50),
    quantity INT,
    price FLOAT, -- I am using FLOAT to store price with decimals
    PRIMARY KEY (id)
);

-- add some sales data to the table
INSERT INTO sales (seller, product, quantity, price) VALUES
('James', 'Pen', 40, 1.99),
('James', 'Notebook', 23, 2.98),
('James', 'Eraser', 53, 0.50),
('John', 'Pen', 28, 1.80),
('John', 'Notebook', 31, 2.50),
('John', 'Eraser', 41, 0.40),
('Jack', 'Pen', 30, 1.70),
('Jack', 'Notebook', 29, 2.60),
('Jack', 'Eraser', 44, 0.35);
