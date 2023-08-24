import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.chrome.options import Options
import datetime
import re
import os
import pyautogui
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from functools import partial

def validateLogin(filename, fileLocation, twitterpage, letterbody, subject, recepients, catchphrase):
     
     global Filename
     global FileLocation
     global Twitterpage
     global Letterbody
     global Subject
     global Recepients
     global Catchphrase
     Filename = filename.get()
     FileLocation = fileLocation.get()
     Twitterpage = twitterpage.get()
     Letterbody = letterbody.get()
     Subject = subject.get()
     Recepients = recepients.get()
     Catchphrase = catchphrase.get()
     print(Filename, r'%s' %FileLocation, Twitterpage, Letterbody, Subject, Recepients, Catchphrase)




     options = webdriver.ChromeOptions()
     options.add_argument(r"user-data-dir=D:\User Data")
     options.add_argument('--no-sandbox')
     #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
     driver = webdriver.Chrome(executable_path=r'C:\Users\LoL\.wdm\drivers\chromedriver\win32\87.0.4280.88\chromedriver.exe', options=options)


     driver.maximize_window()
     print('Hajime')
     wait = WebDriverWait(driver, 0)



     def mail_initiate():
          driver.get('https://mail.google.com/mail/u/0/#inbox')
          time.sleep(15)
          try:
               
               
               compose_xpath = '//*[@id=":lr"]/div/div'#'//*[@id=":lq"]/div/div'
               compose_button = wait.until(EC.element_to_be_clickable(( 
                                             By.XPATH, compose_xpath)))
          except:
               compose_xpath = '//*[@id=":lq"]/div/div'#'//*[@id=":lq"]/div/div'
               compose_button = wait.until(EC.element_to_be_clickable(( 
                                             By.XPATH, compose_xpath)))
          else:
               compose_xpath = '//*[@id=":lr"]/div/div'#'//*[@id=":lq"]/div/div'
               compose_button = wait.until(EC.element_to_be_clickable(( 
                                             By.XPATH, compose_xpath)))
          compose_button.click()
          time.sleep(2)
          To_xpath = '//*[@id=":ra"]'
          To_button = wait.until(EC.element_to_be_clickable((
               By.XPATH, To_xpath)))
          
          
          To_button.send_keys (Recepients)
          To_button.send_keys(Keys.ENTER)
          subject_xpath= '//*[@id=":qs"]'
          subject_button = wait.until(EC.element_to_be_clickable((
               By.XPATH, subject_xpath)))
          subject_button.send_keys (Subject)#Subject
          time.sleep(1)
          body_xpath = '//*[@id=":rx"]'
          body_button = wait.until(EC.element_to_be_clickable((
               By.XPATH, body_xpath)))
          body_button.send_keys(Letterbody)#what you wanna write in the body
          attach_xpath = '//*[@id=":sa"]'
          attach_button = wait.until(EC.element_to_be_clickable((
               By.XPATH, attach_xpath)))
          attach_button.click()
          time.sleep(5)
          pyautogui.click(x=655, y=48)
          
          FileLocation1 = r'%s' %FileLocation
          time.sleep(1)
          pyautogui.write(FileLocation1)#file location
          time.sleep(3)
          pyautogui.write(["enter"])
          
          pyautogui.click(285, 478)
          time.sleep(1)
          pyautogui.write(Filename)#filename
          pyautogui.write(["enter"])
          time.sleep(100)
          send_xpath = '//*[@id=":qi"]'
          send_button = wait.until(EC.element_to_be_clickable((
               By.XPATH, send_xpath)))
          send_button.click()
          
          time.sleep(15)
          
          driver.quit()
          #os.system("shutdown /s /t 1") #system shutdown command
          



     def get_time():
          driver.get(Twitterpage)
          time.sleep(6)
          time_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a/time'
          Time= driver.find_element(
               By.XPATH, time_xpath).text
          return Time











     def tweet_detect():
          driver.get(Twitterpage)
          time.sleep(6)
          try:
               
               tweet_exist = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span'
               find_element = driver.find_element( 
               By.XPATH, tweet_exist)
               time.sleep(2)
               driver.refresh()
               time.sleep(4)
          except:
               gg = 'gg'
               print('failed')
          else:
               #tweet_written = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[4]/div/div/section/div/div/div[1]/div/div/article/div'
               
               tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span'
               tweet = driver.find_element( 
               By.XPATH, tweet_xpath).text
               alert_message = re.compile(Catchphrase)
               old_tweet_checker = re.compile(r'3m|s|1m|2m')
               tweet_sent_time = get_time()
               try:
                    alert_message_exist = alert_message.search(tweet)
                    alert_message_do_exist = alert_message_exist.group()
                    tweet_new_exist = old_tweet_checker.search(tweet_sent_time)
                    tweet_new_do_exist = tweet_new_exist.group()
               except:
                    gg = 'gg'
               else:
                    mail_initiate()
                    done = 'done'
               time.sleep(1)
               driver.refresh()
               time.sleep(4)
     while True:
          tweet_detect()
     #coding experience or knowledge dosen't matter in the face of universities who are known for IT

