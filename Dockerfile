# ۱. پایه سیستم‌عامل پایتون
FROM python:3.12-slim

# ۲. متغیرهای محیطی
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ۳. پوشه کاری
WORKDIR /app

# ۴. نصب ابزارهای سیستم‌عامل + نصب خودکار Node.js و NPM
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# ۵. کپی و نصب نیازمندی‌های پایتون (بک‌اند)
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ۶. کپی و نصب نیازمندی‌های NPM (فرانت‌اند)
# فرض می‌کنیم پوشه فرانت‌اَند شما نامش frontend است و فایل package.json داخل آن است
COPY frontend/package*.json /app/frontend/
RUN cd /app/frontend && npm install

# ۷. کپی کردن کل پروژه
COPY . /app/

# ۸. باز کردن پورت جنگو
EXPOSE 8000