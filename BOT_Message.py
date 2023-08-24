import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.options import Options
import datetime
import re #regex
from tkinter import *
import tkinter as tk
from functools import partial
import tkinter.font as tkFont
import mysql.connector
from mysql.connector import Error
import pandas as pd

def validateLogin(database, password):
     
     global Database
     global Password
     Database = database.get()
     Password = password.get()
     print(Database, Password)
     options = webdriver.ChromeOptions()
     options.add_argument(r"user-data-dir=D:\User Data")
     options.add_argument('--no-sandbox')
     #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
     driver = webdriver.Chrome(executable_path=r'C:\Users\LoL\.wdm\drivers\chromedriver\win32\89.0.4389.23\chromedriver.exe', options=options)
     driver.get('https://web.whatsapp.com')
     
     def create_server_connection(host_name, user_name, user_password):
         connection = None
         try:
             connection = mysql.connector.connect(
                 host=host_name,
                 user=user_name,
                 passwd=user_password
             )
             print("MySQL Database connection successful")
         except Error as err:
             print(f"Error: '{err}'")

         return connection


     pw = Password
     connection = create_server_connection("localhost", "root", pw)


     def create_database(connection, query):
         cursor = connection.cursor()
         try:
             cursor.execute(query)
             print("Database created successfully")
         except Error as err:
             print(f"Error: '{err}'")
             
     create_database_query = "CREATE DATABASE "+Database
     create_database(connection, create_database_query)


     def create_db_connection(host_name, user_name, user_password, db_name):
         connection = None
         try:
             connection = mysql.connector.connect(
                 host=host_name,
                 user=user_name,
                 passwd=user_password,
                 database=db_name
             )
             print("MySQL Database connection successful")
         except Error as err:
             print(f"Error: '{err}'")

         return connection


     def execute_query(connection, query):
         cursor = connection.cursor()
         try:
             cursor.execute(query)
             connection.commit()
             print("Query successful")
         except Error as err:
             print(f"Error: '{err}'")




     create_record_table  = """
     CREATE TABLE record (
       Sender VARCHAR(40) NOT NULL,
       Date DATE NOT NULL,
       SentMSG VARCHAR(40),
       Time TIME NOT NULL
       );
       """


     db = Database
     connection = create_db_connection("localhost", "root", pw, db) # Connect to the Database
     execute_query(connection, create_record_table)
     N = 0




          
     time.sleep(6)
     print("HAJIME")
     wait = WebDriverWait(driver, 0)
     def chat_lokate(name, ii):
          Name ='"'+name+'"' #input("Enter the name of the receiptent: ")
          ii = ii
          try:
               find_chat = '//*[@id="pane-side"]/div[1]/div/div/div['+ii+']/div/div/div[2]/div[1]/div[1]/span/span[@title='+Name+']'
               Group_title = wait.until(EC.element_to_be_clickable(( 
               By.XPATH, find_chat))) 
               Group_title.click()
          except:
               gg = 'gg'
               
          else:
               Find_chat = '//*[@id="pane-side"]/div[1]/div/div/div['+ii+']/div/div/div[2]/div[1]/div[1]/span/span[@title='+Name+']'
               INT = str(i)
          try:
               Find_chat = '//*[@id="pane-side"]/div[1]/div/div/div['+ii+']/div/div/div[2]/div[1]/div[1]/span[@title='+Name+']' 
               group_title = wait.until(EC.element_to_be_clickable(( 
               By.XPATH, Find_chat))) 
               group_title.click()
          except:
                gg = 'gg'
          else:
               Find_chat = '//*[@id="pane-side"]/div[1]/div/div/div['+ii+']/div/div/div[2]/div[1]/div[1]/span[@title='+Name+']'
               INT = str(i)
          
          
          Find_chat = '//*[@id="pane-side"]/div[1]/div/div/div['+INT+']/div/div/div[2]/div[1]/div[1]/span[@title='+Name+']'
          
          return Find_chat

     def message_detect():
          for i in range(0, 40):
               ii = str(i)
               try:
                    
                    msg_detect = '//*[@id="pane-side"]/div[1]/div/div/div['+ii+']/div/div/div[2]/div[2]/div[2]/span[1]/div/span'
                    find_element = driver.find_element( 
                    By.XPATH, msg_detect)

               except:

                    iiii = str(0)
                    continue

               else:

                    iiii = ii
                    break
          iiii = str(iiii)
          return iiii
               


     def msg_send(iiii):
          
          
          chat = '//*[@id="pane-side"]/div[1]/div/div/div['+iiii+']/div/div/div[2]/div[1]/div[1]/span/span'
          try:
               Find_chat = chat
               Group_title = wait.until(EC.element_to_be_clickable(( 
               By.XPATH, Find_chat))) 
               Group_title.click()
          except:
               gg = 'gg'
          
          else:
               #print ("Minute : ", end = "")  
               #print (current_time.minute)
               
               
               time.sleep(2)
               
               
               for D in range(0, 600):
                    DD = str(D)
                    try:
                                    
                                        
                         chat1 = '//*[@id="main"]/div[3]/div/div/div[3]/div['+DD+']/div/div/div/div[2]/div/span'
                         
                         elements = driver.find_element_by_xpath(chat1).text
                    except:
                         gg = 'gg'
                         
                    else:
                         chat1 = '//*[@id="main"]/div[3]/div/div/div[3]/div['+DD+']/div/div/div/div[2]/div/span'
                         chat2 = '//*[@id="main"]/div[3]/div/div/div[3]/div['+DD+']/div/div/div/div[1]/div/span[1]/span'
                         elements = driver.find_element_by_xpath(chat1).text
                         
                         
               
               
               elements = driver.find_element_by_xpath(chat2).text
               
               passcode_re = re.compile(r'RishiRocks')
               try:
                    passcode = passcode_re.search(elements)
                    passcode_exist = passcode.group()
               except:
                    chat_box = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
                    chat_box_ = wait.until(EC.element_to_be_clickable(( 
                                   By.XPATH, chat_box)))
                    chat_box_.click()
                    Action = ActionChains(driver)
                    chat_box_.send_keys("Konichiwa, watashi Rishi's bot des and Rishi is not available rn")
                    chat_box_.send_keys(Keys.ENTER + Keys.SHIFT)
                    chat_box_.send_keys("Hope you Understand!!! (^^)")
                    chat_box_.send_keys(Keys.ENTER)
                    time.sleep(2)
                    driver.refresh()
               else:
                    chat_box = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
                    chat_box_ = wait.until(EC.element_to_be_clickable(( 
                                   By.XPATH, chat_box)))
                    chat_box_.click()
                    Action = ActionChains(driver)
                    x = datetime.datetime.now()
                    T = str(x.strftime("%I:%M:%S.%f %p"))
                    chat_box_.send_keys("*Rishi's last recorded message* _Hello currently I am busy in on some shady activities happening in Shibuya, Tokyo. So I won't be able to respond to any of the messages you send._ *YOUR REPLY TO THIS MESSAGE WILL BE RELAYED TO RISHI THROUGH HIDDEN MEANS* T-120 seconds for recording initiated at ", T)
                    chat_box_.send_keys(Keys.ENTER)
                    time.sleep(10)
                    for D in range(0, 100):
                         DD = str(D)               
                         try:
                              chat1 = '//*[@id="main"]/div[3]/div/div/div[3]/div['+DD+']/div/div/div/div[2]/div/span'
                              elements = driver.find_element_by_xpath(chat1).text
                         except:
                              gg = 'gg'
                         else:
                              chat1 = '//*[@id="main"]/div[3]/div/div/div[3]/div['+DD+']/div/div/div/div[2]/div/span'
                              chat2 = '//*[@id="main"]/div[3]/div/div/div[3]/div['+DD+']/div/div/div/div[1]/div/span[1]/span'
                              elements = driver.find_element_by_xpath(chat1).text
                    recorded_message = driver.find_element_by_xpath(chat2).text
                    recorded_message = "'"+recorded_message+"'"
                    chat_box_.send_keys("Thanks, Your msg has been recorded and will be delivered now (^^)")
                    
                    chat_box_.send_keys(Keys.ENTER)
                    try:
                    
                         sent_by = '//*[@id="main"]/header/div[2]/div/div/span' 
                         Sender = driver.find_element_by_xpath(sent_by).text
                    except:
                         gg = 'gg'
                    else:
                         sent_by = '//*[@id="main"]/header/div[2]/div/div/span' 
                         sender = driver.find_element_by_xpath(sent_by).text
                         sender  = "'"+sender+"'"
                    date = str(x.strftime("'"+"%Y-%m-%d"+"'"))
                    TTime = str(x.strftime("'"+"%I:%M:%S"+"'"))
                    
                    
                    pop_MessageRecord = "INSERT INTO record VALUES("+sender+", "+date+",   "+recorded_message+", "+TTime+");" 
                    execute_query(connection, pop_MessageRecord)
                    
                    
                    time.sleep(2)
                    driver.refresh()


     while True:
          message_alert = message_detect()
          msg_send(message_alert)
     return




