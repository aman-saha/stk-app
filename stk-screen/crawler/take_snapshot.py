import os, sys, time
from clear import clear
from interpret import interpret
from snapshot import snapshot
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

print "Clearing the collection data"
clear = clear()
clear.clearAllCollections()
clear.clearAllSnapshotCollections()
print "Clearing Done !!!"

print "-----------------------------------"

print " Creating Snapshot ..."
ob = snapshot()
ob.initCrawl()
print "Snapshot Taken !!!"

print "-----------------------------------"

print "Clearing the collection data"
clear.clearAllCollections()
print "Clearing Done !!!"

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
