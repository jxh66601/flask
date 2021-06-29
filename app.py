from flask import Flask, send_file

app = Flask(__name__)
@app.route('/')
def index():
    #return 'Hello World'
    return send_file('a.jpg', mimetype='image/gif')
if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', port='5001')


