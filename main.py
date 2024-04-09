from PIL import ImageGrab


data=ImageGrab.grab()

data.save("shot.png")
data.close()