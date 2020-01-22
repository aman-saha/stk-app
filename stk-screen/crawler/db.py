#helloworld!
import os, sys, time
import pymongo
from pymongo import MongoClient
class db():
    def __init__(self):
        client = MongoClient()
        stk_db = client['stk_db']
        self.client = client
        self.stk_db = stk_db
    def insertMany(self,stockBulkData,collection):
        print collection + "\n"
        col = self.stk_db[collection]
        res = col.insert_many(stockBulkData)
        print (res.inserted_ids)
    def findOne(self,collection):
        col = self.stk_db[collection]
        return col.find_one()
    def findMany(self,collection):
        col = self.stk_db[collection]
        return col.find()
    def dropCollection(self,collection):
        col = self.stk_db[collection]
        col.drop()
    