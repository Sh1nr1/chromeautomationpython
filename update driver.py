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

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\User Data")
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
