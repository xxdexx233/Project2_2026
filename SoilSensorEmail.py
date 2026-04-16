#import the time module
import time

#get the current time in seconds since the epoch
seconds = time.time()

result =time.localtime(seconds)

#Set the LastValue variable. Will compare to Current Hour Value
#lastValue = result.tm_hour + 8
startTime = 8
lastValue = startTime

while(True):
	result = time.localtime(seconds)
	Current_Value = result.tm_hour +8
	#Compare Time to send email
	if (lastValue == Currrent_Value):
	print("")
	else:
		difference = Current_Value - lastValue
		if(different >4):
			#remain for function
			lastValue = Current_Value
		else:
			print("")
