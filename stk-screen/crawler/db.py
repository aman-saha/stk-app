import os, sys, time
import pymongo
class db():
    def __init__(self,conn):
        self.conn = conn
    def insertOne(self):
        print "Hello sbsbdworld"