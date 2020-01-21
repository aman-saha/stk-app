import os, sys, time
import pymongo
class db():
    def __init__(self,client,stk_db):
        self.client = client
        self.stk_db = stk_db
    def insertMany(self,stockBulkData,collection):
        print collection + "\n"
        col = self.stk_db[collection]
        res = col.insert_many(stockBulkData)
        print (res.inserted_ids)
    def dropCollection(self,collection):
        col = self.stk_db[collection]
        col.drop()
    