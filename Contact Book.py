import sqlite3
import smtplib, ssl
import os


def add_mail():
    conn = sqlite3.connect("Mail_List.db")
    cursor = conn.cursor()
    name = input("Enter name: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO EMAIL VALUES (?,?);", (name, email))
    conn.commit()
    print("Email Added Successfully")


def rem_mail():
    conn = sqlite3.connect("Mail_List.db")
    cursor = conn.cursor()
    name = input("Enter name: ")
    email = input("Enter email: ")
    cursor.execute("DELETE FROM EMAIL WHERE NAME=? AND EMAIL=?;",(name,email))
    print("Email removed Successfully")
    conn.commit()

def send_message():
    subject = input("Enter the subject: ")
    message = input("Enter the message: ")
    smtp_server = "smtp.sankarsubramanian.online"
    port = 587
    my_email = "mail@sankarsubramanian.online"
    password = ""
    server = smtplib.SMTP(smtp_server,port)
    server.login(my_email, password)
    conn = sqlite3.connect("Mail_List.db")
    cursor = conn.cursor()
    list = cursor.execute('''SELECT * FROM EMAIL''')
    
    for i in list:
        content = "From: Sankar Subramanian <mail@sankarsubramanian.online> \nTo: "+ i[0] + " <" + i[1] + "> \nSubject: " + subject + "\n" + message 
        
        server.sendmail(my_email, i[1], content)
    print("Successfully Sent")
    server.quit()

def list_email():
    conn = sqlite3.connect("Mail_List.db")
    cursor = conn.cursor()
    list = cursor.execute('''SELECT * FROM EMAIL''')
    for i in list:
        print("\n------------------------------------------\n")
        print("Name: "+ i[0] + "\nEmail: " + i[1])
        
    t = input("\n\nPress any key to continue...")
    

while(True):
    os.system('cls')
    print("----BULK MAILER----")
    print("\n1.Add Email\n2.Remove Email\n3.List Email\n4.Send Message\n5.Exit\n")
    c = int(input("Enter your choice: "))
    if c==1:
        add_mail()
    elif c==2:
        rem_mail()
    elif c==3:
        list_email()
    elif c==4:
        send_message()
    elif c==5:
        exit()
    else: print("Worng Choice!")






    
