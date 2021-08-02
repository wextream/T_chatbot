def lineNotify(message):
    payload = {'message':message}
    return _lineNotify(payload)

def notifyFile(filename,Site_id):
    file = {'imageFile':open(filename,'rb')}
    if filename == 'map.png':
        payload = {'message':"สภาพแวดล้อมของไซต์ "+ Site_id}
    if filename ==  'info.png':
        payload = {'message':"องค์ประกอบของไซต์ "+ Site_id}
    if filename == 'info0.png':
        payload = {'message':"ข้อมูลของไซต์ "+ Site_id}
    if filename == 'info1.png':
        payload = {'message':"ข้อมูลของcell "+ Site_id}
    if filename == 'info2.png':
        payload = {'message':"ข้อมูลของcell(ต่อ) "+ Site_id}
    if 'help' in filename:
        payload = {'message':"How to use"+ Site_id}
    if filename == 'map1.png':
        payload = {'message':Site_id}
    if filename == 'map2.png':
        payload = {'message':Site_id}
    if filename == 'location.png':
        payload = {'message': "ไซต์รอบๆท่าน"+Site_id}
    return _lineNotify(payload,file)

def notifyPicture(url):
    payload = {'message':" ",'imageThumbnail':url,'imageFullsize':url}
    return _lineNotify(payload)

def notifySticker(stickerID,stickerPackageID):
    payload = {'message':" ",'stickerPackageId':stickerPackageID,'stickerId':stickerID}
    return _lineNotify(payload)

def _lineNotify(payload,file=None):
    import requests
    token = 'BTXuRMFEQerRPwxbrsKrCmAB9RuCOfHqJpc8EM4TAQd'
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization':'Bearer '+ token}
    return requests.post(url, headers=headers , data = payload, files=file)


