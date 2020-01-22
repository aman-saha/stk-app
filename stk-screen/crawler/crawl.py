#helloworld!
import os, sys, time
import locale
import selenium
import pymongo
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
print currentDate
print currentTime

class crawl():
	def __init__(self,url):
		self.url = url
	
	def initFirefoxBrowser(self):
		firefox_options = webdriver.FirefoxOptions()
		firefox_options.add_argument("--incognito")
		firefox_options.add_argument("--headless")
		self.driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="/Users/amsaha/workspaces/git_proj/stk-app/stk-screen/crawler/drivers/geckodriver")
		self.driver.get(self.url)

	def getStockList(self):
		print "Hello world!!"
		#stockIndex = ["Nifty 50", "Nifty Next 50", "Nifty Midcap 50"]
		stockIndex = ["Nifty 50", "Nifty Bank"]
		for index in stockIndex:
			ob.getEachStock(index)
			time.sleep(5)
		
	def getEachStock(self,index):
		select = Select(self.driver.find_element_by_name('bankNiftySelect'))
		select.select_by_visible_text(index)
		self.driver.find_element_by_name('bankNiftySelect').click()
		table = self.driver.find_element_by_xpath('//*[@id="dataTable"]')
		rows = table.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr') # get all of the rows in the table
		
		collections = {
			'Nifty 50' : 'nifty_50',
			'Nifty Next 50' : 'nifty_next_50',
			'Nifty Midcap 50' : 'nifty_midcap_50',
			'Nifty Smlcap 50':'nifty_smlcap_50',
			'Nifty Bank' : 'nifty_bank',
		}
		stockBulkData = []
		stockData = {}
		for row in rows:
			stockData = ob.parseRow(row)
			if stockData:
				stockBulkData.append(stockData)
		# print stockBulkData
		print collections[index]
		db.insertMany(stockBulkData,collections[index])
		

	def quit(self):	
		self.driver.quit()

	def parseRow(self,row):
		row = row.text
		print row
		print "\n"
		row_data = row.split()
		print row_data
		print "\n"
		stock_data = {}
		if(row_data[0] != "Symbol"):
			stock_data = {
				"Symbol" : str(row_data[0]),
				"Open" : locale.atof(row_data[3]),
				"High" : locale.atof(row_data[4]),
				"Low" : locale.atof(row_data[5]),
				"LTP" : locale.atof(row_data[6]),
				"Chng" : locale.atof(row_data[7]),
				"Chng%" : locale.atof(row_data[8]),
				"Volume" : locale.atof(row_data[8]),
				"Date" : currentDate,
				"Time" : currentTime,
			}
		print stock_data
		print "\n"
		return stock_data



db = db()

url = "https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
ob = crawl(url)
ob.initFirefoxBrowser()
ob.getStockList()
ob.quit()



