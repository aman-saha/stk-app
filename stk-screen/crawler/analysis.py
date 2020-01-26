import os, sys, time
from datetime import datetime
from db import db
import numpy as np
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
class analysis():
    def __init__(self):
        self.a = 1
    def fun(self):
		for index in collections.values():
			x = index.split("_")
			l = x[len(x) - 1]
			self.getRecentData(index)

    def getRecentData(self,index):
		stock_data = db.getLastNDocuments(5,index)
		for doc in stock_data:
			self.getLastNCandles(doc["Symbol"],10,index)
	
    def getLastNCandles(self,symbol,N,index):
		each_stock = db.getLastNDocumentsByQuery(N,index,{"Symbol" : symbol})
		candles = []
		for doc in each_stock:
			x = {
					"Open" : doc["Open"],
					"Low" : doc["Low"],
					"High" : doc["High"],
					"Chng" : doc["Chng"],
					"Chng%" : doc["Chng%"],
					"LTP" : doc["LTP"],
				}
			candles.append(x)
			self.analyzeCandle(candles)

    def analyzeCandle(self,candles):
		print candles
		self.rangeBreakout(candles)
	
    def rangeBreakout(self,candles):
		print "Range Breakout"
		last_candle = candles[len(candles) - 1]
		high_price = []
		low_price = []
		avg_price = []
		ltp = []
		for i in candles:
			high_price.append(i["High"])
			low_price.append(i["Low"])
			avg_price.append((i["High"] + i["Low"] / 2))
		high_mean = np.mean(high_price)
		low_mean = np.mean(low_price)
		print "High Mean"
		print high_mean
		print "Low Mean"
		print low_mean
		print "LTP"
		print last_candle["LTP"]

		


db = db()
ob = analysis()
ob.fun()