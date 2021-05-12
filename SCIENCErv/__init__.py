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

def leap_year(year):
	if year%100 ==0 and year%400 == 0:
		return True
	elif year%100 ==0 and year%400 != 0:
		return False
	elif year%4 == 0:
		return True
	else:
		return False

def pos_com(num):
	return 2**num

def weight_allowed(car, p, max_weight):
	return (car+sum(p))<(max_weight*2.205)

def stack_boxes(n):
	if n<=0:
		return n
	else:
		return n*n

def km_to_miles(kilometers):
	return round((kilometers * 0.621371), 5)

def defangIPaddr(address):
    defa=[]
    for i in address:
        if i == ".":
            defa.append("[.]")
        else:
            defa.append(i)
    return "".join(defa)
