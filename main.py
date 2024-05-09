import mysql.connector as con
import matplotlib.pyplot as ez

def printAll():
    st1001 = "select * from grocery_store"
    cur.execute(st1001)
    data = cur.fetchall()
    for z in data:
        print(z)
    print("Enter 0 to return to main menu")
    print("Enter 1 to end the program")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1

def addItem():
    st434 = 'insert into grocery_store values(%s,%s,%s,%s,%s,%s,%s)'
    productid = int(input("Enter the product id: "))
    product_name = input("Enter the product name: ")
    product_brand = input("Enter the product brand: ")
    product_stock = int(input("Enter the product stock: "))
    product_price = int(input("Enter the product price: "))
    manufacture_date = input("Enter the manufacture date of the product in YYYY-MM-DD format: ")
    expiry_date = input("Enter the expiry date of the product in YYYY-MM-DD format: ")
    val434 = (productid, product_name, product_brand, product_stock, product_price, manufacture_date, expiry_date)
    cur.execute(st434, val434)
    mycon.commit()
    print("The product has been successfully added to the database")
    print("Enter 0 to return to main menu") 
    print("Enter 1 to end the program")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1

def removeItem():
    st102 = 'delete from grocery_store where productid=%s'
    productid = input("Enter the product's id you want to remove: ")
    val102 = (productid,)
    cur.execute(st102, val102)
    mycon.commit()
    print("The product has been removed from the database")
    print("Enter 0 to return to main menu")
    print("Enter 1 to end the program")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1

def changePrice():
    st103 = 'update grocery_store set product_price=%s where productid=%s'
    product_id = int(input("Enter the ID of product you want to update: "))
    product_price = int(input("Enter the new price of the product: "))
    val103 = (product_price, product_id)
    cur.execute(st103, val103)
    mycon.commit()
    print("Price of the product has been successfully updated to:", product_price)
    print("Enter 0 to return to main menu")
    print("Enter 1 to end the program")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1

def changeName():
    st103 = 'update grocery_store set product_name=%s where productid=%s'
    product_id = int(input("Enter the ID of product you want to update: "))
    product_name = input("Enter the new name of the product: ")
    val103 = (product_name, product_id)
    cur.execute(st103, val103)
    mycon.commit()
    print("Name of product has been successfully updated to:", product_name)
    print("Enter 0 to return to main menu")
    print("Enter 1 to end the program")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1

def changeBrand():
    st103 = 'update grocery_store set product_brand=%s where productid=%s'
    product_id = int(input("Enter the ID of product you want to update: "))
    product_brand = input("Enter the new brand of the product: ")
    val103 = (product_brand, product_id)
    cur.execute(st103, val103)
    mycon.commit()
    print("Brand name of the product has been successfully updated to:", product_brand)
    print("Enter 0 to return to main menu")
    print("Enter 1 to end the program")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1

def checkExpiredItems():
    today = input("Enter today's date in YYYY-MM-DD format: ")
    cur.execute('select * from grocery_store where expiry_date<%s', (today,))
    data = cur.fetchall()
    for i in data:
        print(i)
    print("Enter 0 to return to main menu")
    print("Enter 1 to end the program")
    print("Enter 2 to delete expired items from database")
    internal_choice = int(input(""))
    if internal_choice == 0:
        e = 0
    elif internal_choice == 1:
        e = 1
    elif internal_choice == 2:
        for i in data:
            stz = 'delete from grocery_store where productid=%s'
            valz = (i[0],)
            cur.execute(stz, valz)
            print(i[1], '- Has been successfully removed from the database')

mycon = con.connect(host='sql6.freesqldatabase.com', user='sql6705087', passwd='CK8iVNPmCR', database='sql6705087')

