#!/usr/bin/python

# Name: Check Boiler Pressure (Nagios)
# Author: Thomas Chubb
# URL: blog.tchubb.co.uk
# Version: 0.4
# Date: 27/01/2018

# Required modules
import subprocess,sys,time

# Settings
criticalLow = 0.55
warningLow = 0.6
warningHigh = 1.8
criticalHigh = 2.0

# Check the service
retryCount = 0
retryWait = 2
while True:
    # Query the boiler
    test = subprocess.Popen(['/usr/bin/ebusctl','read','-f','WaterPressure'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
    test = test.strip()
    # Return unknown if response contains ERR but retry 4 times as EBUSD can return an odd string
    if 'ERR' in test and retryCount == 4:
        print 'UNKNOWN - ebusd returned an error ' + '(' + test + ')'
        sys.exit(3)
    elif 'ERR' in test:
        retryCount += 1
        time.sleep(retryWait)
        retryWait += 5
    else:
        break

# Return nagios result
pressure = float(test.split(';')[0])
result = '- Central heating water pressure is ' + str(pressure) + ' bar|pressure=' + str(pressure)
if pressure > warningLow and pressure < warningHigh:
    print 'OK',result
    sys.exit(0)
elif pressure >= criticalHigh or pressure <= criticalLow:
    print 'CRITICAL',result
    sys.exit(2)
else:
    print 'WARNING',result
    sys.exit(1)

