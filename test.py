import requests
'''
test program for image comparison api
'''

images = {"url1": "http://wallpaperfx.com/view_image/beautiful-nature-view-1920x1080-wallpaper-781.jpg",
"url2" : "https://www.setaswall.com/wp-content/uploads/2017/06/Mountains-Nature-Forest-View-1920-x-1080-768x432.jpg"}
url = 'http://127.0.0.1:5000/compare'
key = "f4132df3-0628-4d80-9614-8545d52e6d71"

print(*requests.post(url,cookies ={'appkey':'f4132df3-0628-4d80-9614-8545d52e6d71'}, json=images))

