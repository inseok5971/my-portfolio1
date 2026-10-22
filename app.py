from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile_data = {
        "name": "정인석",
        "title": "아트적으로 코딩언어를 다룰 줄 아는 파이썬 전문가",
        "intro": "아트적으로 코딩언어를 다를 줄 아는 파이썬 전문가가 될거야!",
        "learning": ["파이썬", "네트워크", "자바", "자바스크립트"],
        "instagram": "@ebrio_jis_"
    }
    return render_template('index.html', data=profile_data)

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5007))
    app.run(host="0.0.0.0", port=port)