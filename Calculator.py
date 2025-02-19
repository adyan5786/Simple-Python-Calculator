# Calculator


# Modules
import math

import mysql.connector
from tabulate import tabulate

# Connection Part
password = ''
while True:
    try:
        mycon = mysql.connector.connect(host='localhost', user='root', password=password)
    except mysql.connector.errors.ProgrammingError:
        password = input("Enter correct password of mysql:")
        continue
    break

# Table Creation Part
cursor = mycon.cursor()
cursor.execute("create database if not exists calculator;")
cursor.execute('use calculator;')
table = 'create table if not exists history(' \
        'S_No int(100) primary key, ' \
        'Operation_Used varchar(100), ' \
        'Sub_Operation_Used varchar(100) default "-", ' \
        'Operations varchar(100), ' \
        'Result varchar(100), ' \
        'Date_and_Time datetime);'
cursor.execute(table)
cursor.execute("select S_No from history")
data = cursor.fetchall()
index = len(data)


# Intro Code
def intro():
    print("\t\t\t\t\t***********************")
    print("\t\t\t\t\t SCIENTIFIC CALCULATOR")
    print("\t\t\t\t\t***********************")
    print("\t\t\t\t\tPress Enter To Continue\n")
    input()


# Number Code (Not Part Of Main Program)
def num():
    while True:
        try:
            x = float(input("Enter a number:"))
        except ValueError:
            print("Invalid Input.\n")
            continue
        return x


# Degrees or Radians Conversion Code (Not Part Of Main Program)
def rd():
    while True:
        m = input("\nEnter values in Degrees or Radians? (1/2):")
        if m == '1':
            a = num() * (math.pi / 180)
            lrd = ["Deg", a]
            return lrd
        elif m == '2':
            a = num()
            lrd = ["Rad", a]
            return lrd
        else:
            print("Invalid Input.")


# Arithmetic Code
def arithmetic(i):
    print("*Note: Enter a number first and then any of these signs (+,-,*,/) for arithmetic "
          "operations and (=) for the result*")
    num1 = num()
    while True:
        ch1 = input("Enter sign:")
        if ch1 == "+":
            num2 = num()
            num1 += num2
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i, "\"Simple "
                     "Arithmetic Operation\"", "\"Addition\"", "\"" + str(num1 - num2) + ' + ' +
                     str(num2) + "\"", str(num1), 'now()')
            cursor.execute(insert)
        elif ch1 == "-":
            num2 = num()
            num1 -= num2
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i, "\"Simple "
                     "Arithmetic Operation\"", "\"Subtraction\"", "\"" + str(num1 + num2) + ' - ' +
                     str(num2) + "\"", str(num1), 'now()')
            cursor.execute(insert)
        elif ch1 == "*":
            num2 = num()
            num1 *= num2
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i, "\"Simple "   
                     "Arithmetic Operation\"", "\"Multiplication\"", "\"" + str(num1 / num2) +
                     ' * ' + str(num2) + "\"", str(num1), 'now()')
            cursor.execute(insert)
        elif ch1 == "/":
            num2 = num()
            while num2 == 0:
                print("Number cannot be divided by 0")
                num2 = num()
            num1 /= num2
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i, "\"Simple "
                     "Arithmetic Operation\"", "\"Division\"", "\"" + str(num1 * num2) + ' / ' +
                     str(num2) + "\"", str(num1), 'now()')
            cursor.execute(insert)
        elif ch1 == "=":
            print("The Result:", num1)
            return i
        else:
            print("Invalid Choice.\n")


# Roots Code
def root(i):
    print("*Note: Enter a number and then the power of the root*")
    a = num()
    b = num()
    while b == 0:
        print("Number cannot be 0\n")
        b = num()
    c = a ** (1 / b)
    i += 1
    insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i, "\"Root\"", "\"-\"",
             "\"" + str(a) + ' ** (1/' + str(b) + ")\"", str(c), 'now()')
    cursor.execute(insert)
    print("The Root is", c)
    return i


# Exponents Code
def exponents(i):
    print("*Note: Enter a number and then the power*")
    try:
        x = num()
        y = num()
        a = x ** y
        i += 1
        insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i, "\"Exponents\"",
                 "\"-\"", "\"" + str(x) + ' ** ' + str(y) + "\"", str(a), 'now()')
        cursor.execute(insert)
        print("The Result:", a)
    except OverflowError:
        print('Result too large')
    return i


# Log Code
def log(i):
    while True:
        print("Choose the option:")
        print("1. Natural Logarithm (ln)")
        print("2. Custom Base Logarithm (log)")
        ch3 = input("Select Your Option (1-2):")
        print()
        if ch3 == '1':
            print("*Note: Enter the number to get the Natural Log of*")
            a = num()
            while a < 1:
                print("Number cannot be negative or 0\n")
                a = num()
            e = math.e
            c = math.log(a, e)
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Logarithm\"", "\"Natural Logarithm (ln)\"", "\"log(" + str(e) + ') (' +
                     str(a) + ")\"", str(c), 'now()')
            cursor.execute(insert)
            print("The Result:", c)
            return i
        elif ch3 == '2':
            print("*Note: Enter the log base and then the number*")
            a = num()
            while a < 2:
                print("Base cannot be negative or 0 or 1\n")
                a = num()
            b = num()
            while b < 1:
                print("Number cannot be negative or 0\n ")
                b = num()
            c = math.log(b, a)
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Logarithm\"", "\"Custom Base Logarithm\"", "\"log(" + str(a) + ') (' +
                     str(b) + ")\"", str(c), 'now()')
            cursor.execute(insert)
            print("The Result:", c)
            return i
        else:
            print("Invalid Choice.\n")


