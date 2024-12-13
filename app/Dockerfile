# Rasmni tanlash (Python versiyasi)
FROM python:3.11-slim

# Loyihaga oid papkalarni belgilash
WORKDIR /app

# Kutubxonalarni o‘rnatish
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Loyiha fayllarini konteynerga ko‘chirish
COPY . /app/

# Statik fayllarni yig‘ish
RUN python manage.py collectstatic --noinput

# Portni ochish
EXPOSE 8000

# Django serverni ishga tushirish
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
