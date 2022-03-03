
from pynput import keyboard, mouse
from pynput.keyboard import Key, Controller
import threading

"""
keyboard = Controller()

# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
keyboard.press('a')
keyboard.release('a')

# Type two upper case As
keyboard.press('A')
keyboard.release('A')
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')

# Type 'Hello World' using the shortcut type method
keyboard.type('Hello World')

"""

delay = 0.001
button = "e"
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

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