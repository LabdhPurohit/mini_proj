from flask import Flask, render_template, request
import mysql.connector
import table_calls as tc
import os
app = Flask(__name__)


mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="labdh1234",
     database="mini_proj"
     )


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', output="labdh")

@app.route('/create_acc', methods=['POST'])
def create_acc():
        global cus_id
        global email, name, password
        email = request.form['email']
        name = request.form['u_name']
        password = request.form['pass']
        mail_dup()
        if ab==1:
            return render_template('sign_up_page.html', output="Email Already Exists")
        elif ab==0:
            cursor = mydb.cursor()
            cursor.execute(f"INSERT INTO customers (name, email, password) VALUES ('{name}', '{email}', '{password}');")
            cursor.execute(f"select id from customers where email = '{email}';")
            result2 = cursor.fetchall()
            cus_id = result2[0][0]
            mydb.commit()
            return render_template('home.html', output=name)
        
@app.route('/login_email_verification', methods=['POST'])
def login_email_verification():
    global signin
    global cus_id, name
    if request.method=='POST':
        global email
        email = request.form['email']
        u_pass = request.form['pass']
        cursor = mydb.cursor()
        cursor.execute(f"select email from customers where email='{email}';")
        result = cursor.fetchall()
        check_email=f"[('{email}',)]"
        if str(result)==check_email:
            cursor.execute(f"select email, password from customers where email='{email}';")
            result = cursor.fetchall()
            credentials=f"[('{email}', '{u_pass}')]"
            if str(result)==credentials:
                cursor.execute(f"select id, name from customers where email = '{email}'")
                result2 = cursor.fetchall()
                for row in result2:
                    cus_id = row[0]
                    print(cus_id)
                    name = row[1]
                return render_template('home.html', output=name)
            elif str(result)!=credentials:
                return render_template('login_page.html', output="Wrong Credentials")
            else:
                return render_template('login_page.html', output="Something Went Wrong")
        elif str(result)!=check_email:
            return render_template('login_page.html', output="Your email doesn't exist")
        else:
            return render_template('login_page.html', output="Something Went Wrong")
    else:
        return render_template('login_page.html', output="ERROR")

def mail_dup():
     cursor = mydb.cursor()
     cursor.execute(f"select email from customers;")
     result = cursor.fetchall()
     global ab
     ab=0
     for row in result:
        v = str(row)
        value=v.strip("(),'")
        if email==value:
            ab=1
        else:
            pass


# Dog Booking 


@app.route('/d_submit_details', methods=['POST'])
def d_submit_details():
    global d_id, d_type, d_name, d_age, d_breed, d_gender, d_src, d_price
    submit_action = request.form['submit_action']
    d_id = 0
    d_type = ""
    d_name = ""
    d_age = 0
    d_breed = ""
    d_gender = ""
    d_src = ""
    d_price = 0.00
    print(submit_action, type(submit_action))
    mycursor = mydb.cursor()
    # mycursor.execute("select count(id) from pets where type='dog';")
    # result2 = mycursor.fetchall()
    # for i in range(1 ,result2[0][0]+1):
    #     mycursor.execute(f"select * from pets where id={i};")
    #     result = mycursor.fetchall()
    #     if int(submit_action) == result[0][0]:
    mycursor.execute(f"select * from pets where id={submit_action};")
    result = mycursor.fetchall()
    d_id = result[0][0]
    d_type = result[0][1]
    d_name = result[0][2]
    d_age = result[0][3]
    d_breed = result[0][4]
    d_gender = result[0][5]
    d_src = result[0][6]
    d_price = result[0][7]
    return render_template('dog_page.html', element_1 = False, element_2 = True, d_name=d_name, d_age=d_age, d_breed=d_breed, d_gender=d_gender, d_src=d_src, d_price = d_price, name=name)

@app.route('/d_info_submit', methods=['POST'])
def d_info_submit():
    phone = request.form['phone']
    addr = request.form['addr']
    mycursor = mydb.cursor()
    print(cus_id)
    print(phone, type(phone))
    print(addr, type(addr))
    # mycursor.execute(f"UPDATE Customers SET phone_no = {phone}, address = '{addr}' WHERE id = {cus_id};")
    mycursor.execute(f"INSERT INTO orders (c_id, p_id, status, phone_no, address) values({cus_id}, {d_id}, 'N', '{phone}', '{addr}');")
    mydb.commit()
    phone = ""
    addr = ""
    return render_template('home.html', output="Order Complete")


