# Task Manager – Cloud & DevOps Learning Project

A full-stack Task Manager application built with **React, FastAPI, and PostgreSQL**, with a focus on learning and implementing practical **Cloud Engineering and DevOps** concepts.

The project provides a platform for managing tasks while exploring containerization, database management, application deployment, and infrastructure automation.

## Project Overview

The Task Manager application allows users to create, view, update, delete, search, and filter tasks through a web-based interface.

Beyond application development, this project serves as a practical learning environment for understanding how modern applications are developed, containerized, connected, and managed using DevOps tools and practices.

## Technology Stack

### Frontend
- React
- JavaScript
- Vite
- Nginx

### Backend
- Python
- FastAPI
- SQLAlchemy
- REST API

### Database
- PostgreSQL

### Cloud & DevOps
- Docker
- Docker Compose
- Linux (Ubuntu)
- Git
- GitHub
- Docker Volumes
- Container Networking

## Project Architecture

The application consists of three main services:

1. **Frontend:** React application served using Nginx.
2. **Backend:** FastAPI application responsible for business logic and REST API endpoints.
3. **Database:** PostgreSQL database responsible for persistent task storage.

Docker Compose manages the services and their communication.

```text
                  USER
                    |
                    v
             React Frontend
                (Nginx)
              Port: 5173
                    |
                    v
              FastAPI Backend
               Port: 8000
                    |
                    v
                PostgreSQL
               Port: 5432
                    |
                    v
              Persistent Volume
```

## Features

- Create new tasks.
- Retrieve and display tasks.
- Update existing tasks.
- Delete tasks.
- Search and filter tasks.
- Display task statistics.
- RESTful API architecture.
- PostgreSQL database integration.
- Persistent database storage using Docker volumes.
- Multi-container application management using Docker Compose.

## Project Structure

```text
task_manager_devops/
│
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── requirements.txt
│   ├── create_tables.py
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── ...
│   │
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── package.json
│   └── ...
│
├── docs/
│
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Git
- Docker
- Docker Compose
- A web browser

### 1. Clone the Repository

```bash
git clone https://github.com/Nolan550/task_manager_devops.git
```

Navigate into the project directory:

```bash
cd task_manager_devops
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
DB_NAME=task_manager_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
```

Replace `your_password` with your own PostgreSQL password.

**Important:** Never commit your `.env` file or expose database credentials publicly.

### 3. Build and Start the Application

Run:

```bash
docker compose up --build -d
```

This command builds the application images and starts the frontend, backend, and database containers in the background.

### 4. Check Container Status

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs
```

View logs for an individual service:

```bash
docker compose logs backend
```

### 5. Access the Application

| Service | URL |
|---|---|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| API Documentation | http://localhost:8000/docs |

## Database Management

The application uses PostgreSQL for persistent task storage.

The database runs inside a Docker container and uses a Docker named volume to preserve data across container restarts and recreation.

Initialize the database tables:

```bash
docker compose exec backend python create_tables.py
```

Connect to the PostgreSQL container:

```bash
docker compose exec db psql -U postgres -d task_manager_db
```

List database tables:

```sql
\dt
```

Exit PostgreSQL:

```sql
\q
```

## Docker Commands

Useful commands for managing the application:

| Command | Description |
|---|---|
| `docker compose up -d` | Start all services |
| `docker compose up --build -d` | Rebuild and start services |
| `docker compose ps` | Check container status |
| `docker compose logs` | View service logs |
| `docker compose stop` | Stop running containers |
| `docker compose start` | Start stopped containers |
| `docker compose restart` | Restart services |
| `docker compose down` | Stop and remove containers |
| `docker compose down -v` | Remove containers and associated volumes |

**Warning:** `docker compose down -v` deletes the database volume and its stored data. Use it only when you intentionally want to remove the database data.

## Learning Objectives

This project is designed to develop practical experience in:

- Containerization using Docker.
- Multi-container orchestration using Docker Compose.
- Backend and frontend application integration.
- PostgreSQL database management.
- Database persistence using Docker volumes.
- Container networking and service communication.
- Environment variable configuration.
- Linux command-line administration.
- Version control and collaboration using Git and GitHub.
- Application debugging and troubleshooting.

## Project Roadmap

The project is being developed incrementally, with the following planned improvements:

- [x] Build the FastAPI backend.
- [x] Develop the React frontend.
- [x] Integrate PostgreSQL with SQLAlchemy.
- [x] Implement task CRUD operations.
- [x] Containerize the backend.
- [x] Containerize the frontend.
- [x] Containerize PostgreSQL.
- [x] Configure Docker Compose.
- [x] Configure persistent database storage.
- [ ] Implement database migrations using Alembic.
- [ ] Implement automated testing.
- [ ] Set up CI/CD using GitHub Actions.
- [ ] Publish container images to a container registry.
- [ ] Deploy the application to a cloud platform.
- [ ] Implement monitoring and logging.

## Author

**Nolan Davis**

Computer Systems & Networks Student | Aspiring Cloud & DevOps Engineer

- GitHub: [@Nolan550](https://github.com/Nolan550)
- Project Repository: [Task Manager – Cloud & DevOps](https://github.com/Nolan550/task_manager_devops)

---

*This project is part of my practical journey into Cloud Engineering and DevOps, focusing on building, containerizing, managing, and eventually deploying real-world applications.*
