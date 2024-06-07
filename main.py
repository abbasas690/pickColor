from PIL import ImageGrab
from pynput import mouse
import colorsys

def rgb_to_hex(pixel):
    r,g,b = pixel
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



pixel=[]
def main():
    with mouse.Events() as e:
        for x in e:
            try:
                if x.button == mouse.Button.left :
                    data=ImageGrab.grab()
                    pixel=data.getpixel((x.x,x.y))
                if x.button == mouse.Button.right:                
                    print(f"rgb:{pixel} hex:{rgb_to_hex(pixel=pixel)}")
                    break
                
            except: pass
            finally:
                data=ImageGrab.grab()
                pixel=data.getpixel((x.x,x.y))

if __name__ == "__main__":
    main()