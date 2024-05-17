from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from flask import abort

app = Flask(__name__)
CORS(app)

db_file = 'student.db'

# 连接到 SQLite 数据库
def get_db_connection():
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    return conn

# 获取所有销售数据
@app.route('/sales', methods=['GET'])
def get_sales():
    try:
        conn = get_db_connection()
        print("连接上啦！")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM sales LIMIT 30')
        sales = cursor.fetchall()
        conn.close()
        if not sales:
            # Return 404 if no orders found
            abort(404)
        return jsonify([dict(row) for row in sales]), 200
    except Exception as e:
        # Return 500 for any other exceptions
        return jsonify({'error': str(e)}), 500

# 获取所有评论数据
@app.route('/comments', methods=['GET'])
def get_comments():
    try:
        conn = get_db_connection()
        print("连接上啦！")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM comments LIMIT 5')
        comments = cursor.fetchall()
        conn.close()
        if not comments:
            # Return 404 if no orders found
            abort(404)
        return jsonify([dict(row) for row in comments]), 200
    except Exception as e:
        # Return 500 for any other exceptions
        return jsonify({'error': str(e)}), 500

# # 评论查询或关键词搜索
# @app.route('/comments/select', methods=['POST'])
# def query_comments():
#     try:
#         data = request.get_json()

#         id = data.get('id')
#         content = data.get('content')
#         comment_date = data.get('comment_date')

#         conn = get_db_connection()
#         cursor = conn.cursor()

#         query = "SELECT * FROM comments WHERE 1 = 1"
#         params = []

#         if id:
#             query += " AND id = ? "
#             params.append(id)
#         if content:
#             query += " AND content = ? "
#             params.append(content)
#         if comment_date:
#             query += " AND comment_date = ? "
#             params.append(comment_date)

#         cursor.execute(query, params)
#         rows = cursor.fetchall()

#         conn.close()

#         results = [dict(row) for row in rows]
#         if not results:
#             # 如果结果为空，返回404 Not Found
#             return jsonify({'error': 'No orders found matching the criteria'}), 404
#         else:
#             # 如果结果非空，返回200 OK
#             return jsonify(results), 200
#     except Exception as e:
#         # 发生异常时的处理
#         error_message = f"An error occurred: {str(e)}"
#         return jsonify({'error': error_message}), 500

# 评论删除
@app.route('/comments/delete', methods=['POST'])
def query_comments_delete():
    try:
        data = request.get_json()

        id = data.get('id')
        content = data.get('content')
        comment_date = data.get('comment_date')

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM comments WHERE 1 = 1"
        params = []

        if id:
            query += " AND id = ?"
            params.append(id)
        if content:
            query += " AND content = ?"
            params.append(content)
        if comment_date:
            query += " AND comment_date = ?"
            params.append(comment_date)

        cursor.execute(query, params)
        conn.commit()  # Commit changes to the database

        # Fetch the updated list of comments after deletion
        query_select_all = "SELECT * FROM comments"
        cursor.execute(query_select_all)
        rows = cursor.fetchall()

        conn.close()

        results = [dict(row) for row in rows]
        if not results:
            return jsonify({'error': 'No comments found matching the criteria'}), 404
        else:
            return jsonify(results), 200
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

# 获取公告详情
@app.route('/announcements/detail', methods=['GET'])
def get_announcements():
    try:
        # print(aid)
        conn = get_db_connection()
        print("连接上啦！")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM announcements ORDER BY id DESC')
        announcements = cursor.fetchall()
        conn.close()
        if not announcements:
            # Return 404 if no orders found
            abort(404)
        return jsonify([dict(row) for row in announcements]), 200
    except Exception as e:
        # Return 500 for any other exceptions
        return jsonify({'error': str(e)}), 500

# # 公告查询或关键词搜索
# @app.route('/announcements/select', methods=['POST'])
# def query_announcements():
#     try:
#         data = request.get_json()

