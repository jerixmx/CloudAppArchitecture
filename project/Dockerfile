# syntax=docker/dockerfile:1
FROM python:2.7
LABEL description="TechTrends Website" \
    version="1.0.0"
# set docker image working directory
WORKDIR /app

# initialize python dependencies
COPY ./techtrends/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy files in techtrends to image working directory
ADD ./techtrends .
EXPOSE 3111
RUN python init_db.py
CMD python app.py