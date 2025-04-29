# Rasmni tanlash
FROM python:3.11-slim

# Ishlash uchun katalogni belgilash
WORKDIR /app



# Zarur fayllarni nusxalash
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani nusxalash
COPY . /app/

# Django static fayllarini yig'ish
RUN python manage.py collectstatic --noinput

# Portni ochish
EXPOSE 8000

# Loyihani ishga tushirish
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