#         id = data.get('id')
#         title = data.get('title')
#         content = data.get('content')
#         publish_date = data.get('publish_date')

#         conn = get_db_connection()
#         cursor = conn.cursor()

#         query = "SELECT * FROM announcements WHERE 1 = 1"
#         params = []

#         if id:
#             query += " AND id = ?"
#             params.append(id)
#         if title:
#             query += " AND title = ?"
#             params.append(title)
#         if content:
#             query += " AND content = ?"
#             params.append(content)
#         if publish_date:
#             query += " AND publish_date = ?"
#             params.append(publish_date)

#         cursor.execute(query, params)
#         rows = cursor.fetchall()

#         conn.close()

#         results = [dict(row) for row in rows]
#         if not results:
#             # 如果结果为空，返回404 Not Found
#             return jsonify({'error': 'No orders found matching the criteria'}), 404
#         else:
#             # 如果结果非空，返回200 OK
#             return jsonify(results), 200
#     except Exception as e:
#         # 发生异常时的处理
#         error_message = f"An error occurred: {str(e)}"
#         return jsonify({'error': error_message}), 500

# 获取商品信息
@app.route('/products/select', methods=['GET'])
def get_products():
    try:
        # print(aid)
        conn = get_db_connection()
        print("连接上啦！")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products LIMIT 20')
        products = cursor.fetchall()
        conn.close()
        if not products:
            # Return 404 if no orders found
            abort(404)
        return jsonify([dict(row) for row in products]), 200
    except Exception as e:
        # Return 500 for any other exceptions
        return jsonify({'error': str(e)}), 500

# 商品删除
@app.route('/products/delete', methods=['POST'])
def query_products_delete():
    try:
        data = request.get_json()

        id = data.get('id')
        
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM products WHERE 1 = 1"
        params = []

        if id:
            query += " AND id = ?"
            params.append(id)

        cursor.execute(query, params)
        conn.commit()

        query_select_all = "SELECT * FROM products"
        cursor.execute(query_select_all)
        rows = cursor.fetchall()

        conn.close()

        results = [dict(row) for row in rows]
        if not results:
            # 如果结果为空，返回404 Not Found
            return jsonify({'error': 'No orders found matching the criteria'}), 404
        else:
            # 如果结果非空，返回200 OK
            return jsonify(results), 200
    except Exception as e:
        # 发生异常时的处理
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

# 商品增加
@app.route('/products/add', methods=['POST'])
def query_products_add():
    try:
        data = request.get_json()

        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        image = data.get('image')

        conn = get_db_connection()
        cursor = conn.cursor()

        query_insert = "INSERT INTO products ( name, description, price, image) VALUES (?, ?, ?, ?)"
        params = ( name, description, price, image)

        cursor.execute(query_insert, params)
        conn.commit()  # 提交事务

        query_select_all = "SELECT * FROM products"
        cursor.execute(query_select_all)
        rows = cursor.fetchall()

        conn.close()

        results = [dict(row) for row in rows]
        if not results:
            # 如果结果为空，返回404 Not Found
            return jsonify({'error': 'No orders found matching the criteria'}), 404
        else:
            # 如果结果非空，返回200 OK
            return jsonify(results), 200
    except Exception as e:
        # 发生异常时的处理
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

# 商品修改   
@app.route('/products/update', methods=['PUT'])
def products_update():
    try:
        data = request.get_json()

        product_id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')
        image = data.get('image')

        conn = get_db_connection()
        cursor = conn.cursor()

        query_update = "UPDATE products SET name=?, description=?, price=?, image=? WHERE id=?"
        params = (name, description, price, image, product_id)

        cursor.execute(query_update, params)
        conn.commit()

        query_select_all = "SELECT * FROM products"
        cursor.execute(query_select_all)
        rows = cursor.fetchall()

        conn.close()

        results = [dict(row) for row in rows]
        if not results:
            return jsonify({'error': 'No products found'}), 404
        else:
            return jsonify(results), 200
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