if mycon.is_connected():
    print("successfully connected to the database.")
    cur = mycon.cursor()
    k = 0
    while k < 1:
        print("------------------------WELCOME TO GROCERY MANAGEMENT SYSTEM------------------------")
        print("\nPRODUCT DATABASE COMMANDS :-\n")
        print("Enter 1 to print details of all products from the database")
        print("Enter 2 to add a product to the database")
        print("Enter 3 to remove a product from the database")
        print("Enter 4 to change the price of a product")
        print("Enter 5 to change the name of a product")
        print("Enter 6 to change the brand of a product")
        print("Enter 7 to check for expired items")
        print("\nEMPLOYEE DATABASE COMMANDS :-\n")
        print("Enter 8 to print name of all employees from the database")
        print("Enter 9 to add an employee to the database")
        print("Enter 10 to remove an employee from the database")
        print("Enter 11 to change salary of an employee")
        print("Enter 12 to change the name of an employee")
        print("Enter 13 to change the department of an employee")
        print("\nDAILY EARNING COMMANDS :-\n")
        print("Enter 14 to add a sold item to the database")
        print("Enter 15 to view store's earning graph\n")
        print("Enter 16 to end the program")
        print("-----------------------------------------------------------------------------------")
        
        choice = int(input("\nEnter your choice - "))
        
        if choice == 1:
            printAll()
        
        elif choice == 2:
            addItem()
        
        elif choice == 3:
            removeItem()
        
        elif choice == 4:
            changePrice()
        
        
        elif choice == 5:
            changeName()
        
        elif choice == 6:
            changeBrand()
        
        elif choice == 7:
            checkExpiredItems()
        
        elif choice == 8:
            st1001 = "select * from employee"
            cur.execute(st1001)
            data = cur.fetchall()
            for z in data:
                print(z)
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 9:
            st434 = 'insert into employee values(%s,%s,%s,%s,%s,%s)'
            eid = int(input("Enter the employee id: "))
            ename = input("Enter the employee name: ")
            dept = input("Enter the employee department: ")
            age = int(input("Enter the employee age: "))
            salary = int(input("Enter the employee salary: "))
            doj = input("Enter the doj of employee in YYYY-MM-DD format: ")
            val434 = (eid, ename, dept, age, salary, doj)
            cur.execute(st434, val434)
            mycon.commit()
            print("The employee has been successfully added to the database")
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 10:
            st102 = 'delete from employee where eid=%s'
            eid = input("Enter the employee's id you want to remove: ")
            val102 = (eid,)
            cur.execute(st102, val102)
            mycon.commit()
            print("The employee has been successfully removed from the database")
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 11:
            eid = int(input("Enter the employee id: "))
            salary = int(input("Enter the new salary of the employee: "))
            cur.execute('update employee set salary=%s where eid=%s', (salary, eid))
            mycon.commit()
            print("The salary of the employee has been successfully updated to:", salary)
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 12:
            eid = int(input("Enter the employee id: "))
            ename = input("Enter the new name of the employee: ")
            cur.execute('update employee set ename=%s where eid=%s', (ename, eid))
            mycon.commit()
            print("The name of the employee has been successfully updated to:", ename)
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 13:
            eid = int(input("Enter the employee id: "))
            dept = input("Enter the new department of the employee: ")
            cur.execute('update employee set dept=%s where eid=%s', (dept, eid))
            mycon.commit()
            print("The department of the employee has been successfully updated to:", dept)
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 14:
            productid = int(input("Enter the product id: "))
            product_name = input("Enter the name of the product: ")
            product_price = int(input("Enter the price of the product: "))
            items_sold = int(input("Enter the no. of products sold: "))
            week_day = input("Enter the week day item was sold on: ")
            total_earned = product_price * items_sold
            cur.execute('insert into earnings values(%s,%s,%s,%s,%s,%s)',
                        (productid, product_name, product_price, items_sold, week_day, total_earned))
            mycon.commit()
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 0
            elif internal_choice == 1:
                e = 1
        
        elif choice == 15:
            cur.execute('select * from earnings;')
            data = cur.fetchall()
            total_earned = []
            week_day = []
            for i in data:
                total_earned.append(i[5])
                week_day.append(i[4].upper())
            ez.bar(week_day, total_earned)
            ez.ylim(0, 1000)
            ez.xlabel("WEEK DAY")
            ez.ylabel("TOTAL EARNED")
            ez.title("TOTAL MONEY EARNED PER DAY")
            ez.show()
            print("Enter 0 to return to main menu")
            print("Enter 1 to end the program")
            internal_choice = int(input(""))
            if internal_choice == 0:
                e = 1
            elif internal_choice == 1:
                e = 0
        
        elif choice == 16:
            break
        
        else:
            print("Invalid choice")
            break
            
        if e == 0:
            k = 0
        elif e == 1:
            break
            
    print("---------------------------------PROGRAM ENDED---------------------------------")
    print("-----------------------------------THANK YOU-----------------------------------")
