FROM python:3.11-slim
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
COPY ./requirements.txt .
RUN pip install  --no-cache-dir "fastapi[standard]" 
RUN pip install  --no-cache-dir  -r ./requirements.txt 
COPY . .
ENV PYTHONPATH=/src
EXPOSE 8080
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]