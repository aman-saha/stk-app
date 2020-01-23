#helloworld!
import os, sys, time
from datetime import datetime
from db import db
collections = {
			'Nifty 50' : 'nifty_50',
			'Nifty Next 50' : 'nifty_next_50',
			# 'Nifty Midcap 50' : 'nifty_midcap_50',
			# 'Nifty Smlcap 50':'nifty_smlcap_50',
            'Nifty Bank' : 'nifty_bank',
		}
class interpret():
    def __init__(self):
        self.marketSentiment = 0
        self.globalMarketSentiment = 0
        self.retracement_stock = []
        self.optional_stock = []

    def getStockData(self):
        for index in collections.values():
            stock_data = db.findMany(index)
            for stock in stock_data:
                if stock:
                    self.stockCall(stock)

    def calMarketSentiment(self):
        index_val = []
        index_arr = ['nifty_50','nifty_bank']
        for index in index_arr:
            res = db.findOne(index)
            if(res):
                index_val.append(res)
        for i in range(0,len(index_val)):
            self.marketSentiment = index_val[i]['Chng']
        print self.marketSentiment
        
    def stockCall(self,stock):
        print stock["Symbol"]
        symbol = stock["Symbol"]
        ltp = stock["LTP"]
        chng = abs(stock["Chng"])
        chng_percent = stock["Chng%"]
        if(chng_percent >= 3):
            self.retracement_stock.append(symbol)
        elif(stock["LTP"] < 10000):
            if (ltp < 220):
                if chng >= 1:
                    self.optional_stock.append(symbol)
            elif (ltp > 221 and ltp < 250):
                if chng >= 3:
                    self.optional_stock.append(symbol)
            elif (ltp > 251 and ltp < 450):
                if chng >= 4:
                    self.optional_stock.append(symbol)
            elif (ltp > 451 and ltp < 999):
                if chng >=5:
                    self.optional_stock.append(symbol)
            elif (ltp > 999  and ltp < 2200):
                if(chng >= 8):
                    self.optional_stock.append(symbol)
            elif (ltp > 2300):
                if(chng > 30):
                    self.optional_stock.append(symbol)

    def retracementCall(self):
        print "Sending E-mail to Aman\nRetracement Call :\n"    
        print self.retracement_stock
        print "\n"
    
    def OptionalCall(self):
        print "Sending E-mail to Aman\nOptional Call :\n"
        print self.optional_stock
        print "\n"
    
    def gapUpCall(self):

    def gapDownCall(self):
    
    def call(self):
        self.getStockData()
        self.retracementCall()
        self.OptionalCall()
        self.calMarketSentiment()
db = db()