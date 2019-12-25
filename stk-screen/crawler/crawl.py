#helloworl!
import os, sys, time
import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def initChromeBrowser():
	driver = webdriver.Firefox(executable_path="drivers/geckodriver")
	url = "https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
	driver.get(url)
	getStockList(driver)

def quit(driver):	
	driver.quit()

def getStockList(driver):
	print "Hello world!!"
	select = Select(driver.find_element_by_name('bankNiftySelect'))
	select.select_by_visible_text("Nifty Midcap 50")
	driver.find_element_by_name('bankNiftySelect').click()
	table = driver.find_element_by_xpath('//*[@id="dataTable"]')
	rows = table.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr') # get all of the rows in the table
	for row in rows:
		print row.text+"\n"
	time.sleep(10)
	quit(driver)

def main():
	initChromeBrowser()

main()
