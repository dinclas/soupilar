FROM python:3.12.3

WORKDIR /usr/src/soupilar
COPY . /usr/src/soupilar

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
