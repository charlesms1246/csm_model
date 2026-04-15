from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, world from Flask on Azure!"

if __name__ == "__main__":
    app.run()