# Cat Booking 


@app.route('/c_submit_details', methods=['POST'])
def c_submit_details():
    global c_id, c_type, c_name, c_age, c_breed, c_gender, c_src, c_price
    submit_action = request.form['submit_action']
    c_id = 0
    c_type = ""
    c_name = ""
    c_age = 0
    c_breed = ""
    c_gender = ""
    c_src = ""
    c_price = 0.00
    print(submit_action, type(submit_action))
    mycursor = mydb.cursor()
    # mycursor.execute("select count(id) from pets where type='dog';")
    # result2 = mycursor.fetchall()
    # for i in range(1 ,result2[0][0]+1):
    #     mycursor.execute(f"select * from pets where id={i};")
    #     result = mycursor.fetchall()
    #     if int(submit_action) == result[0][0]:
    mycursor.execute(f"select * from pets where id={submit_action};")
    result = mycursor.fetchall()
    c_id = result[0][0]
    c_type = result[0][1]
    c_name = result[0][2]
    c_age = result[0][3]
    c_breed = result[0][4]
    c_gender = result[0][5]
    c_src = result[0][6]
    c_price = result[0][7]
    return render_template('cat_page.html', element_1 = False, element_2 = True, d_name=c_name, d_age=c_age, d_breed=c_breed, d_gender=c_gender, d_src=c_src, d_price = c_price, name=name)

@app.route('/c_info_submit', methods=['POST'])
def c_info_submit():
    phone = request.form['phone']
    addr = request.form['addr']
    mycursor = mydb.cursor()
    print(cus_id)
    print(phone, type(phone))
    print(addr, type(addr))
    # mycursor.execute(f"UPDATE Customers SET phone_no = {phone}, address = '{addr}' WHERE id = {cus_id};")
    mycursor.execute(f"INSERT INTO orders (c_id, p_id, status, phone_no, address) values({cus_id}, {c_id}, 'N', '{phone}', '{addr}');")
    mydb.commit()
    phone = ""
    addr = ""
    return render_template('home.html', output="Order Complete")

#complete_order(Tick Button)
@app.route('/complete_order', methods=['POST'])
def complete_order():
    tick_b = request.form['tick_b']
    print(tick_b)
    mycursor = mydb.cursor()
    mycursor.execute(f"Update orders set status = 'C' where id={tick_b};")
    mydb.commit()
    mycursor.execute('''SELECT o.id AS ORDER_ID, c.name AS NAME, o.order_date_time AS DATE, c.email AS EMAIL, o.phone_no AS PHONE, o.address AS ADDRESS, p.type AS "PET'S TYPE", p.name AS "PET'S NAME", p.age AS "PET'S AGE", p.breed AS "PET'S BREED", p.gender AS "PET'S GENDER", p.spec_requirement AS "PET'S SPECIFIC REQUIREMENTS", p.price AS "PET'S PRICE" FROM orders o JOIN customers c ON o.c_id = c.id JOIN pets p ON o.p_id = p.id WHERE o.status = 'N';''')
    rs1 = mycursor.fetchall()
    mycursor.execute('''SELECT c.name AS NAME, o.order_date_time AS DATE, c.email AS EMAIL, o.phone_no AS PHONE, o.address AS ADDRESS, p.type AS "PET'S TYPE", p.name AS "PET'S NAME", p.age AS "PET'S AGE", p.breed AS "PET'S BREED", p.gender AS "PET'S GENDER", p.spec_requirement AS "PET'S SPECIFIC REQUIREMENTS", p.price AS "PET'S PRICE" FROM orders o JOIN customers c ON o.c_id = c.id JOIN pets p ON o.p_id = p.id WHERE o.status = 'C';''')
    rs2 = mycursor.fetchall()
    return render_template('admin.html', my_list = rs1, my_list2 = rs2, big_element5=False, big_element4=False, big_element3=False, big_element2=True, big_element1=False)

