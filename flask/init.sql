CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date DATETIME,
    total_amount DECIMAL
);

INSERT INTO orders (order_date) VALUES ('2024-05-07 10:30:00');

CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(255),  
    comment_date DATETIME
);

INSERT INTO comments (content, comment_date) VALUES ('good', '2024-05-07 10:30:00');

CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    content VARCHAR,
    publish_date DATETIME
);

INSERT INTO announcements (title, content, publish_date) VALUES ('arrangement', 'rest', '2024-05-07 10:30:00');

CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    amount DECIMAL,
    purchase_date DATETIME
);

INSERT INTO purchases (name, purchase_date, amount) VALUES ('mango','2024-05-07 10:30:00', 2);

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount DECIMAL,
    sales_date DATETIME
);

INSERT INTO sales (sales_date, amount) VALUES ('2024-05-07', 2);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-08', 2);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-09', 2);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-10', 2);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-11', 2);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    description VARCHAR,
    price DECIMAL(10,2),
    image TEXT
);

-- INSERT INTO products (name, description, price) VALUES ('mango', 'delicious', 2);