#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Proxy Message Bot')

#database label and text entry box
databaseLabel = Label(tkWindow)

databaseLabel["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
databaseLabel["font"] = ft
databaseLabel["fg"] = "#ffffff"
databaseLabel["justify"] = "center"
databaseLabel["text"] = "Database_Name"
databaseLabel.place(x=0,y=10,height=20)#.grid(row=7, column=0)


database = StringVar()
databaseEntry = Entry(tkWindow, textvariable=database)
databaseEntry["bg"] = "#636060"
databaseEntry["fg"] = "#ffffff"
databaseEntry.place(x=130,y=10,height=20)

#password label and password entry box
passwordLabel = Label(tkWindow)

passwordLabel["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
passwordLabel["font"] = ft
passwordLabel["fg"] = "#ffffff"
passwordLabel["justify"] = "center"
passwordLabel["text"] = "Database_Password"
passwordLabel.place(x=0,y=60,height=20)#.grid(row=7, column=0)

password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*')
passwordEntry["bg"] = "#636060"
passwordEntry["fg"] = "#ffffff"
passwordEntry.place(x=130,y=60)  
validateLogin = partial(validateLogin, database, password)

#Start button
StartButton = Button(tkWindow, text="Start")
StartButton["activebackground"] = "#000000"
StartButton["activeforeground"] = "#ffffff"
StartButton["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
StartButton["font"] = ft
StartButton["fg"] = "#ffffff"
StartButton["justify"] = "center"
StartButton["command"] = validateLogin
StartButton.place(x=230, y=100)
tkWindow['bg'] = '#414141'
tkWindow.iconbitmap(r"F:\python\Alien monster emoji.ico")
tkWindow.mainloop()

    
    


















          
