#helloworld!
import os, sys, time
import locale
import selenium
import pymongo
import requests
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from db import db
from datetime import datetime

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

now = datetime.now()
currentDate = now.strftime("%d/%m/%Y")
currentTime = now.strftime("%H:%M:%S")


class cr():
	def __init__(self):
		self.url = "http://aman.com/index.html"
	
	def initCrawl(self):
		self.initFirefoxBrowser()
		self.quitt()

	def initFirefoxBrowser(self):
		firefox_options = webdriver.FirefoxOptions()
		firefox_options.add_argument("--incognito")
		#firefox_options.add_argument("--headless")
		self.driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="/Users/amsaha/workspaces/git_proj/stk-app/stk-screen/crawler/drivers/geckodriver")
		# self.driver.get(self.url)
		time.sleep(10)
		for i in range(1,5):
			self.driver.get("http://aman.com/index.html")
			print(self.driver.current_url)
			time.sleep(2)
			s = requests.Session()
			resp = s.post("http://aman2.com/aman2.html")
			self.driver.get("http://aman2.com/aman2.html")
			print(self.driver.current_url)
			time.sleep(2)
	def quitt(self):
		self.driver.quit()

ob = cr()
ob.initCrawl()




