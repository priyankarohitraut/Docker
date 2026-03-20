 Project Overview

This is a simple Flask-based web application containerized using Docker.
It connects to:

 PostgreSQL (Database)

 Redis (Cache)

The project demonstrates a multi-container architecture using Docker Compose.

 Architecture

User → Flask App → PostgreSQL
         → Redis

 Features

Flask API backend

PostgreSQL database integration

Redis caching

Docker multi-stage build

Docker Compose orchestration

Healthchecks and environment variables

 Docker Hub Image

Pull the image:

docker pull yourusername/devops-flask-app:v1
 Run with Docker Compose
1. Clone the repository
git clone <your-repo-url>
cd devops-project
2. Start services
docker compose up -d --build
 Access the App

Home: http://localhost:5000

DB Test: http://localhost:5000/db

Cache Test: http://localhost:5000/cache

 Environment Variables

Create a .env file:

POSTGRES_DB=mydb
POSTGRES_USER=user
POSTGRES_PASSWORD=password
 Useful Commands
docker compose ps
docker compose logs -f
docker compose down
 Tech Stack

Python (Flask)

PostgreSQL

Redis

Docker & Docker Compose

 Learning Outcome

Containerization of applications

Multi-service architecture

Docker image optimization

Networking, volumes, and healthchecks

‍ Author

priyanka 
