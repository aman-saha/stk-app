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
snapshot_collections = {
			'Nifty 50' : 'snapshot_nifty_50',
			'Nifty Next 50' : 'snapshot_nifty_next_50',
			'Nifty Midcap 50' : 'snapshot_nifty_midcap_50',
			'Nifty Smlcap 50':'snapshot_nifty_smlcap_50',
			'Nifty Bank' : 'snapshot_nifty_bank',
		}
class analysis():
    def __init__(self):
        self.a = 1
    def fun(self):
        for i in snapshot_collections.values():
            print i
            print db.count(i,{})

db = db()
ob = analysis()
ob.fun()