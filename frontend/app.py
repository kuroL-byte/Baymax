from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    try:
        subprocess.Popen(["python", r"C:\Users\Tushar Kulkarni\Desktop\voice assistant gg\Baymax\Baymax\backend\final_backend2.py"])
        return 'Backend started!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
