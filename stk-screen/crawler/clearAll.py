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
print "Starting to clear data - "
print "==============================================="

print "-----------------------------------"
print "Start Date : " + startDate
print "Start Time : " + startTime
print "-----------------------------------"

print "Clearing the collection data"
clear = clear()
clear.clearAllCollections()
clear.clearAllSnapshotCollections()
print "Clearing Done !!!"

print "-----------------------------------"

now = datetime.now()
endDate = now.strftime("%d/%m/%Y")
endTime = now.strftime("%H:%M:%S")
print "-----------------------------------"
print "End Date : " + endDate
print "End Time : " + endTime
print "-----------------------------------"
print "All data clearing done !!!"
print "==============================================="

print "Crafted with love by Aman Saha"
