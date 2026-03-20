FROM python:3.9-alpine AS builder
WORKDIR /app
RUN apk add --no-cache gcc musl-dev libffi-dev
COPY requirements.txt .
RUN  pip install --no-cache-dir --prefix=/install -r requirements.txt
FROM python:3.9-alpine
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=builder /install /usr/local
COPY  . .
RUN chown -R appuser:appgroup /app
USER appuser
CMD  ["python","app.py"]

