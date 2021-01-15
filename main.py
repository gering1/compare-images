'''
name: Colton Gering
email: geringcolton@gmail.com
API to compare images
'''
from fastapi import FastAPI
from PIL import Image
import requests
import imgcompare

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
    if i1.size != i2.size or i1.getbands() != i2.getbands():
        return 'images not compatible'

    return imgcompare.image_diff_percent(i1,i2)