# Factorial Code
def factorial(i):
    print("*Note: Enter the number to get the factorial of*")
    while True:
        try:
            b = int(input("Enter a number:"))
            if b < 0:
                print("Number can not be negative.\n")
            else:
                break
        except TypeError and ValueError:
            print("Number can only be an integer.\n")
    c = math.factorial(b)
    i += 1
    insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
             "\"Factorial\"", "\"-\"", "\"" + str(b) + "!\"", str(c), 'now()')
    cursor.execute(insert)
    print("The Result:", c)
    return i


# Trigonometry Code
def trigonometry(i):
    while True:
        print("Choose the Trigonometric Ratio:")
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Cosec")
        print("5. Sec")
        print("6. Cot")
        ch2 = input("Select Your Option (1-6):")
        if ch2 == '1':
            Lt = rd()
            a = math.sin(Lt[1])
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Trigonometry\"", "\"Sin (" + str(Lt[0]) + ")\"", "\"Sin(" + str(Lt[1]) +
                     ")\"", str(a), 'now()')
            cursor.execute(insert)
            print("The Result:", a)
            return i
        elif ch2 == '2':
            Lt = rd()
            a = math.cos(Lt[1])
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Trigonometry\"", "\"Cos (" + str(Lt[0]) + ")\"", "\"Cos(" + str(Lt[1]) +
                     ")\"", str(a), 'now()')
            cursor.execute(insert)
            print("The Result:", a)
            return i
        elif ch2 == '3':
            Lt = rd()
            a = math.tan(Lt[1])
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Trigonometry\"", "\"Tan (" + str(Lt[0]) + ")\"", "\"Tan(" + str(Lt[1]) +
                     ")\"", str(a), 'now()')
            cursor.execute(insert)
            print("The Result:", a)
            return i
        elif ch2 == '4':
            Lt = rd()
            while Lt[1] == 0:
                print("Number cannot be 0")
                Lt = rd()
            a = 1 / (math.sin(Lt[1]))
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Trigonometry\"", "\"Cosec (" + Lt[0] + ")\"", "\"Cosec(" + str(Lt[1]) +
                     ")\"", str(a), 'now()')
            cursor.execute(insert)
            print("The Result:", a)
            return i
        elif ch2 == '5':
            Lt = rd()
            a = 1 / (math.cos(Lt[1]))
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Trigonometry\"", "\"Sec (" + str(Lt[0]) + ")\"", "\"Sec(" + str(Lt[1]) +
                     ")\"", str(a), 'now()')
            cursor.execute(insert)
            print("The Result:", a)
            return i
        elif ch2 == '6':
            Lt = rd()
            while Lt[1] == 0:
                print("Number cannot be 0")
                Lt = rd()
            a = 1 / (math.tan(Lt[1]))
            i += 1
            insert = 'insert into history values({0},{1},{2},{3},{4},{5})'.format(i,
                     "\"Trigonometry\"", "\"Cot (" + str(Lt[0]) + ")\"", "\"Cot(" + str(Lt[1]) +
                     ")\"", str(a), 'now()')
            cursor.execute(insert)
            print("The Result:", a)
            return i
        else:
            print("Invalid Input.\n")


# History Table Code
def historytable(i):
    cursor.execute("Select * from history;")
    d = cursor.fetchall()
    h = ['S. No.', 'Operation Used', 'Sub Operation Used', 'Operations', 'Result', 'Date and Time']
    print("Showing", len(d), 'records:\n')
    print(tabulate(d, headers=h, tablefmt='psql'))
    while True:
        if len(d) == 0:
            i = 0
            return i
        else:
            a = input("\nClear history? (y/n):")
            if a == 'y':
                delete = 'delete from history where S_No>0'
                cursor.execute(delete)
                mycon.commit()
                i = 0
                print("History cleared.")
                return i
            elif a == 'n':
                return i
            else:
                print("Invalid Choice.")


# Start Of The Program
intro()
while True:
    print("\tMAIN MENU")
    print("\t1. Simple Arithmetic Operations")
    print("\t2. Exponents")
    print("\t3. Roots")
    print("\t4. Logarithm")
    print("\t5. Factorial")
    print("\t6. Trigonometry")
    print("\t7. History")
    print("\t8. Quit Program")
    ch = input("\tSelect Your Option (1-8):").strip()
    print('\n')
    if ch == '1':
        index = arithmetic(index)
    elif ch == '2':
        index = exponents(index)
    elif ch == '3':
        index = root(index)
    elif ch == '4':
        index = log(index)
    elif ch == '5':
        index = factorial(index)
    elif ch == '6':
        index = trigonometry(index)
    elif ch == '7':
        index = historytable(index)
    elif ch == '8':
        mycon.close()
        break
    else:
        print("Invalid Choice.")
    mycon.commit()
    ch = input("\nPress Enter To Go Back To Main Menu\n")
