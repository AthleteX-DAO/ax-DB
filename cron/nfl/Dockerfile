FROM python:3.10.6-slim

#add user group and add user to that group
#RUN addgroup -S appgroup && adduser -S appuser -G appgroup

RUN apt update 

#creates work dir
WORKDIR /app

#copy python script to the container folder app
COPY GetNFLAthleteData.py /app/GetNFLAthleteData.py
COPY requirements.txt /app/

RUN pip install -r requirements.txt

RUN chmod +x /app/GetNFLAthleteData.py

#user is appuser
#USER appuser

ENTRYPOINT ["/app/GetNFLAthleteData.py"]

