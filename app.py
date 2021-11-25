"""
Deploy Flask App in IIS Server
"""
from flask import Flask
app = Flask(__name__)

import os
import pypandoc

#pandoc_path = pypandoc.get_pandoc_path()
#print(pandoc_path)

#os.environ.setdefault('PYPANDOC_PANDOC','C:\\inetpub\\wwwroot\\Nov_25\\venv\\lib\\site-packages\\pypandoc\\files\\pandoc.exe')
#os.environ.setdefault('PYPANDOC_PANDOC','\\venv\\lib\\site-packages\\pypandoc\\files\\pandoc')

os.environ.setdefault('PYPANDOC_PANDOC','C:\\Pandoc\\pandoc.exe')

@app.route("/")
def home():
    return "Hello, This is the Flask App on IIS Server."

@app.route('/rtf')
def hello_world():
    #print("BASE ADDRESS : ",os.path.abspath(os.path.dirname(__file__)))
    #path = os.environ.get("PYPANDOC_PANDOC")
    #path2 = os.environ.get("DriverData")
    #print("PATH :",path)
    note = '<p>Test</p><h1><strong>testw</strong></h1>'
    rtf_string = pypandoc.convert_text(note, 'rtf', format='html')
    return f"RTF conversion succeded"

if __name__ == "__main__":
    app.run(debug=True)
