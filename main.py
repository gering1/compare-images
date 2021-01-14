'''
name: Colton Gering
email: geringcolton@gmail.com
API to compare images
'''
from typing import Optional
from fastapi import FastAPI
from flask import Flask,request
from PIL import Image,ImageChops,ImageStat
import requests
import json
appkey = "kmrhn74zgzcq4nqb"

app = FastAPI()

@app.post("/compare")
def handleComparison(url1:str,url2:str,key:str):

    providedKey = key
    if providedKey == appkey:
        u1 = url1
        u2 = url2
        return json.dumps(compareImages(u1,u2))
    else:
        return json.dumps('Key not matching')

    
def compareImages(url1:str,url2:str):
    i1 = Image.open(requests.get(url1,stream=True).raw)

    i2 = Image.open(requests.get(url2, stream=True).raw)
    print(i1,i2)
    print(i1.getbands(),i2.getbands())
   # return ImageState.StatImageChops.difference(i1,i2))
    #difference as image
    print(i1,i2)
    difference = ImageChops.difference(i1,i2)

    '''
    #make the image a stat object
    difference_stat = ImageStat.Stat(difference)
    #get list of average for each band
    avg_difference = difference_stat.mean
    #calculate averages to a single percentage
    res = round(sum(avg_difference) / len(avg_difference), 2)
        return str(res) + "%"

    '''
    return difference
