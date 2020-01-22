import os, sys, time
from crawl import crawl
from clear import clear
from interpret import interpret
from db import db

db = db()

clear = clear()
clear.clearAllCollections()

ob = crawl()
ob.initCrawl()

ob = interpret()
ob.call()

clear.clearAllCollections()


