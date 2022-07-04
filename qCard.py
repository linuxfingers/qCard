import os
import pyqrcode
import png
from pyqrcode import QRCode

directory = "qCards"
parent_dir = "./"
path = os.path.join(parent_dir, directory)
isFile = os.path.isfile(path)

def initDir():
    directory = "qCards"
    parent_dir = "./"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)

def qCard():
    www = input("What URL do you want to put into a QR code? ")
    print("Okay, making", www, "into an SVG and PNG." )

    # gen QR code
    url = pyqrcode.create(www)

    # make svg and png
    url.svg(path+'/'+www+'.svg', scale = 8)
    url.png(path+'/'+www+'.png', scale = 6)

if isFile == True:
    initDir()
    qCard()
else:
    qCard()

