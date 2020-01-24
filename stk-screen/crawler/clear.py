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
class clear():
    def __init__(self):
        self.remove = 1
    def clearAllCollections(self):
        for index in collections.values():
            print "Clearing collection : " + index + "\n" 
            db.delAll(index)

db = db()