'''
name: Colton Gering
email: geringcolton@gmail.com
API to compare images
'''
from flask import Flask,request
from PIL import Image,ImageChops,ImageStat
import requests

app = Flask(__name__)
appkey = "f4132df3-0628-4d80-9614-8545d52e6d71"


@app.route('/compare',methods=['POST','GET'])
def handleComparison():
    providedKey = request.cookies['appkey']
    if providedKey == appkey:
        u1 = request.json['url1']
        u2 = request.json['url2']
        return compareImages(u1,u2)
    else:
        return 'Key not matching'


def compareImages(url1,url2):
    i1 = Image.open(requests.get(url1,stream=True).raw)
    i2 = Image.open(requests.get(url2, stream=True).raw)

    #difference as image
    difference = ImageChops.difference(i1,i2)
    #make the image a stat object
    difference_stat = ImageStat.Stat(difference)
    #get list of average for each band
    avg_difference = difference_stat.mean
    #calculate averages to a single percentage
    res = round(sum(avg_difference) / len(avg_difference), 2)
    return str(res) + "%"


if __name__ == '__main__':
    app.run()



