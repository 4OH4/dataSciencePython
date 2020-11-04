# datascience-jupyter
# Lightweight data science Docker container for efficient working with Jupyter Lab

#FROM jupyter/minimal-notebook
#FROM jupyter/scipy-notebook
FROM jupyter/datascience-notebook
#FROM jupyter/tensorflow-notebook
#FROM jupyter/pyspark-notebook
MAINTAINER 4oh4

USER root

WORKDIR "/"

# Install dependencies:

# Option 1: use Conda environment.yml file
#ADD ./environment.yml /
#RUN conda env update -f environment.yml

# Option 2: use pip requirements.txt file (simpler)
ADD ./requirements.txt /
RUN pip install -r requirements.txt

# Switch back to the unprivileged user
USER jovyan