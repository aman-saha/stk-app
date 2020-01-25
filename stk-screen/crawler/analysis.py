import os, sys, time
from datetime import datetime
from db import db
collections = {
			'Nifty 50' : 'nifty_50',
			# 'Nifty Next 50' : 'nifty_next_50',
			# 'Nifty Midcap 50' : 'nifty_midcap_50',
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
			# print doc["Symbol"]
			self.getLastNCandles(doc["Symbol"],10,index)
	
    def getLastNCandles(self,symbol,N,index):
		each_stock = db.getLastNDocumentsByQuery(N,index,{"Symbol" : symbol})
		for doc in each_stock:
			print doc

db = db()
ob = analysis()
ob.fun()