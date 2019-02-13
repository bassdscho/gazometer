#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
echo `date +%d.%m.%y`\;`date +%H:%M`\;`cat /home/pi/gazometer/value` >> /media/ds_sonstiges/Energieverbrauch/gas.csv
