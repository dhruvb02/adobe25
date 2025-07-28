# ✅ Start with Python base image
FROM python:3.9-slim-buster

# ✅ Set workdir
WORKDIR /app

# ✅ Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy code
COPY . .

# ✅ Default command — this is the missing part!
CMD ["python", "run.py"]
