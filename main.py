from PIL import ImageGrab
from pynput import mouse

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    data=ImageGrab.grab()
    pixel=data.getpixel((x,y))
    print("pixel",pixel)
    data.close()
    if not pressed:
        # Stop listener
        return False

# listener = mouse.Listener(
#     on_click=on_click,
#     )
# listener.start()
with mouse.Listener(
        on_click=on_click,
       ) as listener:
    listener.join()
