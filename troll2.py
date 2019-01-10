# --- TYPE ---
# --- RACER ---
# ---  BOT  ---

import numpy as np
from PIL import ImageGrab
from PIL import Image
import pytesseract
import cv2
import time
from pynput.keyboard import Key, Controller
import random


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
keyboard = Controller()

def process_img(img):
    # gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply dilation and erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return img

screen = np.array(ImageGrab.grab(bbox=(340,500,1300,900)))
new_screen = process_img(screen)
cv2.imshow('window', new_screen)
if cv2.waitKey(25) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

text = pytesseract.image_to_string(new_screen)
text = text.replace('\n', ' ').replace('\r', '').replace('|', 'I').replace('[', '').replace(']', '').replace('‘', '\'')
print(text)
try:
    #begin = text.index('>')+1
    end = text.index('change display format')
    #text = text[begin:end]
    text = text[:end]
    print(text)
    time.sleep(1)
    for char in text:
        # to adjust WPM adjust var low and high: the higher the slower
        low = 35
        high = 45
        rand_delay = 0.001*(random.randrange(low,high,1))
        #print(rand_delay)
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(rand_delay)
except:
    print('RIP LOL')
        
