#helloworl!
import os, sys, time
import selenium
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def initFirefoxBrowser(url):
	firefox_options = webdriver.FirefoxOptions()
	firefox_options.add_argument("--incognito")
	driver = webdriver.Firefox(executable_path="/Users/amsaha/workspaces/git_proj/stk-app/stk-screen/crawler/drivers/geckodriver")
	driver.get(url)
	getStockList(driver)
	quit(driver)

def quit(driver):	
	driver.quit()

def getStockList(driver):
	print "Hello world!!"
	stockIndex = ["Nifty 50", "Nifty Next 50", "Nifty Midcap 50"]
	for index in stockIndex:
		getEachStock(index,driver)
		time.sleep(5)
	
	
def getEachStock(index,driver):
	select = Select(driver.find_element_by_name('bankNiftySelect'))
	select.select_by_visible_text(index)
	driver.find_element_by_name('bankNiftySelect').click()
	table = driver.find_element_by_xpath('//*[@id="dataTable"]')
	rows = table.find_elements_by_xpath('//*[@id="dataTable"]/tbody/tr') # get all of the rows in the table
	for row in rows:
		print row.text+"\n"

def main():
	url = "https://www.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"
	initFirefoxBrowser(url)

main()
