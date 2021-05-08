# 플라스크 시작코드
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '나의 첫 서버!!'

@app.route('/mypage')
def mypage():
   return 'my Page'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)