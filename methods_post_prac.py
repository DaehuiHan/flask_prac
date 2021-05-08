# get 요청 API 코드
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# 위에 jsonify, request 추가

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)


=================
# post 요청 확인 ajax 코드
$.ajax({
    type: "POST",
    url: "/test",
    data: { title_give:'봄날은간다' },
    success: function(response){
       console.log(response)
    }
  })