#DOG DETAIL INSERT
@app.route('/insert_dog_table', methods=['POST'])
def insert_dog_table():
    d_name = request.form['d_name']
    d_age = request.form['d_age']
    d_breed = request.form['d_breed']
    d_gender = request.form['d_gender']
    d_sr = request.form['d_sr']
    d_price = request.form['d_price']
    file = request.files['image']
    
    if file.filename == '':
        return 'No selected file'
    
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO Pets (type, name, age, breed, gender, spec_requirement, price) VALUES ('Dog', '{d_name}', {d_age}, '{d_breed}', '{d_gender}', '{d_sr}', {d_price});")
    mydb.commit()
    mycursor.execute("SELECT id FROM pets ORDER BY id DESC LIMIT 1;")
    rs1 = mycursor.fetchall()
    d_id = rs1[0][0]
    # Specify the directory where you want to save the file
    upload_folder = 'Project/static/images/dogs'
    # Create the directory if it doesn't exist
    new_filename = 'dog_' + str(d_id) + '.jpg'
    # Save the file to the specified directory with the new filename
    file.save(os.path.join(upload_folder, new_filename))
    mycursor.execute("SELECT * from pets where type='dog';")
    rs2 = mycursor.fetchall()
    return render_template('admin.html', my_list3=rs2, show_element1=True, show_element2=False, show_pop1=True, big_element5=False,  big_element4=False, big_element3=True, big_element2=False, big_element1=False)
    

@app.route('/update_dog_table', methods=['POST'])
def update_dog_table():
    global update_button
    d_name = request.form['d_name']
    d_age = request.form['d_age']
    d_breed = request.form['d_breed']
    d_gender = request.form['d_gender']
    d_sr = request.form['d_sr']
    d_price = request.form['d_price']
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE Pets SET name = '{d_name}', age = {d_age}, breed = '{d_breed}', gender = '{d_gender}', spec_requirement = '{d_sr}', price = {d_price} WHERE id = '{update_button}';")
    mydb.commit()
    update_button = ""
    mycursor.execute(f"select * from pets where type='dog';")
    result2 = mycursor.fetchall()
    return render_template('admin.html', my_list3 = result2, show_element1 = True, show_element2 = False, show_pop2=True, big_element5=False,  big_element4=False, big_element3=True, big_element2=False, big_element1=False)

#CAT DETAIL INSERT
@app.route('/insert_cat_table', methods=['POST'])
def insert_cat_table():
    d_name = request.form['d_name']
    d_age = request.form['d_age']
    d_breed = request.form['d_breed']
    d_gender = request.form['d_gender']
    d_sr = request.form['d_sr']
    d_price = request.form['d_price']
    file = request.files['image']
    
    if file.filename == '':
        return 'No selected file'
    
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO Pets (type, name, age, breed, gender, spec_requirement, price) VALUES ('Cat', '{d_name}', {d_age}, '{d_breed}', '{d_gender}', '{d_sr}', {d_price});")
    mydb.commit()
    mycursor.execute("SELECT id FROM pets ORDER BY id DESC LIMIT 1;")
    rs1 = mycursor.fetchall()
    d_id = rs1[0][0]
    # Specify the directory where you want to save the file
    upload_folder = 'Project/static/images/cats'
    # Create the directory if it doesn't exist
    new_filename = 'cat_' + str(d_id) + '.jpg'
    # Save the file to the specified directory with the new filename
    file.save(os.path.join(upload_folder, new_filename))
    mycursor.execute("SELECT * from pets where type='cat';")
    rs2 = mycursor.fetchall()
    return render_template('admin.html', my_list3=rs2, show_element1=True, show_element2=False, show_pop1=True, big_element5=False,  big_element4=True, big_element3=False, big_element2=False, big_element1=False)
    #4 true

@app.route('/update_cat_table', methods=['POST'])
def update_cat_table():
    global update_button
    d_name = request.form['d_name']
    d_age = request.form['d_age']
    d_breed = request.form['d_breed']
    d_gender = request.form['d_gender']
    d_sr = request.form['d_sr']
    d_price = request.form['d_price']
    mycursor = mydb.cursor()
    mycursor.execute(f"UPDATE Pets SET name = '{d_name}', age = {d_age}, breed = '{d_breed}', gender = '{d_gender}', spec_requirement = '{d_sr}', price = {d_price} WHERE id = '{update_button}';")
    mydb.commit()
    update_button = ""
    mycursor.execute(f"select * from pets where type='cat';")
    result2 = mycursor.fetchall()
    return render_template('admin.html', my_list3 = result2, show_element1 = True, show_element2 = False, show_pop2=True, big_element5=False,  big_element4=True, big_element3=False, big_element2=False, big_element1=False)

    
