#!/usr/bin/python
# Filename: Local.py
# support for Mouse Air
# Version 1.0 03/24/14 
#
# Local Execute Objects for RasPiConnect  
# to add Execute objects, modify this file 
#
#
#
# RasPiConnectServer interface constants

REMOTE_WEBVIEW_UITYPE = 1
ACTION_BUTTON_UITYPE = 16
FEEDBACK_ACTION_BUTTON_UITYPE = 17
SINGLE_LED_DISPLAY_UITYPE = 32
SPEEDOMETER_UITYPE = 64
VOLTMETER_UITYPE = 128
BARMETER_UITYPE = 129
SERVER_STATUS_UITYPE = 256
PICTURE_REMOTE_WEBVIEW_UITYPE = 512
LABEL_UITYPE = 1024
FM_BLINK_LED_UITYPE = 2048
TEXT_DISPLAY_UITYPE = 4096
TOGGLE_SWITCH_UITYPE = 33
SEND_TEXT_UITYPE = 34
SIMPLE_GAUGE_VIEW_LIVE_UITYPE = 37
SIMPLE_LINE_GRAPH_LIVE_UITYPE = 38
COMPLEX_LINE_GRAPH_LIVE_UITYPE = 42
# system imports
import sys
import subprocess
import time

# RasPiConnectImports

import Config
import Validate
import BuildResponse 

#
#
# Command to Mouse Air procdures
#
#
def sendCommandToMouseAirAndWait(command):
	status = True
	print "Sending Command: ", command

        f = open("/home/pi/MouseAir/state/MouseCommand.txt", "w")
        f.write(command)
        f.close()	
	timeout = 20		
	commandresponse = ""
	while timeout > 0:
		time.sleep(1.0)
		print "Waiting for Response"

        	f = open("/home/pi/MouseAir/state/MouseCommand.txt", "r")
        	commandresponse = f.read()
        	f.close()	
		timeout = timeout-1
		if (commandresponse == "DONE"):
			status = True
			print "Response = DONE"
			timeout = 0
		else:
			status = False
		 
	return status

def sendCommandToMouseAirAndReturn(command):

	return


