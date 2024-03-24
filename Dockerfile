FROM python:3.11
WORKDIR /app
COPY requiments.txt ./
RUN pip install --no-cache-dir -r requiments.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
