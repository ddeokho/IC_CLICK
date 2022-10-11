from pynput.mouse import Listener


def click(x,y, button, pressed) :
	if pressed:
		x = int(x)
		y = int(y)

		print('x='+str(x)+' y='+str(y))

with Listener(on_click = click) as Listener:
	Listener.join()

	
