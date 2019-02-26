#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytesseract
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
#engine.setProperty('rate','hindi')

from PIL import Image, ImageEnhance, ImageFilter
sound = engine.getProperty('voices')
#engine.setProperty('voice',sound[2].id)  #male voice
engine.setProperty('voice','english+f2')

#scale = 1
#delta = 0
#ddepth = cv2.CV_16S
#
#gray=cv2.imread("voice.png")
#cv2.namedWindow("Main")
#cv2.imshow("Main", gray)
#### trim the edges
#cut_offset=23
#gray=gray[cut_offset:-cut_offset,cut_offset:-cut_offset]
#
#### convert to gray color
#gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
#
#### edge enhancing by Sobeling
## Gradient-X
#grad_x = cv2.Sobel(gray,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
##grad_x = cv2.Scharr(gray,ddepth,1,0)
#
## Gradient-Y
#grad_y = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
##grad_y = cv2.Scharr(gray,ddepth,0,1)
#
#abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
#abs_grad_y = cv2.convertScaleAbs(grad_y)
#gray = cv2.addWeighted(abs_grad_x,0.4,abs_grad_y,0.4,0)
#
#### Bluring
#image1 = cv2.medianBlur(gray,5) 
#image1[image1 < 50]= 255
#image1 = cv2.GaussianBlur(image1,(31,13),0)     
#color_offset=220
#image1[image1 >= color_offset]= 255  
#image1[image1 < color_offset ] = 0      #black
#
##### Insert White Border
#offset=30
#height,width = image1.shape
#image1=cv2.copyMakeBorder(image1,offset,offset,offset,offset,cv2.BORDER_CONSTANT,value=(255,255,255)) 
#cv2.namedWindow("Test")
#cv2.imshow("Test", image1)
#cv2.imwrite("an91cut_decoded.jpg",image1)
#'''
#### tesseract OCR
#api = pytesseract.TessBaseAPI()
#api.Init(".","eng",pytesseract.OEM_DEFAULT)
#api.SetPageSegMode(tesseract.PSM_AUTO)
##as suggested by zdenko podobny <zdenop@gmail.com>, 
##using PSM_SINGLE_BLOCK will be more reliable for ocr-ing a line of word. 
##api.SetPageSegMode(tesseract.PSM_SINGLE_BLOCK)
#height1,width1 = image1.shape
#channel1=1
#image = cv.CreateImageHeader((width1,height1), cv.IPL_DEPTH_8U, channel1)
#cv.SetData(image, image1.tostring(),image1.dtype.itemsize * channel1 * (width1))
#tesseract.SetCvImage(image,api)
#text=api.GetUTF8Text()
#conf=api.MeanTextConf()
#image=None
#
#
#'''



#import argparse
#import cv2
# 
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())
# 
#im = cv2.imread(args["image"])
# 
#cv2.imshow("image", im)
#cv2.waitKey(0)


im = Image.open("voice.png") # the second one 
#im = im.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)
#im = im.convert('1')
#im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('voice.png'))
print(text)
print("...............")
#print("Ocred Text: %s"%text)
engine.say(text)
engine.runAndWait()
#print("Cofidence Level: %d %%"%conf)
#cv2.waitKey(0)
#cv2.destroyWindow("Test")
#cv2.destroyWindow("Main")
#api.End()


'''

#To check how the volume , voice, rate changes accrodingly


import pyttsx3
voiceEngine = pyttsx3.init()
 
rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')
 
print(rate)
print(volume)
print(voice)
 
newVoiceRate = 50
while newVoiceRate <= 300:
    voiceEngine.setProperty('rate', newVoiceRate)
    voiceEngine.say('Testing different voice rates.')
    voiceEngine.runAndWait()
    newVoiceRate = newVoiceRate+50
 
voiceEngine.setProperty('rate', 125)
 
newVolume = 0.1
while newVolume <= 1:
    voiceEngine.setProperty('volume', newVolume)
    voiceEngine.say('Testing different voice volumes.')
    voiceEngine.runAndWait()
    newVolume = newVolume+0.3
    
 '''
    
'''
************************************************

*************************************************
'''
'''
#Speaking text

import pyttsx3
engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#Listening for events

import pyttsx3
def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#Interrupting an utterance

import pyttsx3
def onWord(name, location, length):
   print('word', name, location, length)
   if location > 10:
      engine.stop()
engine = pyttsx3.init()
engine.connect('started-word', onWord)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#Changing voices

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#Changing speech rate

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#Changing volume

engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#Running a driver event loop

engine = pyttsx3.init()
def onStart(name):
   print('starting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)
   if name == 'fox':
      engine.say('What a lazy dog!', 'dog')
   elif name == 'dog':
      engine.endLoop()
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
engine.startLoop()

#Using an external event loop

engine = pyttsx3.init()
engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
engine.startLoop(False)
# engine.iterate() must be called inside externalLoop()
externalLoop()
engine.endLoop()
'''