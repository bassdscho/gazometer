from gpiozero import Button
from signal import pause

def read_old():
	return float(open("value", "r").read())

def write_absolute(val):
	open("value", "w+").write(str(round(val,3)))

locked = True
def seen_low():
	global locked
	locked = False
	print("seen low, unlocked!") 

def add_round():
	global locked
	if not locked:
		new_val = read_old() + 0.001
		write_absolute(new_val)
		locked = True
		print("add_round, new val: %s" % new_val)
	else:
		print("add_round: locked doing nothing!")

button = Button(2)

button.when_pressed = seen_low
button.when_released = add_round

pause()
