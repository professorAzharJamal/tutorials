def is_cold(temperature):
	return temperature < 18

def heat_on(is_cold):
	if is_cold:
		return "Turn the heater on"
	else:
		return "Turn the heater off"

#Set the current temperature
current_temp = 15

#perform action
action = heat_on(is_cold(current_temp))

#print the outcome
print(action)