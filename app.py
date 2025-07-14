from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
      <head><title>My Details</title></head>
      <body>
        <h1>Harshal Patil</h1>
        <p><strong>Email:</strong> hvpatil9@gmail.com</p>
        <p><strong>Location:</strong> India</p>
        <p><strong>Learning:</strong> DevOps, AWS, Docker</p>
      </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
