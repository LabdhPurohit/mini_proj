import mysql.connector

mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="labdh1234",
     database="mini_proj"
     )


cursor = mydb.cursor()
# cursor.execute(f"select * from customers where email='labdhpurohit@gmail.com';")
# result = cursor.fetchall()
# print(result)

# def all_dogs():
#     cursor.execute(f"select * from pets where type='dog';")
#     result = cursor.fetchall()
#     for i in result:
#         print(i)


def earning_call():
    cursor.execute(f"SELECT SUM(p.price) AS total_price FROM orders o JOIN pets p ON o.p_id = p.id WHERE o.status = 'C';")
    rs = cursor.fetchall()
    return rs[0][0]

def no_orders_call():
    cursor.execute(f"SELECT COUNT(*) FROM orders;")
    rs = cursor.fetchall()
    return rs[0][0]

def no_completed_orders_call():
    cursor.execute(f"select count(*) from orders where status='C';")
    rs = cursor.fetchall()
    return rs[0][0]

def no_users_call():
    cursor.execute(f"select count(*) from customers;")
    rs = cursor.fetchall()
    return rs[0][0]

def no_dog_call():
    cursor.execute(f"select count(*) from pets where type='Dog';")
    rs = cursor.fetchall()
    return rs[0][0]

def no_cat_call():
    cursor.execute(f"select count(*) from pets where type='Cat';")
    rs = cursor.fetchall()
    return rs[0][0]

def not_completed_order_details():
    cursor.execute('''SELECT o.id AS ORDER_ID, c.name AS NAME, o.order_date_time AS DATE, c.email AS EMAIL, o.phone_no AS PHONE, o.address AS ADDRESS, p.type AS "PET'S TYPE", p.name AS "PET'S NAME", p.age AS "PET'S AGE", p.breed AS "PET'S BREED", p.gender AS "PET'S GENDER", p.spec_requirement AS "PET'S SPECIFIC REQUIREMENTS", p.price AS "PET'S PRICE" FROM orders o JOIN customers c ON o.c_id = c.id JOIN pets p ON o.p_id = p.id WHERE o.status = 'N';''')
    rs = cursor.fetchall()
    return rs
def completed_order_details():
    cursor.execute('''SELECT c.name AS NAME, o.order_date_time AS DATE, c.email AS EMAIL, o.phone_no AS PHONE, o.address AS ADDRESS, p.type AS "PET'S TYPE", p.name AS "PET'S NAME", p.age AS "PET'S AGE", p.breed AS "PET'S BREED", p.gender AS "PET'S GENDER", p.spec_requirement AS "PET'S SPECIFIC REQUIREMENTS", p.price AS "PET'S PRICE" FROM orders o JOIN customers c ON o.c_id = c.id JOIN pets p ON o.p_id = p.id WHERE o.status = 'C';''')
    rs = cursor.fetchall()
    return rs
# def all_cats():
#     cursor.execute(f"select id from customers where email = 'labdhpurohit@gmail.com'")
#     result2 = cursor.fetchall()
#     print(result2[0][0])