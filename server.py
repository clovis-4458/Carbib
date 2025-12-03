from waitress import serve
from project2.wsgi import application  # your project name here

if __name__ == "__main__":
    serve(application, host="0.0.0.0", port=8000)
