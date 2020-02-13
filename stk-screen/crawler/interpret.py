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
        self.positve_retracement_stock = []
        self.negative_stock = []
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
                if(doc["LTP"] > 200 and doc["LTP"] < 10000):
                    open_gap = abs(doc["Open"] - stock["Open"])
                    if(doc["Open"] > stock["Open"] and open_gap > 3):
                        self.gap_up_stock.append(symbol)
                    elif(doc["Open"] < stock["Open"] and open_gap > 3):
                        self.gap_down_stock.append(symbol)

        if(chng_percent >= 3 and ltp < 10000):
            self.positve_retracement_stock.append(stock)
        elif(chng_percent <= -0.7 and ltp > 200 and ltp < 10000):
            self.negative_stock.append(stock)
        elif(ltp > 200 and ltp < 10000):
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
        pos_symbols = []
        neg_symbols = []
        print "\n Sending E-mail to Aman\n Positve Retracement Call :\n"
        for i in self.positve_retracement_stock:
            # print "Symbol = " + str(i["Symbol"])
            # print "LTP = " + str(i["LTP"])
            # print "Change% = " + str(i["Chng%"])
            # print "High = " + str(i["High"])
            # print "-------------------------"
            pos_symbols.append(str(i["Symbol"]))
        print pos_symbols

        print "\n Negative Sell Call :\n"
        for i in self.negative_stock:
            neg_symbols.append(str(i["Symbol"]))
        print neg_symbols

    def OptionalCall(self):
        symbols = []
        print "\nSending E-mail to Aman\nOptional Call :\n"
        for i in self.optional_stock:
            symbols.append(str(i["Symbol"]))
        print symbols

    def gapCall(self):
        print "\nGap Up Call\n"
        print self.gap_up_stock

        print "\nGap Down Call\n"
        print self.gap_down_stock

    def call(self):
        self.getStockData()
        self.retracementCall()
        self.OptionalCall()
        self.gapCall()
        # self.calMarketSentiment()
db = db()
