# Flask_Rest_API

Basic Flask API, using a dummy linear regression model (cf training folder)

Running on ubuntu server 18.04 VM.

### Flask/Gunicorn

#### Install/config/test

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

Structure

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

Install requirements

```
pip install -r ~Flask_Rest_API/flask_app/requirements.txt
```



Git Clone 

```bash
git config --global user.name="My Name"
git config --global user.email=My@email
git clone https://github.com/terman37/Flask_Rest_API.git
```

Run server

```bash
cd ~/Flask_Rest_API/flask_app/
gunicorn -w 1 -b 0.0.0.0:8000 wsgi:server
```



Query the API: (brower or postman...)

```
http://<serverIP>:8000/predict/?x=3.25
```

should return a value ;-)

```
http://<serverIP>:8000/
```

should return an amazing "Hello World" :-)



### Docker

Build the docker container 

from Dockerfile directory run: (**do not forget the dot at the end**)

```
docker build --tag myfirstflaskapi:v0 .
```

Check images installed

```
docker images
```

Run it: (bind port 80 to 8000 in container)

```
docker run -d -p 80:8000 myfirstflaskapi:v0
```

check in browser

```
localhost/predict/?x=8.65
```







### Tip

- clean docker images/volumes... (all but the ones running)

  ```
  docker system prune -a
  ```

  