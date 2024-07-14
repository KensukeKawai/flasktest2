import requests

requrl_local = 'http://localhost:5000/upload'               # ローカルホストで試す場合はコレ
requrl_server = 'https://flasktest-qvzx.onrender.com'       # RenderサーバーにReqestする場合はコレ

def datareq(getdata):
    data = {
        'roll': getdata[0],
        'pitch': getdata[1],
        'yaw': getdata[2]
    }
    response = requests.post(requrl_local, json=data)
    print(response.status_code) # 200:Success、4**,5**:Failed,301:Redirect
    # http://localhost:5000
    # ↑=http://127.0.0.1:5000/