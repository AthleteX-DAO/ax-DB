FROM python:3.10.6-slim

#add user group and add user to that group
#RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN apt update 

#creates work dir
WORKDIR /app

#copy python script to the container folder app
COPY GetNBAAthleteData.py /app/GetNBAAthleteData.py
COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN chmod +x /app/GetNBAAthleteData.py

#user is appuser
#USER appuser

ENTRYPOINT ["/app/GetNBAAthleteData.py"]

