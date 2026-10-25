# 🚀 Zero-Downtime Deployment Pipeline

## 📌 Project Overview

This project demonstrates a modern DevOps deployment pipeline that aims to minimize application downtime during software updates using Docker, Kubernetes, Argo Rollouts, and Prometheus.

A Flask web application is containerized with Docker and deployed on Kubernetes. Canary deployment gradually introduces new application versions, while monitoring and health checks help detect issues and support automated rollback.

## 🛠️ Technologies Used

- **Python & Flask** – Web application
- **Docker** – Containerization
- **Kubernetes** – Container orchestration
- **Argo Rollouts** – Canary deployments and rollback
- **Prometheus** – Monitoring and metrics
- **Git & GitHub** – Version control
- **AWS ECR & EKS** – Container registry and managed Kubernetes (planned or implemented, depending on project status)
- **GitHub Actions** – CI/CD automation (planned or implemented, depending on project status)

## ✨ Key Features

- Containerized Flask application
- Application health-check endpoint
- Progressive Canary deployment strategy
- Kubernetes-based application management
- Monitoring with Prometheus
- Automated rollback when configured analysis checks fail
- Version control using Git and GitHub

## 🏗️ Architecture

Developer → GitHub → Docker Image → Kubernetes → Argo Rollouts → Canary Deployment

Prometheus monitors application metrics and can provide data for deployment analysis and rollback decisions.

## 📂 Project Structure

```text
zero-downtime-deployment/
├── app/
│   ├── app.py
│   └── requirements.txt
├── kubernetes/
│   ├── rollout.yaml
│   └── service.yaml
├── Dockerfile
├── README.md
└── .gitignore
```

Update this structure to match the files actually present in your repository.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sojangshibu/zero-downtime-deployment-pipeline.git
cd zero-downtime-deployment-pipeline
```

### 2. Build the Docker image

```bash
docker build -t zero-downtime-app:v1 .
```

### 3. Run the application

```bash
docker run --rm -p 5000:5000 -e APP_VERSION=v1 zero-downtime-app:v1
```

### 4. Test the application

Open `http://localhost:5000/` in your browser, or run:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
```

## 🎯 Learning Outcomes

- Docker image creation and container management
- Kubernetes deployment concepts
- Canary release strategies
- Application health checks
- Prometheus monitoring fundamentals
- DevOps automation and rollback concepts

## 👨‍💻 Author

**DevOps & Cloud Engineering Learner**

This project is part of my hands-on learning journey in DevOps, Linux administration, containerization, Kubernetes, monitoring, and cloud technologies.