# 显示图片
@app.route('/image', methods=['GET'])
def get_image():
    try:
        conn = get_db_connection()
        print("连接上啦！")
        cursor = conn.cursor()
        cursor.execute('SELECT image FROM products WHERE id = 1')
        products = cursor.fetchall()
        conn.close()
        if not products:
            # Return 404 if no orders found
            abort(404)
        return jsonify([dict(row) for row in products]), 200
    except Exception as e:
        # Return 500 for any other exceptions
        return jsonify({'error': str(e)}), 500
    
# 获取所有采购数据
@app.route('/purchases', methods=['GET'])
def get_purchases():
    try:
        conn = get_db_connection()
        print("连接上啦！")
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM purchases LIMIT 20')
        purchases = cursor.fetchall()
        conn.close()
        if not purchases:
            # Return 404 if no orders found
            abort(404)
        return jsonify([dict(row) for row in purchases]), 200
    except Exception as e:
        # Return 500 for any other exceptions
        return jsonify({'error': str(e)}), 500

# # 采购查询和关键词搜索
# @app.route('/purchases/select', methods=['POST'])
# def query_purchases():
#     try:
#         data = request.get_json()

#         id = data.get('id')
#         amount = data.get('amount')
#         purchase_date = data.get('purchase_date')

#         conn = get_db_connection()
#         cursor = conn.cursor()

#         query = "SELECT * FROM purchases WHERE 1 = 1"
#         params = []

#         if id:
#             query += " AND id = ?"
#             params.append(id)
#         if amount:
#             query += " AND amount = ?"
#             params.append(amount)
#         if purchase_date:
#             query += " AND purchase_date = ?"
#             params.append(purchase_date)

#         cursor.execute(query, params)
#         rows = cursor.fetchall()

#         conn.close()

#         results = [dict(row) for row in rows]
#         if not results:
#             # 如果结果为空，返回404 Not Found
#             return jsonify({'error': 'No orders found matching the criteria'}), 404
#         else:
#             # 如果结果非空，返回200 OK
#             return jsonify(results), 200
#     except Exception as e:
#         # 发生异常时的处理
#         error_message = f"An error occurred: {str(e)}"
#         return jsonify({'error': error_message}), 500
    
# 采购删除
@app.route('/purchases/delete', methods=['POST'])
def query_purchases_delete():
    try:
        data = request.get_json()

        id = data.get('id')
        print(id)

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM purchases WHERE 1 = 1"
        params = []

        if id:
            query += " AND id = ?"
            params.append(id)
        cursor.execute(query, params)
        conn.commit()  # Commit changes to the database

        # Fetch the updated list of comments after deletion
        query_select_all = "SELECT * FROM purchases"
        cursor.execute(query_select_all)
        rows = cursor.fetchall()

        conn.close()

        results = [dict(row) for row in rows]
        if not results:
            return jsonify({'error': 'No comments found matching the criteria'}), 404
        else:
            return jsonify(results), 200
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

# 采购增加（进购）
@app.route('/purchases/add', methods=['POST'])
def query_purchases_add():
    try:
        data = request.get_json()

        name = data.get('name')
        amount = data.get('amount')
        purchase_date = data.get('purchase_date')

        conn = get_db_connection()
        cursor = conn.cursor()

        query_insert = "INSERT INTO purchases ( name, amount, purchase_date) VALUES (?, ?, ?)"
        params = ( name, amount, purchase_date)

        cursor.execute(query_insert, params)
        conn.commit()  # 提交事务

        query_select_all = "SELECT * FROM purchases"
        cursor.execute(query_select_all)
        rows = cursor.fetchall()

        conn.close()

        results = [dict(row) for row in rows]
        if not results:
            # 如果结果为空，返回404 Not Found
            return jsonify({'error': 'No orders found matching the criteria'}), 404
        else:
            # 如果结果非空，返回200 OK
            return jsonify(results), 200
    except Exception as e:
        # 发生异常时的处理
        error_message = f"An error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
