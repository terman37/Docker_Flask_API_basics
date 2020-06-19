# Flask_Rest_API

On ubuntu server 18.04 VM



Install python

```bash
sudo apt install python3.7
sudo apt install python-pip
sudo apt install python3.7-venv
```

upgrade pip

```bash
python -m pip install --upgrade pip
```

structure

```bash
mkdir venvs
```



Create venv

```bash
python3.7 -m venv ~/venvs/flask_env
```

Activate venv windows

```bash
source ~/venvs/flask_env/bin/activate
```



Git Clone 

```bash
git config --global user.name="My Name"
git config --global user.email=My@email
git clone https://github.com/terman37/Flask_Rest_API.git
```

or create 2 files in ~/flask_app/

App.py:

```python
from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'hello world!'
```

wsgi.pi

```python
from app import server

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=8000)
```



install flask (in correct venv)

```bash
pip install flask
pip install gunicorn
```

run server

```bash
cd ~/flask_app/
gunicorn -w 1 -b 0.0.0.0:8000 wsgi:server
```

