from flask import Flask 
import os
import datetime
import subprocess
app = Flask(__name__)
@app.route('/')
def home():
    return "home"
@app.route('/htop')
def htop():
    name = "Sumit shakya"
    username = os.getenv("USER" , "codespace")
    server_time= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        top_output = subprocess.check_output("top -bn1 | head -20", shell=True , text = True)
    except exception as e:
        top_output = str(e)

    return f"""
    <pre>
    Name:{name}
    user:{username}
    server Time (IST):{server_time}
    TOP output:
    {top_output}
    </pre>
    """
if __name__=='__main__':
    app.run(host='0.0.0.0' , port=5000,debug=True)