#-------------------------------------------------------------------
#-------------------------------------------------------------------
# Redirecting Pages
#-------------------------------------------------------------------
#-------------------------------------------------------------------


#Login Page

@app.route('/login', methods=['GET'])
def login():
    return render_template('login_page.html', name="Shubha")

#SignUp Page

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up_page.html')

#Dog's Page

@app.route('/dogs', methods=['GET'])
def dogs():
    cursor = mydb.cursor()
    cursor.execute(f"select * from pets where type='dog';")
    result2 = cursor.fetchall()
    return render_template('dog_page.html', my_list = result2, element_1=True, element_2=False)

#Cat's Page

@app.route('/cats', methods=['GET'])
def cats():
    cursor = mydb.cursor()
    cursor.execute(f"select * from pets where type='cat';")
    result2 = cursor.fetchall()
    return render_template('cat_page.html', my_list = result2, element_1=True, element_2=False)


@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    if username == "ssl_admin" and password == "ssl@dmin1234":
        Total_Earnings = tc.earning_call()
        Total_No_Orders = tc.no_orders_call()
        Total_No_Completed = tc.no_completed_orders_call()
        Total_No_Users = tc.no_users_call()
        Total_No_Cat_Orders = tc.no_cat_call()
        Total_No_Dog_Orders = tc.no_dog_call()
        return render_template('admin.html', Total_Earnings=Total_Earnings, Total_No_Orders=Total_No_Orders, Total_No_Completed=Total_No_Completed, Total_No_Users=Total_No_Users, Total_No_Cat_Orders=Total_No_Cat_Orders, Total_No_Dog_Orders=Total_No_Dog_Orders, big_element5=False, big_element4=False, big_element3=False, big_element2=False, big_element1=True)
    else:
        return render_template('admin_login.html', output="Wrong Username or Password")

@app.route('/dashboard_page', methods=['GET'])
def dashboard_page():
    Total_Earnings = tc.earning_call()
    Total_No_Orders = tc.no_orders_call()
    Total_No_Completed = tc.no_completed_orders_call()
    Total_No_Users = tc.no_users_call()
    Total_No_Cat_Orders = tc.no_cat_call()
    Total_No_Dog_Orders = tc.no_dog_call()
    return render_template('admin.html', Total_Earnings=Total_Earnings, Total_No_Orders=Total_No_Orders, Total_No_Completed=Total_No_Completed, Total_No_Users=Total_No_Users, Total_No_Cat_Orders=Total_No_Cat_Orders, Total_No_Dog_Orders=Total_No_Dog_Orders, big_element5=False, big_element4=False, big_element3=False, big_element2=False, big_element1=True)

@app.route('/orders_page', methods=['GET'])
def orders_page():
    mycursor = mydb.cursor()
    mycursor.execute('''SELECT o.id AS ORDER_ID, c.name AS NAME, o.order_date_time AS DATE, c.email AS EMAIL, o.phone_no AS PHONE, o.address AS ADDRESS, p.type AS "PET'S TYPE", p.name AS "PET'S NAME", p.age AS "PET'S AGE", p.breed AS "PET'S BREED", p.gender AS "PET'S GENDER", p.spec_requirement AS "PET'S SPECIFIC REQUIREMENTS", p.price AS "PET'S PRICE" FROM orders o JOIN customers c ON o.c_id = c.id JOIN pets p ON o.p_id = p.id WHERE o.status = 'N';''')
    rs1 = mycursor.fetchall()
    mycursor.execute('''SELECT c.name AS NAME, o.order_date_time AS DATE, c.email AS EMAIL, o.phone_no AS PHONE, o.address AS ADDRESS, p.type AS "PET'S TYPE", p.name AS "PET'S NAME", p.age AS "PET'S AGE", p.breed AS "PET'S BREED", p.gender AS "PET'S GENDER", p.spec_requirement AS "PET'S SPECIFIC REQUIREMENTS", p.price AS "PET'S PRICE" FROM orders o JOIN customers c ON o.c_id = c.id JOIN pets p ON o.p_id = p.id WHERE o.status = 'C';''')
    rs2 = mycursor.fetchall()
    return render_template('admin.html', my_list = rs1, my_list2 = rs2, big_element5=False, big_element4=False, big_element3=False, big_element2=True, big_element1=False)

