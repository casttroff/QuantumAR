from cfg import create_app
# from flask_cors import CORS

app = create_app()
# CORS(app)

@app.route('/index')
def index():
    return [{"members": ["member1", "member2", "member3"]}]


if __name__ == "__main__":
    app.run(debug=True, port="5000")