def ExecuteUserObjects(objectType, element):

	# Example Objects

	# fetch information from XML for use in user elements

	#objectServerID is the RasPiConnect ID from the RasPiConnect App

        objectServerID = element.find("./OBJECTSERVERID").text
        objectID = element.find("./OBJECTID").text
      # find the interface object type
        objectName = element.find("./OBJECTNAME").text
        objectFlags = element.find("./OBJECTFLAGS").text


        if (Config.debug()):
        	print("objectServerID = %s" % objectServerID)
	# 
	# check to see if this is a Validate request
	#
        validate = Validate.checkForValidate(element)

        if (Config.debug()):
        	print "VALIDATE=%s" % validate

        
	# Build the header for the response

	outgoingXMLData = BuildResponse.buildHeader(element)


	# objects are split up by object types by Interface Constants
	#
	#
	#
	# search for matches to object Type 



	# object Type match
	if (objectType ==  COMPLEX_LINE_GRAPH_LIVE_UITYPE):

		if (Config.debug()):
			print "COMPLEX_LINE_GRAPH_LIVE_UITYPE of %s found" % objectServerID

		# CLGL-1 - ultrasonic graph
		if (objectServerID == "CLGL-1"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData
	
                        # normal response requested
			try:
        			f = open("/home/pi/MouseAir/state/UltrasonicGraph.txt", "r")
        			commandresponse = f.read()
        			f.close()	
			except IOError as e:
				commandresponse = "0^^0||No Data from MouseAir^^"			

                        outgoingXMLData += BuildResponse.buildResponse(commandresponse)


                        outgoingXMLData += BuildResponse.buildFooter()
                        return outgoingXMLData	



	# object Type match
	if (objectType ==  SIMPLE_LINE_GRAPH_LIVE_UITYPE):

		if (Config.debug()):
			print "SIMPLE_LINE_GRAPH_LIVE_UITYPE of %s found" % objectServerID

		# SLGL-1 - ultrasonic graph
		if (objectServerID == "SLGL-1"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData
	
                        # normal response requested
			try:
        			f = open("/home/pi/MouseAir/state/UltrasonicGraph.txt", "r")
        			commandresponse = f.read()
        			f.close()	
			except IOError as e:
				commandresponse = "0^^0||No Data from MouseAir^^"			

                        outgoingXMLData += BuildResponse.buildResponse(commandresponse)


                        outgoingXMLData += BuildResponse.buildFooter()
                        return outgoingXMLData	

	# object Type match
	if (objectType == PICTURE_REMOTE_WEBVIEW_UITYPE):

		if (Config.debug()):
			print "PICTURE_REMOTE_WEBVIEW_UITYPE of %s found" % objectServerID

		# W-10 - play a beep on the Raspberry Pi
		if (objectServerID == "W-10"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData
	
                        # normal response requested

                        imageName = "picamera.jpg"


                        responseData = "<html><head>"
                        responseData += "<META HTTP-EQUIV='CACHE-CONTROL' CONTENT='NO-CACHE'>"
                        responseData += "<title></title><style>body,html,iframe{margin:0;padding:0;}</style>"
                        responseData += "</head>"

                        responseData += "<body><img src=\""
                        responseData += Config.localURL()
                        responseData += "static/"
                        responseData += imageName
                        responseData += "\" type=\"jpg\" width=\"585\" height=\"300\">"

                        responseData +="</body>"

                        responseData += "</html>"


                        outgoingXMLData += BuildResponse.buildResponse(responseData)


                        outgoingXMLData += BuildResponse.buildFooter()
                        return outgoingXMLData	

	# object Type match
	if (objectType == ACTION_BUTTON_UITYPE):

		if (Config.debug()):
			print "ACTION_BUTTON_UTYPE of %s found" % objectServerID

		# B-10 - fire Mouse 
		if (objectServerID == "B-10"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-10 Fire Mouse"
			status = sendCommandToMouseAirAndWait("FIREMOUSE")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		

		# B-11 - take picture 
		if (objectServerID == "B-11"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-11 Take Picture"
			status = sendCommandToMouseAirAndWait("TAKEPICTURE")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		

		# B-13 - Pan to Mouse watch
		if (objectServerID == "B-13"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-13 Pan to Watch Mouse"
			status = sendCommandToMouseAirAndWait("PANTOMOUSE")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		
		# B-14 - Pan to Cat watch
		if (objectServerID == "B-14"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-14 Pan to Watch Cat"
			status = sendCommandToMouseAirAndWait("PANTOCAT")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		



		# B-15 - Shoot Solenoid 
		if (objectServerID == "B-15"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-15 Shoot Solenoid "
			status = sendCommandToMouseAirAndWait("SHOOTSOLENOID")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		
		# B-16 - Pan Left 
		if (objectServerID == "B-16"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-16 Pan Left"
			status = sendCommandToMouseAirAndWait("PANLEFT")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		
		
		
		
		# B-17 - Pan Right 
		if (objectServerID == "B-17"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-17 Pan Right"
			status = sendCommandToMouseAirAndWait("PANRIGHT")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		
		# B-18 - Tilt Up 
		if (objectServerID == "B-18"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-18 Tilt Up "
			status = sendCommandToMouseAirAndWait("TILTUP")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		
		# B-19 - Tilt Down 
		if (objectServerID == "B-19"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			print "set B-19 Tilt Down"
			status = sendCommandToMouseAirAndWait("TILTDOWN")
			
			responseData = "OK" 
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
	



	
	# object Type match
	if (objectType == FEEDBACK_ACTION_BUTTON_UITYPE):

		if (Config.debug()):
			print "FEEDBACK_ACTION_BUTTON_UTYPE of %s found" % objectServerID

		
		# FB-10 -  turn ultrasonics on and off 
		if (objectServerID == "FB-10"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

                        responseData = "XXX"

                        if (objectName is None):
                                objectName = "XXX"

               		lowername = objectName.lower()


                	if (lowername == "ultrasonic on"):
				
				status = sendCommandToMouseAirAndWait("ULTRASONICON") 
                        	responseData = "ultrasonic off" 
                        	responseData = responseData.title()


                	elif (lowername == "ultrasonic off"):
				
				status = sendCommandToMouseAirAndWait("ULTRASONICOFF")
                        	responseData = "ultrasonic on" 
                        	responseData = responseData.title()


			 # defaults to off 
                	else:
				status = sendCommandToMouseAirAndWait("ULTRASONICOFF") 
                        	lowername = "ultrasonic on" 
                        	responseData = lowername.title()

	
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData


		
		# FB-11 -  turn RFID on and off 
		if (objectServerID == "FB-11"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

                        responseData = "XXX"

                        if (objectName is None):
                                objectName = "XXX"

               		lowername = objectName.lower()


                	if (lowername == "rfid on"):
				
				status = sendCommandToMouseAirAndWait("RFIDON") 
                        	responseData = "RFID off" 
                        	responseData = responseData.title()


                	elif (lowername == "rfid off"):
				
				status = sendCommandToMouseAirAndWait("RFIDOFF")
                        	responseData = "RFID on" 
                        	responseData = responseData.title()


			 # defaults to off 
                	else:
				status = sendCommandToMouseAirAndWait("RFIDOFF") 
                        	lowername = "RFID on" 
                        	responseData = lowername.title()

	
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData

		# FB-12 -  turn USECAMERAMOTION on and off 
		if (objectServerID == "FB-11"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

                        responseData = "XXX"

                        if (objectName is None):
                                objectName = "XXX"

               		lowername = objectName.lower()


                	if (lowername == "camera motion on"):
				
				status = sendCommandToMouseAirAndWait("CAMERAMOTIONON") 
                        	responseData = "camera motion off" 
                        	responseData = responseData.title()


                	elif (lowername == "camera motion off"):
				
				status = sendCommandToMouseAirAndWait("CAMERAMOTIONOFF")
                        	responseData = "camera motion on" 
                        	responseData = responseData.title()


			 # defaults to off 
                	else:
				status = sendCommandToMouseAirAndWait("CAMERAMOTIONOFF") 
                        	lowername = "camera motion on" 
                        	responseData = lowername.title()

	
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData


		# FB-13 -  turn top servo on
		if (objectServerID == "FB-13"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

                        responseData = "XXX"

                        if (objectName is None):
                                objectName = "XXX"

               		lowername = objectName.lower()

			print("lowername =", lowername)

                	if (lowername == "top servo close"):
				
				print "set top servo close"
				status = sendCommandToMouseAirAndWait("TOPSERVOCLOSE") 
                        	responseData = "top servo open" 
                        	responseData = responseData.title()


                	elif (lowername == "top servo open"):
				
				print "set top servo open"
				status = sendCommandToMouseAirAndWait("TOPSERVOOPEN")
                        	responseData = "top servo close" 
                        	responseData = responseData.title()


			 # defaults to top servo closed
                	else:
				print "set top servo close"
				status = sendCommandToMouseAirAndWait("TOPSERVOCLOSE") 
                        	lowername = "top servo open" 
                        	responseData = lowername.title()

	
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData


		# FB-15 -  turn bottom servo on
		if (objectServerID == "FB-15"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

                        responseData = "XXX"

                        if (objectName is None):
                                objectName = "XXX"

               		lowername = objectName.lower()

			print("lowername =", lowername)

                	if (lowername == "bottom servo close"):
				
				print "set bottom servo close"
				status = sendCommandToMouseAirAndWait("BOTTOMSERVOCLOSE") 
                        	responseData = "bottom servo open" 
                        	responseData = responseData.title()


                	elif (lowername == "bottom servo open"):
				
				print "set bottom servo open"
				status = sendCommandToMouseAirAndWait("BOTTOMSERVOOPEN")
                        	responseData = "bottom servo close" 
                        	responseData = responseData.title()


			 # defaults to top servo closed
                	else:
				print "set bottom servo close"
				status = sendCommandToMouseAirAndWait("BOTTOMSERVOCLOSE") 
                        	lowername = "bottom servo open" 
                        	responseData = lowername.title()

	
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData


		# FB-16 -  turn motors on 
		if (objectServerID == "FB-16"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

                        responseData = "XXX"

                        if (objectName is None):
                                objectName = "XXX"

               		lowername = objectName.lower()


                	if (lowername == "motors on"):
				
				print "set Motors On"
				status = sendCommandToMouseAirAndWait("MOTORSON") 
                        	responseData = "motors Off" 
                        	responseData = responseData.title()


                	elif (lowername == "motors off"):
				
				status = sendCommandToMouseAirAndWait("MOTORSOFF")
                        	responseData = "Motors On" 
                        	responseData = responseData.title()


			 # defaults to Motors off 
                	else:
				print "Motors Off"
				status = sendCommandToMouseAirAndWait("MOTORSOFF") 
                        	lowername = "Motors On" 
                        	responseData = lowername.title()

	
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData


	else:
		return ""
	# returning a zero length string tells the server that you have not matched 
	# the object and server 
	return ""

