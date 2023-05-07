import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Aruna@1105",database="Inventory_Management")
cur=mydb.cursor()



//creating manufacture table
t='CREATE TABLE manufacture(manufacture_id INT PRIMARY KEY,product_name varchar(30) NOT NULL,color VARCHAR(30) NOT NULL,quantity INT NOT NULL,defective_quantity INT,manufacture_date DATE NOT NULL)'
cur.execute(t)
z='INSERT INTO manufacture (manufacture_id,product_name, color, quantity, manufacture_date) VALUES(%s,%s,%s,%s,%s)'
a=[(1,'Wooden Chair', 'Brown', 100, '2023-04-01'),(2,'Wooden Table', 'White', 50, '2023-02-02'),(3,'Red Toy Car', 'Red', 200, '2023-02-18'),(4,'Blue Toy Car', 'Blue', 150 , '2023-03-03'),(5,'Shirt', 'Blue', 300 , '2023-04-01')]
cur.executemany(z,a)
mydb.commit()
print('data inserted successfully')



//creating goods table
t='CREATE TABLE goods (goods_id INT PRIMARY KEY,product_name varchar(30) NOT NULL,color varchar(30) NOT NULL,quantity INT NOT NULL,manufacture_date DATE NOT NULL)'
cur.execute(t)
z='INSERT INTO goods (goods_id,product_name, color, quantity, manufacture_date) VALUES(%s,%s,%s,%s,%s)'
a=[(21,'Wooden Chair', 'Brown', 80, '2023-04-01'),(22,'Wooden Table', 'White', 40, '2023-02-02'),(23,'Red Toy Car', 'Red', 150, '2023-02-18'),(24,'Blue Toy Car', 'Blue', 100, '2023-03-03')]
cur.executemany(z,a)
mydb.commit()
print("inserted")



//creating purchase table
t='CREATE TABLE purchase (purchase_id INT PRIMARY KEY,store_name varchar(30) NOT NULL,product_name varchar(30) NOT NULL,color varchar(30) NOT NULL,quantity INT NOT NULL,purchase_date DATE NOT NULL)'
cur.execute(t)
z='INSERT INTO purchase (purchase_id,store_name, product_name, color, quantity, purchase_date)VALUES(%s,%s,%s,%s,%s,%s)'
a=[(31,'MyKids', 'Red Toy Car', 'Red', 50, '2023-02-20'),(32,'MyKids', 'Blue Toy Car', 'Blue', 30, '2023-03-05'),(33,'ORay', 'Shirt', 'Blue', 100, '2023-04-02'),(34,'MyCare', 'Wooden Table', 'Brown', 1, '2023-04-20')]
cur.executemany(z,a)
mydb.commit()
print("insert in purchase")






//creating sales table
t='CREATE TABLE sale (sale_id INT PRIMARY KEY,store_name varchar(30) NOT NULL,product_name varchar(30) NOT NULL,color varchar(30) NOT NULL,quantity INT NOT NULL,sale_date DATE NOT NULL,sale_price float NOT NULL,cost_price float NOT NULL,profit_margin float NOT NULL,company varchar(30) NOT NULL)'
cur.execute(t)
z='INSERT INTO sale (sale_id, store_name, product_name, color, quantity, sale_date, sale_price, cost_price, profit_margin,company)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
a=[(41,'MyCare', 'wooden_table', 'Red', 40, '2023-02-25',70,50,20,'SS Export'),(42,'ORay','Shirt','Red',150,'2023-05-17',90,50,40,'ABC Export')]
cur.executemany(z,a)
mydb.commit()
print("insert in sales")





f="SELECT *FROM goods WHERE product_name = 'Wooden Chair' AND manufacture_date < '2023-05-01'"
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)






x="UPDATE manufacture SET quantity = quantity - (SELECT SUM(quantity) FROM purchase WHERE color = 'Red' AND store_name = 'MyKids')WHERE color = 'Red'"
cur.execute(x)
mydb.commit()
print("commited successfully")





f="select profit_margin from sale where product_name='wooden_table' and store_name='MyCare' and company='SS Export'"
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)


x='delete from purchase where product_name="Shirt" and purchase_date="2023-04-02" and store_name="ORay"'
cur.execute(x)
mydb.commit()