#window
tkWindow = Tk()  
tkWindow.geometry('400x400')  
tkWindow.title('Message Bot')

#database label and text entry box
filename = Label(tkWindow)

filename["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
filename["font"] = ft
filename["fg"] = "#ffffff"
filename["justify"] = "center"
filename["text"] = "File_name(eg AK.mp3)"
filename.place(x=0,y=10,height=20)#.grid(row=7, column=0)


filename = StringVar()
filenameEntry = Entry(tkWindow, textvariable=filename)
filenameEntry["bg"] = "#636060"
filenameEntry["fg"] = "#ffffff"
filenameEntry.place(x=130,y=10,height=20)

#file location entry box
fileLocation = Label(tkWindow)

fileLocation["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
fileLocation["font"] = ft
fileLocation["fg"] = "#ffffff"
fileLocation["justify"] = "center"
fileLocation["text"] = "fileLocation"
fileLocation.place(x=0,y=60,height=20)#.grid(row=7, column=0)

fileLocation = StringVar()
fileLocationEntry = Entry(tkWindow, textvariable=fileLocation)
fileLocationEntry["bg"] = "#636060"
fileLocationEntry["fg"] = "#ffffff"
fileLocationEntry.place(x=130,y=60)

#twitterpage link

twitterpage = Label(tkWindow)
twitterpage["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
twitterpage["font"] = ft
twitterpage["fg"] = "#ffffff"
twitterpage["justify"] = "center"
twitterpage["text"] = "twitterpage"
twitterpage.place(x=0,y=110,height=20)#.grid(row=7, column=0)

twitterpage = StringVar()
twitterpageEntry = Entry(tkWindow, textvariable=twitterpage)
twitterpageEntry["bg"] = "#636060"
twitterpageEntry["fg"] = "#ffffff"
twitterpageEntry.place(x=130,y=110)

#body of the letter
letterbody = Label(tkWindow)

letterbody["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
letterbody["font"] = ft
letterbody["fg"] = "#ffffff"
letterbody["justify"] = "center"
letterbody["text"] = "letterbody"
letterbody.place(x=0,y=160,height=20)#.grid(row=7, column=0)

letterbody = StringVar()
letterbodyEntry = Entry(tkWindow, textvariable=letterbody)
letterbodyEntry["bg"] = "#636060"
letterbodyEntry["fg"] = "#ffffff"
letterbodyEntry.place(x=130,y=160)

#subject of the letter
subject = Label(tkWindow)

subject["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
subject["font"] = ft
subject["fg"] = "#ffffff"
subject["justify"] = "center"
subject["text"] = "subject"
subject.place(x=0,y=210,height=20)#.grid(row=7, column=0)

subject = StringVar()
subjectEntry = Entry(tkWindow, textvariable=subject)
subjectEntry["bg"] = "#636060"
subjectEntry["fg"] = "#ffffff"
subjectEntry.place(x=130,y=210)

#recepients
recepients = Label(tkWindow)

recepients["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
recepients["font"] = ft
recepients["fg"] = "#ffffff"
recepients["justify"] = "center"
recepients["text"] = "recepients"
recepients.place(x=0,y=260,height=20)#.grid(row=7, column=0)

recepients = StringVar()
recepientsEntry = Entry(tkWindow, textvariable=recepients)
recepientsEntry["bg"] = "#636060"
recepientsEntry["fg"] = "#ffffff"
recepientsEntry.place(x=130,y=260)

#catchphrase
catchphrase = Label(tkWindow)

catchphrase["bg"] = "#636060"
ft = tkFont.Font(family='Times',size=10)
catchphrase["font"] = ft
catchphrase["fg"] = "#ffffff"
catchphrase["justify"] = "center"
catchphrase["text"] = "catchphrase"
catchphrase.place(x=0,y=310,height=20)#.grid(row=7, column=0)

catchphrase = StringVar()
catchphraseEntry = Entry(tkWindow, textvariable=catchphrase)
catchphraseEntry["bg"] = "#636060"
catchphraseEntry["fg"] = "#ffffff"
catchphraseEntry.place(x=130,y=310)

validateLogin = partial(validateLogin, filename, fileLocation, twitterpage, letterbody, subject, recepients, catchphrase)

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
StartButton.place(x=230, y=350)
tkWindow['bg'] = '#414141'
tkWindow.iconbitmap(r"F:\python\Alien monster emoji.ico")
tkWindow.mainloop()


