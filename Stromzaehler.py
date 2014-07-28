#!/usr/bin/python

import datetime as DT

readings = {DT.date(2013,1,29) : 36369.0 ,
            DT.date(2013,5,15) : 36674.0 ,
            DT.date(2013,12,31) : 37864.0 ,
            DT.date(2014,1,26) : 38035.0 ,
            DT.date(2014,7,28) : 39164.0 ,
            }

readings_end = readings.copy()
readings_end.pop(DT.date(2013,1,29))

for date_begin, date_end in zip(sorted(readings), sorted(readings_end)):
    kw_per_day = (readings_end[date_end] - readings[date_begin]) / (date_end - date_begin).days;
    # leap year can be neglected 
    kw_per_year = kw_per_day * 365;       
    print date_begin, " - " , date_end, ": ", kw_per_day , "kW per day (", kw_per_year, " kW per year)"

