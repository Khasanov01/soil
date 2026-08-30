# Soil Project

Create soil application to learn FAST API basics

## Introduction & learninng path

- Asynchronous vs Synchronous Programming
- ASGI Frameworks (routing, middleware, response)
  Starlette > FastAPI
- FastAPI focus on Validation, Docs and Development Process
- Conda virtual Environment


## Project Run Sources

- Install conda and create virtual  environment

```
brew install miniconda
conda --version
conda env list

conda create --name soil python=3.11.0
conda create --name soil python=3.11.0 numpy
conda activate soil
conda deactivate

pip install -r requirements.txt
pip  install pillow
pip freeze > requirements.txt
```

-Install and Run Project

```
pip install fastapi[all]
pip freeze > requirements.txt
```

```
for Development:
fastapi dev main.py
fastapi dev main.py --port 5000
```