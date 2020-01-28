#helloworld!
import os, sys, time
from datetime import datetime
from db import db
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
class interpret():
    def __init__(self):
        self.marketSentiment = 0
        self.globalMarketSentiment = 0
        self.retracement_stock = []
        self.optional_stock = []
        self.gap_up_stock = []
        self.gap_down_stock = []

    def getStockData(self):
        stock_data = []
        for index in collections.values():
            print index
            stock_data = db.getLastNDocuments(50,index) 
            for stock in stock_data:
                if stock:
                    self.stockCall(index,stock)

    # def calMarketSentiment(self):
    #     index_val = []
    #     index_arr = ['nifty_50','nifty_bank']
    #     for index in index_arr:
    #         res = db.findOne(index)
    #         if(res):
    #             index_val.append(res)
    #     for i in range(0,len(index_val)):
    #         self.marketSentiment = index_val[i]['Chng']
    #     print self.marketSentiment
        
    def stockCall(self,index,stock):
        symbol = stock["Symbol"]
        ltp = stock["LTP"]
        o_chng = stock["Chng"]
        chng = abs(stock["Chng"])
        chng_percent = stock["Chng%"]
        
        snap_stock = db.findLatestDoc(index,{"Symbol" : symbol})
        for doc in snap_stock:
            if doc:
                open_gap = abs(doc["Open"] - stock["Open"])
                if(doc["Open"] > stock["Open"] and open_gap > 3):
                    self.gap_up_stock.append(symbol)
                elif(doc["Open"] < stock["Open"] and open_gap > 3):
                    self.gap_down_stock.append(symbol)

        if(chng_percent >= 3 or chng_percent <=-1):
            self.retracement_stock.append(stock)
        elif(stock["LTP"] < 10000):
            if (ltp < 220):
                if chng >= 1:
                    self.optional_stock.append(stock)
            elif (ltp > 221 and ltp < 250):
                if chng >= 3:
                    self.optional_stock.append(stock)
            elif (ltp > 251 and ltp < 450):
                if chng >= 4:
                    self.optional_stock.append(stock)
            elif (ltp > 451 and ltp < 999):
                if chng >=5:
                    self.optional_stock.append(stock)
            elif (ltp > 999  and ltp < 2200):
                if(chng >= 8):
                    self.optional_stock.append(stock)
            elif (ltp > 2300):
                if(chng > 30):
                    self.optional_stock.append(stock)

    def retracementCall(self):
        symbols = []
        print "Sending E-mail to Aman\nRetracement Call :\n"
        for i in self.retracement_stock:
            symbols.append(i["Symbol"])
        print symbols

    def OptionalCall(self):
        symbols = []
        print "Sending E-mail to Aman\nOptional Call :\n"
        for i in self.optional_stock:
            symbols.append(i["Symbol"])
        print symbols

    def gapCall(self):
        print "Gap Up Call"
        print self.gap_up_stock

        print "Gap Down Call"
        print self.gap_down_stock

    def call(self):
        self.getStockData()
        self.retracementCall()
        self.OptionalCall()
        self.gapCall()
        # self.calMarketSentiment()
db = db()
