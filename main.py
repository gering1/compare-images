'''
name: Colton Gering
email: geringcolton@gmail.com
API to compare images
'''
from fastapi import FastAPI
from PIL import Image,ImageChops
import requests
import imgcompare

import json
appkey = "kmrhn74zgzcq4nqb"
app = FastAPI()

@app.post("/compare")
def handleComparison(url1:str,url2:str,key:str):
    '''
    check if api is correct and accept query params
    :param url1: first image url
    :param url2: second image url
    :param key: api key
    :return: image similarity percentage
    '''
    providedKey = key
    if providedKey == appkey:
        u1 = url1
        u2 = url2
        return json.dumps(compareImages(u1,u2))
    else:
        return json.dumps('Key not matching')

    
def compareImages(url1:str,url2:str):
    '''
    :param url1: first image url
    :param url2: second image url
    :return: image similarity percentage
    '''
    i1 = Image.open(requests.get(url1,stream=True).raw)
    i2 = Image.open(requests.get(url2, stream=True).raw)

    #convert images to same type
    if i1.getbands() != i2.getbands():
        i1 = i1.convert('RGB')
        i2 = i2.convert('RGB')

    #resize to same size
    if i1.size != i2.size:
        i1,i2 = resizeImages(i1,i2)

    diff= ImageChops.difference(i1,i2)

    #show a single of difference merged into one image
    if diff.getbbox():
        diff.show()
    return round(imgcompare.image_diff_percent(i1,i2),2)

def resizeImages(i1:Image,i2:Image):
    '''
    Resizes images to the minimum x and minimum y values between the images
    :param i1:  first image
    :param i2: second image
    :return: first and second image resized as tuple
    '''
    i1_x, i1_y = i1.size[0], i1.size[1]
    i2_x, i2_y = i2.size[0], i2.size[1]
    min_x = min(i1_x, i2_x)
    min_y = min(i1_y, i2_y)
    new_size = (min_x,min_y)
    i1 = i1.resize(new_size)
    i2 = i2.resize(new_size)
    return (i1,i2)



