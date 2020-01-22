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

    def findOne(self,collection):
        col = self.stk_db[collection]
        return col.find_one()

    def findMany(self,collection):
        col = self.stk_db[collection]
        return col.find()
    
    def findQuery(self,collection,query):
        col = self.stk_db[collection]
        return col.find(query)
    
    def delManyQuery(self,collection,query):
        col = self.stk_db[collection]
        res = col.delete_many(query)
        return res.deleted_count

    def delAll(self,collection):
        col = self.stk_db[collection]
        res = col.delete_many({})
        return res.deleted_count
    
    def dropCollection(self,collection):
        col = self.stk_db[collection]
        col.drop()
    