import pymysql 


try: 
    db=pymysql.connect(host="localhost",user="root",password="sms", database='theatre')
    print("Connected Successfully!!") 
except Exception as e: 
    print("Database connection error",e) 
cur=db.cursor() 
cur.execute("Show databases;") 
print(cur.fetchall()) 

 

def insert(): 
    ticketno=input("Ticket no: ") 
    name=input("Name: ") 
    mname=input("Movie Name: ") 
    seatno=input("Seat No: ") 
    dot=input("Date[YYYY-MM-DD]") 
    time=input("Time :") 
    sql = '''INSERT INTO MOVIE VALUES("{}","{}","{}","{}","{}","{}")'''.format(ticketno,name,mname,seatno,dot,time) 
    cur.execute(sql) 
    db.commit() 
    print(cur.rowcount, " record inserted.") 

 

def delete_ticket_no(): 
    n=int(input("Enter the ticket no to be deleted :")) 
    sql = "DELETE FROM movie WHERE ticket_no='%s'" % n 
    cur.execute(sql) 
    db.commit() 
    print(cur.rowcount, "record(s) deleted") 

 

def update(): 
    n=int(input("Enter the ticketno for which record is to updated :")) 
    name=input("Enter the name :") 
    se=input("Enter new seat :") 
    sql = "UPDATE movie SET seat_no='%s' WHERE ticket_no='%s' and name='%s'; " % (se,n,name) 
    cur.execute(sql) 
    db.commit() 

 

def display(): 
    numrow=cur.execute("SELECT * FROM movie") 
    print(cur.fetchall()) 



def search(): 
    t=int(input("Enter the ticketno")) 
    adr = (t) 
    sql="SELECT * FROM movie WHERE ticket_no = %s"%(t) 
    numrow=cur.execute(sql) 
    print(cur.fetchall()) 

 

def create_table(): 
    try: 
        tab=cur.execute("CREATE TABLE THEATRE(Ticket_no INT primary key, Name VARCHAR(20), MovieName VARCHAR (50),SEAT_no VARCHAR (4),Date DATE, TIME VARCHAR(6))") 
        print("Table created!!") 
    except: 
        print("Table exists") 
        cur.execute("Decs THEATRE") 
        X=cur.fetchall() 
        for i in cur: 
            print(i) 

 

c='y'     

while c=="y": 

    print("1. Insert\n2. Delete \n3. Update Seat no\n4. Display all\n5. Search a Records\n6. Create table") 
    choice=int(input("Enter your choice: ")) 

    if (choice==1): 
        insert() 

    elif (choice==2): 
        delete_ticket_no() 

    elif (choice==3): 
        update() 

    elif (choice==4): 
        display() 

    elif (choice==5): 
        search() 

    elif choice==6: 
        create_table() 

    else: 
        print("Wrong Input") 

    c=input("Do you want to continue or not? ") 