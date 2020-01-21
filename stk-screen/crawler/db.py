import os, sys, time
import pymongo
class db():
    def __init__(self,client):
        self.client = client
    def existsDb(self):
        dblist = self.client.list_database_names()
        if "stk_db" in dblist:
	        print("The database exists \n")
        else:
            print ("The database doesn't exists \n")
    def insertOne(self):
        print "Hello sbsbdworld"