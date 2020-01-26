import os, sys, time
from crawl import crawl
from clear import clear
from interpret import interpret
from db import db
from datetime import datetime

db = db()

now = datetime.now()
startDate = now.strftime("%d/%m/%Y")
startTime = now.strftime("%H:%M:%S")
print "==============================================="
print "Starting the Test - "
print "==============================================="

print "-----------------------------------"
print "Start Date : " + startDate
print "Start Time : " + startTime
print "-----------------------------------"

print "Crawling Started"
ob = crawl()
ob.initCrawl()
print "Crawling Done !!!"
print "-----------------------------------"

print "Analysis Started "
"Hello Aman! All the best. Please wait while we process."
ob = interpret()
print "Final Results : "
print "-----------------------------------"
ob.call()
print "Analysis Done!!!"

now = datetime.now()
endDate = now.strftime("%d/%m/%Y")
endTime = now.strftime("%H:%M:%S")
print "-----------------------------------"
print "End Date : " + endDate
print "End Time : " + endTime
print "-----------------------------------"
print "Ending the Test"
print "==============================================="

print "Crafted with love by Aman Saha"
