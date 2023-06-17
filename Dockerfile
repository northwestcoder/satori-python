FROM jupyter/datascience-notebook:latest

# Install production dependencies.
RUN pip install --upgrade git+https://github.com/northwestcoder/satoripython

COPY HelloWorld.ipynb /home/jovyan/HelloWorld.ipynb
