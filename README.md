# check_vaillant_ebus

I started writing a collection of Nagios checks to monitor my Vaillant Combi Boiler (Vaillant ecoTec plus 824 R1) in late 2016. I have recently been updating them so I thought I should share them for anyone as mad as me. I am still working on the scripts so they are very much a work in progress with some scrips containing hardcored values etc.

**Current Version:** Release v1.0

Checks:

 * check_vaillant_ebus_faultcode.py - checks the boiler for a fault and if one is found translates the 'F' code into the human readable fault description
 * check_vaillant_ebus_flowtemp.py - checks the bolier flow temperature (useful to monitor if the heating is working as expected)
 * check_vaillant_ebus_pressure.py - checks the boiler pressure and alerts if too high or too low to prevent a fault (dry fire)
 
perfdata is returned by the pressure and flowtemp checks for graphing

## Script Dependencies

The script use EBUSD to query the boiler. (thank you John!)

[EBUSD](https://github.com/john30/ebusd/wiki)


## How it Works with Nagios Core

Nagios Core --> NRPE --> EBUSD --> USB to EBUS Adapter --> Vaillant Boiler

I plan to do a full guide on how to setup these checks in the future.

## Release Notes

v1.0 - Initial version

## Contribute/Feature Requests

I am always happy to recieve feedback good or bad. I plan to improve and expand on these checks.

Drop me a line if you find a bug or want a feature adding to an existing check or have an idea for an additional check.

Feel free to message me if you need help getting the checks working with your boiler.

https://github.com/tschubb/check_vaillant_ebus