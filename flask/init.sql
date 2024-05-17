CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content VARCHAR(255),  
    comment_date DATETIME
);

INSERT INTO comments (content, comment_date) VALUES ('The fruits here are really fresh and delicious! Every bite is filled with a sweet flavor, especially love their strawberries and melons.', '2024-05-07');
INSERT INTO comments (content, comment_date) VALUES ('The service attitude is very good! The staff warmly introduced various fruits, making the experience very pleasant.', '2024-05-08');
INSERT INTO comments (content, comment_date) VALUES ('Reasonable prices and high-quality fruits. Will visit again next time!', '2024-05-09');
INSERT INTO comments (content, comment_date) VALUES ('The only regret is that there are not enough varieties of fruits on the shelves. Hope the store can increase the selection.', '2024-05-10');
INSERT INTO comments (content, comment_date) VALUES ('I feel that the fruits here are much fresher than those in supermarkets, although slightly more expensive, but the quality is worth it.', '2024-05-11');

CREATE TABLE IF NOT EXISTS announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    content VARCHAR,
    publish_date DATETIME
);

INSERT INTO announcements (title, content, publish_date) VALUES ('Store Hours Adjustment', 'To better serve our customers, our store hours will be adjusted to 8 AM to 9 PM daily starting next week. Thank you for your understanding and support!', '2024-05-07');
INSERT INTO announcements (title, content, publish_date) VALUES ('Fresh Fruit Promotion', 'This weekend, all fresh fruits are 20% off! Do not miss this great opportunity to buy your favorite fruits. Welcome!', '2024-05-07');
INSERT INTO announcements (title, content, publish_date) VALUES ('Launch of Membership Points System', 'We are pleased to announce the launch of our membership points system. Earn one point for every yuan spent, and 100 points can be redeemed for a 10-yuan discount. Welcome to apply for a membership card!', '2024-05-07');
INSERT INTO announcements (title, content, publish_date) VALUES ('Store Relocation Notice', 'Dear customers, our store will be relocating to a new address at XX Road, No. XX next month. We apologize for any inconvenience caused during the move. The new store will provide a better shopping environment. We look forward to your visit!', '2024-05-07');
INSERT INTO announcements (title, content, publish_date) VALUES ('Job Openings', 'Our store is currently hiring cashiers and stock clerks. Candidates should be responsible, with relevant work experience preferred. Interested parties are welcome to inquire and apply! Contact number: XXXXXXXX.', '2024-05-07');

CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    amount DECIMAL,
    purchase_date DATETIME
);

INSERT INTO purchases (name, purchase_date, amount) VALUES ('Mango','2024-05-07', 20);
INSERT INTO purchases (name, purchase_date, amount) VALUES ('Blueberry','2024-05-08', 30);
INSERT INTO purchases (name, purchase_date, amount) VALUES ('Lemon','2024-05-09', 25);
INSERT INTO purchases (name, purchase_date, amount) VALUES ('Apple','2024-05-10', 80);
INSERT INTO purchases (name, purchase_date, amount) VALUES ('Lychee','2024-05-11', 20);
INSERT INTO purchases (name, purchase_date, amount) VALUES ('Durian','2024-05-12', 19);

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount DECIMAL,
    sales_date DATETIME
);

INSERT INTO sales (sales_date, amount) VALUES ('2024-05-07', 2);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-08', 100);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-09', 30);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-10', 80);
INSERT INTO sales (sales_date, amount) VALUES ('2024-05-11', 200);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    description VARCHAR,
    price DECIMAL(10,2),
    image TEXT
);

-- INSERT INTO products (name, description, price) VALUES ('mango', 'delicious', 2);
