import mysql.connector
userid = None
username = None
pincode = None

def login():
    global userid, username, pincode
    if userid is None or username is None or pincode is None:
        userid = input("Enter userid: ")
        username = input("Enter username: ")
        pincode = input("Enter pincode: ")
    return userid, username, pincode

    
        
        
    


def displaycart():
    import mysql.connector

    con = mysql.connector.connect(host='localhost',
                                  user='root', password='root123',
                                  database='shopping_cart')

    cur = con.cursor()
    userid, username, pincode = login()
    
    print()
    query = "select user_id,username,itemname,price,discount,qty from items,user where user.itemnumber=items.itemnumber and user_id={};".format(
        userid)
    cur.execute(query)
    cart = cur.fetchall()

    print('user_id',' ','username','itemname' ,' ','price',' ','discount', '   ','qty')
    
    print()
    for i in cart:
        for j in i:
            print(j,end='\t')
        print()
    con.commit()
    con.close()
    cur.close()




def add():
    import mysql.connector
    

    con = mysql.connector.connect(host='localhost',
                                  user='root', password='root123',
                                  database='shopping_cart')

    cur = con.cursor()
    userid, username, pincode = login()

    

    
    print("---------------------------------------")
    print("1-itemA\n2-itemB\n3-itemC\n4-itemD\n5-itemE\n6-itemF\n7-itemG\n8-itemH")
    print("---------------------------------------")
    while True:

        sel_itemno = input("Enter the item numbers you want to add to cart ")
        qty=input("enter the quantity")
        
        query = "insert into user (user_id , username ,pincode,itemnumber,qty) values({},'{}','{}',{},{} );".format(userid,
                                                                                                            username,
                                                                                                            pincode,
                                                                                                            sel_itemno,
                                                                                                                qty)
        cur.execute(query)

        ch = input("input y to continue,n to stop: ")
        if ch == 'n' or ch == 'N':
            break
    con.commit()
    con.close()
    cur.close()
    
    displaycart()


def total_amount():
    import mysql.connector

    con = mysql.connector.connect(host='localhost',
                                  user='root', password='root123',
                                  database='shopping_cart')
    cur = con.cursor()
    count = 0
    userid, username, pincode = login()

    
    query = "select username,cast(SUM(Price - (Price * Discount / 100))*qty as signed) from items,user where items.itemnumber=user.itemnumber and user_id ={} group by username,qty ;".format(
        userid)

    cur.execute(query)
    r = cur.fetchall()
    
    for i in r:
        
        

    
      z=i[1]
      count=count+z
    print("your total amount is :",'$',count )
    
    con.commit()
    con.close()
    cur.close()
    return count



    
def update():
    import mysql.connector
    
    con = mysql.connector.connect(host='localhost',
                                  user='root', password='root123',
                                  database='shopping_cart')
    cur=con.cursor()
    userid, username, pincode = login()
    
    query = "select user_id,username,itemname,price,discount from items,user where user.itemnumber=items.itemnumber and user_id={};".format(
        userid)
    cur.execute(query)
    cart = cur.fetchall()
    
    print('the items your can select to update are \n')
    
    

    for i in cart:
        
        print(i[2])
        
    print()
    print("the cart before update")
    displaycart()
    print()
    print("---------------------------------------")
    print("1-itemA\n2-itemB\n3-itemC\n4-itemD\n5-itemE\n6-itemF\n7-itemG\n8-itemH")
    print("---------------------------------------")
    z = int(input("input the previous item number"))
    b = int(input("new itemnumber "))
    qtyy=input("enter the new  quantity")
    


    query = "update user set itemnumber= {} where itemnumber={}".format(b, z)
    q1="update user set qty= {} where itemnumber={}".format(qtyy, z)
    cur.execute(q1)

    cur.execute(query)

    con.commit()
    con.close()
    cur.close()
    print("the cart after update")
    print("\n")
    displaycart()
    print()


def delete():
    con = mysql.connector.connect(host='localhost',
                                  user='root', password='root123',
                                  database='shopping_cart')

    cur = con.cursor()
    
    userid, username, pincode = login()
    query = "select user_id,username,itemname,price,discount from items,user where user.itemnumber=items.itemnumber and user_id={};".format(
        userid)
    cur.execute(query)
    
    cart = cur.fetchall()
    print('the items your can select to delete are \n')

    for i in cart:
        
        print(i[2])

    print()
    print("the item numbers are")
    print("---------------------------------------")
    print("1-itemA\n2-itemB\n3-itemC\n4-itemD\n5-itemE\n6-itemF\n7-itemG\n8-itemH")
    print("---------------------------------------")
    z = int(input("input the item number of the item you want to delete"))
    print("the cart before deletion")
    displaycart()
    print()

    query = "delete from  user where itemnumber={};".format(z)

    cur.execute(query)

    con.commit()
    con.close()
    cur.close()
    print("after deletion")
    displaycart()
    print()
def payment():
    import mysql.connector

    con = mysql.connector.connect(host='localhost',
                                  user='root', password='root123',
                                  database='shopping_cart')

    cur = con.cursor()
    userid, username, pincode = login()
    print("payment options are google_pay,credit_card , debit _card")

    payment = input("the type of payment:")
    q=total_amount()
    pay=int(input("enter your amount to be owed"))
    print()
    if pay==q:
        
        print("Transation Successful")

    else:
        print("error invalid payment")
    

    query = "insert into payment (pay_type,user_id) values('{}',{});".format(payment, userid)
    z = cur.execute(query)
    
    con.commit()
    con.close()
    cur.close()


while True:
    print("---------------------------------------")
    chioce = input("0-login\n1- add to cart\n2- display cart\n3- show total price of items bought\n4-delete an item from cart\n5- update an item from cart\n6 to select payment method\n7 to exit\nenter your chioce")
    print("---------------------------------------")
    
    if chioce =="0":
        print()
        login()
        print()
    elif chioce == "1":

        add()

        print("\n")



    elif chioce == "2":
        print("your cart is:")
        displaycart()
        print("\n")

    elif chioce == "3":
        
        total_amount()
        print("\n")
    elif chioce == "4":

        delete()
    elif chioce == "5":
        update()
    elif chioce == "6":
        print("\n")
        payment()
        print("\n")
    elif chioce=="7":
        break