from pickle import TRUE
from traceback import print_exception
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="xxxxxxxx",
  database="restaurant")
mycursor = mydb.cursor()
mycursor.execute('''CREATE TABLE bill (Item_name varchar(50) primary key,Price_per_item integer,no_of_items integer
,total_price integer)''')



vegstarter=[["Panner Tikka",110],["Veg Seekh Kebab",110],["Hara Bhara Kebab",110],["Shanghai Spring Roll",140],["American Corn Ball",150]]
nonvegstarter=[["Chicken Tikka",170],["Murg Reshmi Kebab",180],["Murg Chilli Kebab",170],["Chicken Seekh Kebab",180],["Tangdi Kebab",160]]
maincourse=[["Shahi Panner",210],["Stuffed Kulcha",250],["Mughlai Chicken",240],["Fish Sarsowala",220],["Kadahi Vegetable",210]]
dessert1=[["Chocolate Walnut Brownie",110],["Marble Cake",150],["Mocha Magic",140],["Pineapple Shake",120],["Softy Pineapple",120]]
price=0
def additem():
    print('''Enter which one section do you want to add item
                  1) Starter
                  2) Main
                  3) Dessert''')
    a=int(input())
    if a==1:
        lis=[]
        d=int(input("Is it Veg(press1) or Nonveg(press2)"))
        item=input("Enter item name:-")
        pri=int(input("Enter item's price:-"))
        if d==1:
            lis.append(item)
            lis.append(pri)
            vegstarter.append(lis)
            print("Item added succesfully")
        elif d==2:
            lis.append(item)
            lis.append(pri)
            nonvegstarter.append(lis)
            print("Item added successfully")
        else:
            print("Choose between 1 or 2")
            return
    elif a==2:
        lis=[]
        item=input("Enter item name:-")
        prt=int(input("Enter item's price:-"))
        lis.append(item)
        lis.append(pri)
        maincourse.append(lis)
        print("Item added successfully")
    elif a==3:
        lis=[]
        item=input("Enter item name:-")
        prt=int(input("Enter item's price:-"))
        lis.append(item)
        lis.append(pri)
        dessert.append(lis)
        print("Item added successfully")
    else:
        print("Choose from 1 to 5")
        return
            
        
def menu():
    print("\t#######-------WELCOME------########")
    print("\t1)Starter (press1)")
    print("\t2)Main (press 2)")
    print("\t3)Dessert (press3)")
    print("\t4)Add item (press4)")
    print("\tIf you go for bill (enter 5) ")
    a=int(input("Enter the choice as above given menu:-"))
    if a==1:
        starter()
    elif a==2:
        main()
    elif a==3:
        dessert()
    elif a==4:
        additem()
    elif a==5:
        bill()
    else:
        print("Enter the values from 1 to 3 ")            

def starter():
    print("-------------------------------------------")
    print("---------Welcome to Starter Menu------------")
    print()
    global price
    while True:
        print("---------------------------------------")
        print("Enter VS for veg starter")
        print("Enter NVS for non veg starter")
        print("Enter M for menu")
        print("Enter Q for quit (for quit and go to bill section")
        print()
        l=input("Enter choice:-")
        print()
        if l=="vs" or l=="VS":
            print("------------VEG STARTER(Srno,Item Name,Price(in Rs.))---------------")
            for i in range(len(vegstarter)):
                print((i+1),vegstarter[i][0],vegstarter[i][1])
                print()
            x=int(input("Choose your starter from above list:-"))
            y=int(input("Enter the total no of starters do you want:-"))
            price=price+y*vegstarter[x-1][1]
            print("Item successfull added")
            sql = "INSERT INTO bill (Item_name, Price_per_item,no_of_items,total_price) VALUES (%s, %s,%s,%s)"
            val = (vegstarter[x-1][0],vegstarter[x-1][1],y,y*vegstarter[x-1][1] )
            mycursor.execute(sql, val)
            mydb.commit()
                
            
        elif l=="nvs" or l=="NVS":
            print("-------NON-VEG STARTER(Srno,Item Name,Price(in Rs.))---------")
            for i in range(len(nonvegstarter)):
                print((i+1),nonvegstarter[i][0],nonvegstarter[i][1])
                print()
            x=int(input("Choose your starter from above list:-"))
            y=int(input("Enter the total no of starters do you want:-"))
            price=price+y*nonvegstarter[x-1][1]
            print("Item successfull added")
            sql = "INSERT INTO bill (Item_name,Price_per_item,no_of_items,total_price) VALUES (%s, %s,%s,%s)"
            val = (nonvegstarter[x-1][0],nonvegstarter[x-1][1],y,y*nonvegstarter[x-1][1] )
            mycursor.execute(sql, val)
            mydb.commit()

        
        elif l=="M"or l=="m":
            menu()
        elif l=="Q" or l=="q":
            bill()
            break
           
            
def main():
    global price
    print("-------------------------------------------")
    print("Welcome to Main")
    print()
    while True:
        print("Enter MA for main")
        print("Enter M for menu")
        print("Enter Q for quit (for quit and go to bill section):-")
        print()
        l=input("Enter choice:-")
        print()
        if l=="MA" or l=="ma":
            print("--------MAIN COURSE(Srno,Item Name,Price(in Rs.)-------")
            for i in range(len(maincourse)):
                print((i+1),maincourse[i][0],maincourse[i][1])
                print()
            x=int(input("Choose your starter from above list:-"))
            y=int(input("Enter the total no of starters do you want:-"))
            price=price+y*maincourse[x-1][1]
            print("Item successfull added")
            sql = "INSERT INTO bill (Item_name,Price_per_item,no_of_items,total_price) VALUES (%s, %s,%s,%s)"
            val = (maincourse[x-1][0],maincourse[x-1][1],y,y*maincourse[x-1][1] )
            mycursor.execute(sql, val)
            mydb.commit()
        elif l=="m" or l=="M":
            menu()
        elif l=="q" or l=="Q":
            bill()
            break



def dessert():
    global price
    print("-------------------------------------------")
    print("Welcome To Dessert Section")
    print()
    while True:
        print("Enter DE for main:-")
        print("Enter M for menu:-")
        print("Enter Q for quit (for quit and go to bill section):-")
        print()
        l=input("Enter choice:-")
        if l=="DE" or l=="de":
            print("-------DESSERT(Srno,Item Name,Price(in Rs.)---------")
            for i in range(len(dessert1)):
                print((i+1),dessert1[i][0],dessert1[i][1])
                print()
            x=int(input("Choose your starter from above list:-"))
            y=int(input("Enter the total no of starters do you want:-"))
            price=price+y*dessert1[x-1][1]
            print("Item successfull added")
            sql = "INSERT INTO bill (Item_name, Price_per_item,no_of_items,total_price) VALUES (%s, %s,%s,%s)"
            val = (dessert1[x-1][0],dessert1[x-1][1],y,y*dessert1[x-1][1] )
            mycursor.execute(sql, val)
            mydb.commit()
        elif l=="M" or l=="m":
            menu()
        elif l=="q" or l=="Q":
            bill()
            break
            
        


def bill():
    if price!=0:
        print("--------------------------")
        sql_select_Query = "select * from bill"
        mycursor.execute(sql_select_Query)
        records = mycursor.fetchall()
        print("Here is the bill:-")
        print("Item_name     price_per_item    no_of_items    total_price")
        for i in records:
            print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
        sql = "DROP TABLE bill"
        mycursor.execute(sql)
        print("The final price:",price)
        print("Thanks for buying")
    else:
        print("You didn't buy anything")
menu()

