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

collections = {
			'Nifty 50' : 'nifty_50',
			'Nifty Next 50' : 'nifty_next_50',
			'Nifty Midcap 50' : 'nifty_midcap_50',
		}
snapshot_collections = {
			'Nifty 50' : 'snapshot_nifty_50',
			'Nifty Next 50' : 'snapshot_nifty_next_50',
			'Nifty Midcap 50' : 'snapshot_nifty_midcap_50',
		}

class crawl():
	def __init__(self):
		self.url = "https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
	
	def initCrawl(self):
		for index in collections.keys():
			self.initFirefoxBrowser()
			time.sleep(5)
			self.getEachStock(index)
			self.quit()

	def initFirefoxBrowser(self):
		firefox_options = webdriver.FirefoxOptions()
		firefox_options.add_argument("--incognito")
		firefox_options.add_argument("--headless")
		self.driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="/Users/amsaha/workspaces/git_proj/stk-app/stk-screen/crawler/drivers/geckodriver")
		self.driver.get(self.url)

	def getEachStock(self,index):
		select = Select(self.driver.find_element_by_name('bankNiftySelect'))
		select.select_by_visible_text(index)
		self.driver.find_element_by_name('bankNiftySelect').click()
		table = self.driver.find_element_by_xpath('//*[@id="dataTable"]')
		rows = table.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr') # get all of the rows in the table
		
		stockBulkData = []
		stockData = {}
		for row in rows:
			stockData = self.parseRow(row)
			if stockData:
				stockBulkData.append(stockData)
		db.insertMany(stockBulkData,collections[index])
		
	def quit(self):	
		self.driver.quit()

	def parseRow(self,row):
		row = row.text
		row_data = row.split()
		stock_data = {}
		if(row_data[0] != "Symbol"):
			if(row_data[0] != "NIFTY"):
				stock_data = {
					"Symbol" : str(row_data[0]),
					"Open" : locale.atof(row_data[1]),
					"High" : locale.atof(row_data[2]),
					"Low" : locale.atof(row_data[3]),
					"LTP" : locale.atof(row_data[4]),
					"Chng" : locale.atof(row_data[5]),
					"Chng%" : locale.atof(row_data[6]),
					"Volume" : locale.atof(row_data[7]),
					"Date" : currentDate,
					"Time" : currentTime,
				}
		return stock_data

db = db()



