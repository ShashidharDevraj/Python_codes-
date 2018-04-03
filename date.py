# Script to convert the Date time format.

# Tue Apr 03 03:22:40 UTC 2018.    # Actual Input
# 2018-04-03 03:22:40 UTC          # Expected Output

from time import strptime

a = "Tue Apr 03 03:22:40 UTC 2018"

month = strptime(a[4:7], '%b').tm_mon

Month  = str(month).zfill(2) 

print(a[-4:]+ '-' + str(Month) + '-' + a[8:-5])

