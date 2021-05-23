# Pull base image
FROM python:3.8
#USER root
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code/
# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev
COPY . /code/
EXPOSE 3000
CMD ["python", "main.py"]