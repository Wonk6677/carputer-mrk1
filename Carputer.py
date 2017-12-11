#!/usr/bin/env python
###########################################################################
# Carputer mrkl
###########################################################################
#-------------------------------------------------------------------------------
import obd

connection = obd.OBD("/dev/ttyUSB0") # create connection with USB 0

cmd = obd.commands.RPM # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint
print(response.value.to("RPM")) # user-friendly unit conversions