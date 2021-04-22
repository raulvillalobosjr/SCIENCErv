def convert(minutes):
	return minutes*60

def how_many_seconds(hours):
	return hours*60*60

def calc_age(age):
	return age*365

def circuit_power(voltage, current):
	return voltage*current

def convertToSecs(hours, minutes):
	return (hours*60*60)+(minutes*60)

def frames(minutes, fps):
	return fps*60*minutes

def calculate_fuel(n):
	if n<10:
		return 100
	else:
		return n*10

def area(h, w):
	if h <= 0 or w <=0:
		return -1
	else:
		return h*w

inches_to_feet = lambda inches: math.floor(inches/12)
