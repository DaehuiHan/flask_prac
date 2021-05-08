# flask prac

- 플라스크 시작코드
  from flask import Flask
  app = Flask(**name**)

  @app.route('/')
  def home():
  return 'This is Home!'

  if **name** == '**main**':  
   app.run('0.0.0.0',port=5000,debug=True)
