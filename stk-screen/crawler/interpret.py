#helloworld!
import os, sys, time
from datetime import datetime
from db import db
collections = {
			'Nifty 50' : 'nifty_50',
			# 'Nifty Next 50' : 'nifty_next_50',
			# 'Nifty Midcap 50' : 'nifty_midcap_50',
			# 'Nifty Smlcap 50':'nifty_smlcap_50',
            'Nifty Bank' : 'nifty_bank',
		}
class interpret():
    def __init__(self):
        self.marketSentiment = 0
        self.globalMarketSentiment = 0

    def getStockData(self):
        for index in collections.values():
            stock_data = db.findMany(index)
            for stock in stock_data:
                if stock:
                    ob.stockCall(stock)
                    
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
        print stock
        print "\n"
        stock_symbols = []
        symbol = stock["Symbol"]
        ltp = stock["LTP"]
        chng = abs(stock["Chng"])
        chng_percent = abs(stock["Chng%"])
        if(chng_percent > 3):
            ob.retracementCall(symbol)
        elif(stock["LTP"] < 10000):
            if (ltp < 220):
                if chng >= 1:
                    stock_symbols.append(symbol)
            elif (ltp > 221 and ltp < 250):
                if chng >= 3:
                    stock_symbols.append(symbol)
            elif (ltp > 251 and ltp < 450):
                if chng >= 4:
                    stock_symbols.append(symbol)
            elif (ltp > 451 and ltp < 999):
                if chng >=5:
                    stock_symbols.append(symbol)
            elif (ltp > 999  and ltp < 2200):
                if(chng >= 8):
                    stock_symbols.append(symbol)
            elif (ltp > 2300):
                if(chng > 30):
                    stock_symbols.append(symbol)
            ob.OptionalCall(stock_symbols)

    def retracementCall(self,stockSymbol):
        print "Sending E-mail to Aman\n"
    
    def OptionalCall(self,stockSymbols):
        print "Sending E-mail to Aman\n"
        print stockSymbols

db = db()
ob = interpret()
ob.getStockData()
# ob.calMarketSentiment()