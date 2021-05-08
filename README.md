# flask prac

- Flask 프레임워크: 서버를 구동 시켜주는 편한 코드 모음.

  - 통상적으로 프레임워크는 하나를 쓰고 그 안에서 원하는 만큼의 라이브러리를 가져다 쓸 수 있다.

- app.py의 return 부분에 html을 작성하면 그대로 브라우져에 나타나게 된다. 하지만 매우 비효율 적이기 때문에 app.py 상단에 Flask를 import하는 부분에 render_template을 같이 import해주고 페이지의 리턴 부분에 render_template('') 이렇게 적어주고, 따움표 안에는 templates 폴더에 저장된 html파일 이름을 확장자 명과 함께 적어주면 된다.