#----------------------------------------------------------------
#DOG DETAIL
#----------------------------------------------------------------
@app.route('/dog_data_page', methods=['GET'])
def dog_data_page():
    cursor = mydb.cursor()
    cursor.execute(f"select * from pets where type='dog';")
    result2 = cursor.fetchall()
    return render_template('admin.html', my_list3 = result2, show_element1 = True, show_element2 = False, big_element5=False, big_element4=False, big_element3=True, big_element2=False, big_element1=False)


@app.route('/update_dog_link', methods=['POST'])
def update_dog_link():
    global update_button
    update_button = request.form['update_button']
    cursor = mydb.cursor()
    cursor.execute(f"select * from pets where id = '{update_button}';")
    rs = cursor.fetchall()
    print(update_button, rs)
    name = rs[0][2]
    age = rs[0][3]
    breed = rs[0][4]
    gender = rs[0][5]
    sr = rs[0][6]
    price = rs[0][7]
    return render_template('admin.html', show_element1 = False, show_element2 = True, name=name, age=age,breed=breed,gender=gender,sr=sr,price=int(price),big_element5=False,big_element4=False, big_element3=True, big_element2=False, big_element1=False)


#----------------------------------------------------------------
#CAT DETAIL
#----------------------------------------------------------------

@app.route('/cat_data_page', methods=['GET'])
def cat_data_page():
    cursor = mydb.cursor()
    cursor.execute(f"select * from pets where type='cat';")
    result2 = cursor.fetchall()
    return render_template('admin.html', my_list3 = result2, show_element1 = True, show_element2 = False, big_element5=False,big_element4=True, big_element3=False, big_element2=False, big_element1=False)



@app.route('/update_cat_link', methods=['POST'])
def update_cat_link():
    global update_button
    update_button = request.form['update_button']
    cursor = mydb.cursor()
    cursor.execute(f"select * from pets where id = '{update_button}';")
    rs = cursor.fetchall()
    print(update_button, rs)
    name = rs[0][2]
    age = rs[0][3]
    breed = rs[0][4]
    gender = rs[0][5]
    sr = rs[0][6]
    price = rs[0][7]
    return render_template('admin.html', show_element1 = False, show_element2 = True, name=name, age=age,breed=breed,gender=gender,sr=sr,price=int(price), big_element5=False,big_element4=True, big_element3=False, big_element2=False, big_element1=False)



@app.route('/all_user_details', methods=['GET'])
def all_user_details():
    cursor = mydb.cursor()
    cursor.execute(f"SELECT c.id, c.name, c.email, COUNT(o.id) AS num_orders FROM customers c LEFT JOIN orders o ON c.id = o.c_id GROUP BY c.id, c.name, c.email;")
    result2 = cursor.fetchall()
    return render_template('admin.html', my_list4 = result2, show_element1=True,  big_element5=True,big_element4=False, big_element3=False, big_element2=False, big_element1=False)


@app.route('/view_customer_ord', methods=['POST'])
def view_customer_ord():
    view_button = request.form['view_button']
    cursor = mydb.cursor()
    cursor.execute(f"SELECT o.*, p.* FROM orders o JOIN pets p ON o.p_id = p.id WHERE o.c_id = {view_button};")
    rs = cursor.fetchall()
    cursor.execute(f"select name from customers where id = {view_button};")
    rs2 = cursor.fetchall()
    name = rs2[0][0]
    return render_template('admin.html', my_list5 = rs, name = name, show_element2 = True, big_element5=True,big_element4=False, big_element3=False, big_element2=False, big_element1=False)

@app.route('/admin_page_link', methods=['GET'])
def admin_page_link():
    return render_template('admin_login.html')
#Home Page

if __name__ == '__main__':
    app.run(debug=True)
