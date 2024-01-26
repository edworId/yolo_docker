FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime

WORKDIR /app
ENV FLASK_APP app.py

COPY . .

RUN apt-get update && apt-get upgrade -y
RUN apt-get install curl -y
RUN apt-get install libgl1 -y
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN pip3 install flask
RUN pip3 install opencv-python
RUN pip3 install pandas
RUN pip3 install ultralytics

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
