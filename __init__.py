from flask import Flask , request , abort
import json
import requests
from noti import _lineNotify , notifyFile ,lineNotify
import testcoor as au
import df as df
import remember as re
import status as st

Channel_access_token = '7pp8WnbhnsNT5+lk8Z8v2Lr/zlBBiLFDUCNp7+ojxltCIr+w3TvslebQPHL8QEzVA1vkHt1b6mtmQDW30r2m3nZdB9wIHdtDlJdwrUtfsVcbDEqJ4OSwvaD+jjUbZGnRT6m75fqTJA6QAneF9wv+mwdB04t89/1O/w1cDnyilFU='
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

app = Flask(__name__)

Command_List = ['Site ', 'Zoomin ', 'Zoomout ','Info ','Cell ','Initzoom','EnodeBID','ARH','NRS','AFS','CS ','DAS ']

@app.route('/')
def hello():
    return 'hello' , 200

@app.route('/webhook',methods = ['POST','GET'])
def webhook():
    if request.method == 'POST':
        status = st.Read_status()
        message = ''
        payload = request.json
        Message_Type = payload['events'] [0]['message']['type']
        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        if Message_Type == 'text' and status == 'Available':
            message = payload['events'][0]['message']['text']
            lenm = len(message)
            print(message)
            prev_message = re.Previous_Message()
            print(prev_message)
            for x in Command_List:
                if x in message:
                    re.New_Message(message)
                    break
                else:
                    re.New_Message(prev_message)
            if 'Info ' in prev_message:
                print('ddddd')
                for i in Command_List:
                    if i in message and i != 'Cell ':
                        st.Not_ok_status()
                        au.Endinfo()
                        st.Ok_status()
            if 'Cell ' in prev_message:
                print('ddddd')
                for i in Command_List:
                    if i in message and i != 'Cell ':
                        st.Not_ok_status()
                        au.Endinfo()
                        st.Ok_status()
            if 'Help' in message:
                notifyFile('help1.png',"")
                notifyFile('help2.png',"")
            if 'Site ' in message and lenm >= 5 :
                st.Not_ok_status()
                print('affirmative')
                Site_id = message[5:]
                Check = message[5]
                if Check in alphabet:
                    au.Mapclick()
                    au.findCoordinate(Site_id)
                    au.screenshot()
                    au.Savecrop('map')
                    notifyFile('map.png',Site_id)
                    st.Ok_status()
            if 'Zoomin ' in message and lenm >= 7:
                st.Not_ok_status()
                clicks = int(message[7:])
                for i in range (0,clicks):
                    au.ZoomIN()
                au.screenshot()
                for i in range (0,clicks):
                    au.ZoomOUT()
                au.Savecrop('map1')
                notifyFile('map1.png',message)
                st.Ok_status()
            if 'Zoomout ' in message and lenm >= 7:
                st.Not_ok_status()
                clicks = int(message[7:])
                for i in range (0,clicks):
                    au.ZoomOUT()
                au.screenshot()
                for i in range (0,clicks):
                    au.ZoomIN()
                au.Savecrop('map2')
                notifyFile('map2.png',message)
                st.Ok_status()
            if 'Info ' in message and lenm >= 5 :
                st.Not_ok_status()
                Site_id = message[5:]
                Check = message[5]
                if Check in alphabet:
                    au.slide()
                    au.ZoomIN()
                    au.ZoomIN()
                    au.Mapclick()
                    au.findCoordinate(Site_id)
                    au.GetSiteinfo()
                    au.screenshot()
                    au.Savecrop('info')
                    notifyFile('info.png',Site_id)
                    st.Ok_status()
            if 'Cell ' in message and lenm >= 5:
                st.Not_ok_status()
                Cell_number = int(message[5:])
                if Cell_number == 0 :
                    au.infoBegin()
                    au.screenshot()
                    au.Savecrop('info0')
                    au.endcellinfo()
                    notifyFile('info0.png',"")
                    st.Ok_status()
                else: 
                    au.GetSiteinfo()
                    au.GetCellinfo(Cell_number)
                    au.Savecellinfo()
                    au.endcellinfo()
                    notifyFile('info1.png',"")
                    notifyFile('info2.png',"")
                    st.Ok_status()
            if 'Endinfo' in message :
                au.closeinfo()
                au.ZoomOUT()
                au.ZoomOUT()
                au.slide()
            if 'Initzoom' in message:
                st.Not_ok_status()
                au.Mapclick()
                au.initZoom()
                st.Ok_status
            if 'EnodeBID ' in message and lenm >= 9:
                st.Not_ok_status()
                EnodeB_ID = message[9:]
                Site_id = df.enodeBIDseach(EnodeB_ID,'ExportLTE2125.csv')
                au.Mapclick()
                au.findCoordinate(Site_id)
                au.screenshot()
                au.Savecrop('map')
                notifyFile('map.png',Site_id)
                st.Ok_status()
        if Message_Type == 'text' and status == 'Unavailable':
            message = payload['events'][0]['message']['text']
            for i in Command_List:
                if i in message:
                    lineNotify('รอแปปนึง')
            if 'Statcheck' in message:
                a = st.Read_status()
                lineNotify(a)
        if Message_Type == 'location':
            prev_message = re.Previous_Message()
            print(prev_message)
            re.New_Message('')
            latitude = str(payload['events'][0]['message']['latitude'])
            longitude = str(payload['events'][0]['message']['longitude'])
            print('lat '+ latitude)
            print('long '+ longitude)
            if 'ARH' in prev_message and status == 'Available':
                st.Not_ok_status()
                au.Spatialclick()
                au.Insertsymbol()
                au.Selectsymbol()
                au.locateurself(longitude,latitude)
                au.Findsymbol()
                au.Findmark()
                au.screenshot()
                au.Savecrop('location')
                au.delsymbol()
                notifyFile('location.png','')
                st.Ok_status()
            if 'NRS' in prev_message:
                out = df.Get_nearest_site(latitude,longitude,'ExportLTE2125.csv')
                lineNotify(out)
            if 'AFS' in prev_message:
                out = df.Get_Angle_f_site(latitude,longitude,'ExportLTE2125.csv')[0]
                lineNotify(out)
            if 'CS ' in prev_message:
                Sys = prev_message[3:]
                out = df.Compare_angle(latitude,longitude,'ExportLTE2125.csv',Sys)
                lineNotify(out)
            if 'DAS ' in prev_message:
                site_id  = prev_message[4:]
                out = df.Distance_Angle_f_site(latitude,longitude,site_id,'ExportLTE2125.csv')
                lineNotify(out)
            if 'CVC ' in prev_message:
                site_id  = prev_message[4:]
                out = df.Cell_in_target(latitude,longitude,site_id,'ExportLTE2125.csv','Data_Base.csv')
                lineNotify(out)
            #print(payload)
        return request.json, 200
    elif request.method == 'GET':
        return 'This is method GET',200
    else:
        abort(400)

    




def ReplyMessage(Reply_token, Message, Line_Acees_Token,Type_of_message):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization':Authorization
    }
    if Type_of_message == 1:
        data = {"replyToken":Reply_token,
        "messages":[{
        "type":"text",
        "text":Message
        }]
        }
    else:
        data = {
        "replyToken":Reply_token,
        "messages":[{
        "type":"image",
        "originalContentUrl":Message,
        "previewImageUrl":Message
        }]
        }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200


    
