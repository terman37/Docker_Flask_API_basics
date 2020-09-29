

## Python

### Install Python

- from https://www.python.org/downloads/



## Virtual Environments

- Create

  ```
  python -m venv path\to\env
  ```

- Activate

  ```
  path\to\env\Scripts\activate.bat
  ```

- Deactivate

  ```
  path\to\env\Scripts\deactivate.bat
  ```



## Jupyter

### Install Jupyter (not in env)

```
pip install jupyter-lab
```

### Default Startup Folder

- generate config file

  ```
  jupyter notebook –generate-config
  ```

- uncomment / modify in %USERPROFILE%/.jupyter/jupyter_notebook_config.py

  ```
  #c.NotebookApp.notebook_dir = ''
  ```

### Install IPyKernel (for each env)

```
pip install ipykernel
```

- add environment to use it in Jupyter

  ```
  python -m ipykernel install --user --name=display_name
  ```

- list existing env

  ```
  jupyter kernelspec list
  ```

- remove env

  ```
  jupyter kernelspec uninstall myenv
  ```



## Docker

Make it run on Docker:

### Build the docker container 

from Dockerfile directory run: (**do not forget the dot at the end**)

```bash
docker build --tag myfirstflaskapi:v0 .
```

Check images installed

```bash
docker images
```

Run it: (bind port 80 to 8000 in container)

```bash
docker run -d -p 80:8000 myfirstflaskapi:v0
```

check in browser

```
localhost/predictln/?x=8.65
```



### Tip

- clean docker images/volumes... (all but the ones running)

  ```bash
  docker system prune -a
  ```

  