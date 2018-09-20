#!/usr/bin/python

# Name: Check Boiler Fault Code (Nagios)
# Author: Thomas Chubb
# URL: blog.tchubb.co.uk
# Version: 0.8
# Date: 27/01/2018

# Required modules
import subprocess,sys

# Check the service
retryCount = 0
retryWait = 2
while True:
    # Query the boiler
    test = subprocess.Popen(['/usr/bin/ebusctl','read','-f','currenterror'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()[0]
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
if test == '-;-;-;-;-':
    print 'OK - There are currently no boiler faults. Boiler response: ' + test
    sys.exit(0)

# Fault code meanings
faultCodes = {
    0:'Flow-NTC open circuit',
    1:'Return-NTC open circuit',
    10:'Flow NTC short circuit',
    11:'Return NTC short circuit',
    13:'Tank NTC short circuit',
    20:'Safety temperature limiter by NTC activated',
    22:'Dry fire',
    23:'Water shortage, temperature difference between flow and return NTC too large',
    24:'Water shortage, temperature rise too quick',
    25:'Interruption in the compact thermal module cable harness',
    27:'Incorrect sensing of flame',
    28:'Appliance does not start: Attempts to ignite during start failed',
    29:'Flame goes off during operation and subsequent ignition attempts failed',
    32:'Fan speed variation',
    49:'eBUS undervoltage',
    61:'Gas-valve control defective',
    62:'Gas valve shutoff delay',
    63:'EEPROM error',
    64:'Electronics/NTC fault',
    65:'Electronics temperature too high',
    67:'Flame detector input signal is outside the limits (0 or 5 V)',
    70:'No valid DSN in display and/or mainboard',
    71:'Flow NTC reports constant value (stuck at)',
    72:'Flow and/or return NTC fault',
    73:'Water pressure sensor signal out of range (too low)',
    74:'Water pressure sensor signal out of range (too high)',
    75:'No pressure rise was detected on turning on the pump',
    76:'Overheating protection on primary heat exchanger triggered',
    77:'Condensate pump or feedback of accessorie blocks heating',
    78:'wrong configuration with accessory',
    'con':'no communication to mainboard'	
}

# Parse boiler response
faultCode = int(test.split(';')[0])

# Return nagios result
try:
    errorMessage = 'CRITICAL - ' + 'F.' + str(faultCode) + ' ' + faultCodes[faultCode] + ' (' + test + ')'
except:
    print 'UNKNOWN - Undefined boiler fault' + ' (' + test + ')'
    sys.exit(3)
	
print errorMessage
sys.exit(2)


