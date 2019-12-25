#helloworl!
import os, sys, time
from db import db as db
import selenium
import pymongo
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class crawler():
	def __init__(self, driver,url):
		self.driver = driver
		self.url = url
	
	def initFirefoxBrowser(self):
		driver.get(self.url)

	def getStockList(self):
		print "Hello world!!"
		stockIndex = ["Nifty 50", "Nifty Next 50", "Nifty Midcap 50"]
		for index in stockIndex:
			ob.getEachStock(index)
			time.sleep(5)
		
	def getEachStock(self,index):
		select = Select(driver.find_element_by_name('bankNiftySelect'))
		select.select_by_visible_text(index)
		self.driver.find_element_by_name('bankNiftySelect').click()
		table = self.driver.find_element_by_xpath('//*[@id="dataTable"]')
		rows = table.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr') # get all of the rows in the table
		for row in rows:
			print row.text+"\n"

	def quit(self):	
		self.driver.quit()

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--incognito")
driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="/Users/amsaha/workspaces/git_proj/stk-app/stk-screen/crawler/drivers/geckodriver")
url = "https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
conn = pymongo.MongoClient("mongodb://localhost:27017/")
# ob = crawler(driver,url)
# ob.initFirefoxBrowser()
# ob.getStockList()
# ob.quit()
db = db(conn)
db.insertOne()
