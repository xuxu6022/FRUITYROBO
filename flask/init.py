import os
import sqlite3
import base64

db_file = 'student.db'

# 如果数据库文件不存在，则创建数据库文件并初始化数据
if not os.path.exists(db_file):
    conn = sqlite3.connect(db_file)
    print("Opened database successfully")

    # 读取 SQL 文件并执行
    with open('init.sql', 'r') as file:
        sql_script = file.read()
        conn.executescript(sql_script)

    # 读取图片并转换为 base64 编码
    with open("./images/mango.jpg", "rb") as image_file:    
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        # 将 base64 编码字符串存储到数据库中
        cursor = conn.cursor()
        # 使用PRAGMA语句查看指定表的列名
        table_name = 'products'  # 要查看的表名
        cursor.execute(f"PRAGMA table_info({table_name})")

        # 获取列名信息并打印
        columns = cursor.fetchall()
        for column in columns:
            print(column[1])  # column[1] 包含列名
        # cursor.execute("INSERT INTO products (name, image) VALUES ('mango', ?)", (encoded_string,))
        cursor.execute("INSERT INTO products (name, description, price, image) VALUES ('mango', 'delicious', 2, ?)", (encoded_string,))
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    conn.commit()
    conn.close()

    print("Database created and initialized successfully")
else:
    print("Database has initialized!")
    conn = sqlite3.connect(db_file)
    print("Opened database successfully")

    # 读取 SQL 文件并执行
    with open('init.sql', 'r') as file:
        sql_script = file.read()
        conn.executescript(sql_script)

    # 读取图片并转换为 base64 编码
    with open("./images/mango.jpg", "rb") as image_file:    
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        # 将 base64 编码字符串存储到数据库中
        cursor = conn.cursor()
        # 使用PRAGMA语句查看指定表的列名
        table_name = 'products'  # 要查看的表名
        cursor.execute(f"PRAGMA table_info({table_name})")

        # 获取列名信息并打印
        columns = cursor.fetchall()
        for column in columns:
            print(column[1])  # column[1] 包含列名
        cursor.execute("INSERT INTO products (name, description, price, image) VALUES ('mango', 'delicious', 2, ?)", (encoded_string,))
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    conn.commit()
    conn.close()

    print("Database created successfully")