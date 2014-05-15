#!/usr/bin/python
# coding=latin1

"""
Datums-Rumgerechne 
"""

import datetime as DT
import random

Birthdays = { 'Kathrin' : DT.date(1972,1,31) , 'Bruce' : DT.date(1967,3,15) , 'Jesus' : DT.date(1,12,24)}
Weekdays = ['Montag'  , 'Dienstag' , 'Mittwoch' , 'Donnerstag' , 'Freitag' , 'Samstag' , 'Sonntag']

def nextBirthday(bd, cd):
    nextbd = bd.replace(year=cd.year)
    if((nextbd-cd).days < 0):
        nextbd = nextbd.replace(year=cd.year+1)
    return nextbd


currentdate = DT.datetime.today().date()
print "Aktuelles Datum: " , currentdate
print "Kathrins Geburtstag: " , Birthdays['Kathrin']
print "Bruces Geburtstag: " , Birthdays['Bruce']
print "-------------------------------------------------"
print "Differenz der Geburtstage von Bruce und Kathrin: ", (Birthdays['Kathrin']-Birthdays['Bruce']).days
randomweek = random.randint(1,52)
print "%s Wochen nach Kathrins Geburtstag: %s" % (randomweek, Birthdays['Kathrin'] + DT.timedelta(weeks=randomweek))
print "Wochentag von Kathrins Geburtstag: ", Weekdays[Birthdays['Kathrin'].isoweekday()]
print "Wochentag von Bruces Geburtstag: ", Weekdays[Birthdays['Bruce'].isoweekday()]
print "Lebenstage von Kathrin bis heute: ", (currentdate - Birthdays['Kathrin']).days
print "Lebenstage von Bruce bis heute: ", (currentdate - Birthdays['Bruce']).days
print "-------------------------------------------------"
nextBirthdays = dict((key, nextBirthday(Birthdays[key], currentdate)) for key in Birthdays.keys())
print "Nächster Geburtstag von Kathrin: ", nextBirthdays['Kathrin']   
print "Nächster Geburtstag von Bruce: ", nextBirthdays['Bruce']
print "Differenz der nächsten Geburtstage von Kathrin und Bruce: ", (nextBirthdays['Bruce']-nextBirthdays['Kathrin']).days
print "Tage bis zum nächsten Geburtstag von Kathrin: ", (nextBirthdays['Kathrin'] - currentdate).days
print "Tage bis zum nächsten Geburtstag von Bruce: ", (nextBirthdays['Bruce'] - currentdate).days
print "-------------------------------------------------"
print "Tage bis Weihnachten: ", (nextBirthdays['Jesus'] - currentdate).days
print "-------------------------------------------------"
print "TEMP = ", (38025-36103)/((DT.date(2014,1,26) - DT.date(2012,12,21)).days / 365.0)*0.2703+12*17.57
