FROM nvidia/cuda:12.2.2-base-ubuntu20.04    			
RUN apt update
RUN apt install -y tzdata
RUN apt install python3 ffmpeg python3-pip -y
WORKDIR /app 
COPY . . 
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
