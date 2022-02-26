import math
import pynput 
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='w')


#I like Python



#auto clicker that gives you the optiont oeither spam clicks, text, scroll. It has a terminal to ask what you want to spam and more specificallt what mous you want to click right or left. 
print("Alex's Auto Input \n (1) AutoClicker \n (2) AutoScroll \n (3) AutoType")
option_1 = int(input("What would you like to choose?: "))

def error():
	print("Something went wrong please run this software again")

if option_1 == 1:
	print("(1) Display screen ration for 20 seconds and input exact coordinates \n (2) Choose position with click of button ")
	opC = int(input("Choose how to continue: "))
	#Option Clicker

	if opC == 1:
		print("alright then")

	elif opC == 2:
		print("Press s to stop/start it and e to stop the whole program")

		class ClickMouse(threading.Thread):
			def __init__(self, delay, button):
				super(ClickMouse, self).__init__()
				self.delay = delay
				self.button = button
				self.running = False
				self.program_running = True

			def start_clicking(self):
				self.running = True

			def stop_clicking(self):
				self.running = False

			def exit(self):
				self.stop_clicking()
				self.program_running = False

			def run(self):
				while self.program_running:
					while self.running:
						mouse.click(self.button)
						time.sleep(self.delay)
					time.sleep(0.1)


		mouse = Controller()
		click_thread = ClickMouse(delay, button)
		click_thread.start()


		def on_press(key):
			if key == start_stop_key:
				if click_thread.running:
					click_thread.stop_clicking()
				else:
					click_thread.start_clicking()
			elif key == exit_key:
				click_thread.exit()
				listener.stop()


		with Listener(on_press=on_press) as listener:
			listener.join()
	else:
		error()


elif option_1 == "2":
	print("How Do You want to scroll? ")


elif option_1 == "3":
	print("What do you want to type? ")

else:
	error()
