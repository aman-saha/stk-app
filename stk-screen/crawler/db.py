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

    # inserts N documents into a collection
    def insertMany(self,stockBulkData,collection):
        col = self.stk_db[collection]
        res = col.insert_many(stockBulkData)

    # returns the first document in a collection
    def findOne(self,collection):
        col = self.stk_db[collection]
        return col.find_one()

    # returns all the documents in a collection
    def findMany(self,collection):
        col = self.stk_db[collection]
        return col.find()

    # return all document matching a particular query
    def findQuery(self,collection,query):
        col = self.stk_db[collection]
        return col.find(query)

    # delete all documents matching a particular query in a collection and return count
    def delManyQuery(self,collection,query):
        col = self.stk_db[collection]
        res = col.delete_many(query)
        return res.deleted_count

    # delete all documents in a collection and return count
    def delAll(self,collection):
        col = self.stk_db[collection]
        res = col.delete_many({})
        return res.deleted_count
    # returns no of documents in a collection
    def count(self,collection,query):
        col = self.stk_db[collection]
        return col.count(query)
    # delete a collection
    def dropCollection(self,collection):
        col = self.stk_db[collection]
        col.drop()
    
    def getLastNDocuments(self,N,collection):
        col = self.stk_db[collection]
        if(col.count() < N):
            return "Try another time!!!"
        return col.find().skip(col.count() - N)
    def getLastNDocumentsByQuery(self,N,collection,query):
        print query
        col = self.stk_db[collection]
        N = min(N,col.count()/50)
        return col.find(query).limit(N)
    