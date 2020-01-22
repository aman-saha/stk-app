#helloworld!
import os, sys, time
from datetime import datetime
from db import db

class interpret():
    def __init__(self):
        self.a = 1
    def getStockData(self):
        collections = {
			'Nifty 50' : 'nifty_50',
			'Nifty Next 50' : 'nifty_next_50',
			'Nifty Midcap 50' : 'nifty_midcap_50',
			'Nifty Smlcap 50':'nifty_smlcap_50',
            'Nifty Bank' : 'nifty_bank',
		}
        stock_data = db.findMany("nifty_bank")
        for i in stock_data:
            print i
            print "\n"

db = db()
ob = interpret()
ob.getStockData()