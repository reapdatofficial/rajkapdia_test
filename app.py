from flask import Flask
from weasyprint import HTML
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, this is mani test!'


HTML('https://render-rajkapdia-test.onrender.com').write_pdf('output.pdf')

if __name__ == '__main__':
    app.run()
