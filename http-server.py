
# serve text variable to the web by web server under port 5000
def start_web_server():
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def home():
        html = '''
        <html>
        <head>
            <title>My Web Page</title>
        </head>
        <body>
            <h1>Welcome to My Web Page</h1>
            <p>I am Timur</p>
        </body>
        </html>
        '''
        return html

    app.run(port=5000)

start_web_server()
