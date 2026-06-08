# Containerized ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![AWS S3](https://img.shields.io/badge/AWS_S3-Storage-FF9900?logo=amazons3&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3-SDK-232F3E?logo=amazonaws&logoColor=white)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

## 🚀 Overview

The **Containerized ETL Pipeline** project demonstrates how a complete **API-to-S3 data pipeline** can be packaged and run inside a Docker container.

This project takes a real-world data engineering workflow and makes it:
- Portable  
- Reproducible  
- Scalable  

---

## 🎯 Problem Statement

Traditional ETL pipelines often face challenges like:

- Environment dependency issues  
- "It works on my machine" problem  
- Difficult deployment across systems  
- Manual setup of dependencies  

---

## ✅ Solution

This project solves these problems by:

- Containerizing the entire ETL pipeline using **Docker**
- Running the same code in any environment without setup issues
- Automating the flow from **API → Processing → AWS S3**
- Ensuring reproducibility across development and production

---

## 🏗️ Architecture

WeatherAPI → Python ETL Script → Pandas Transformation → CSV File → AWS S3 Upload (Boto3)
↓
Docker Container

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Core ETL logic |
| Docker | Containerization |
| Pandas | Data transformation |
| Requests | API calls |
| Boto3 | AWS S3 integration |
| AWS S3 | Cloud storage |

---

## 📦 Project Features

- API-based data extraction (Weather data)
- Data cleaning and transformation using Pandas
- CSV file generation
- Automated upload to AWS S3
- Fully containerized execution using Docker

---

## 📂 Project Structure

* etl-pipeline-containerized-docker/
* │
* ├── app.py # Main ETL pipeline script
* ├── requirements.txt # Python dependencies
* ├── Dockerfile # Docker configuration
* ├── .env # Environment variables (excluded from Git)
* └── README.md

---

## ⚙️ How It Works

### 1️⃣ Extract
- Fetch live data from WeatherAPI using `requests`

### 2️⃣ Transform
- Convert JSON response into structured Pandas DataFrame
- Clean and format data

### 3️⃣ Load
- Save data as CSV
- Upload file to AWS S3 using Boto3

---

## 🐳 Docker Setup

### Build Docker Image

docker build -t containerized-etl

---

## Run Container

### Docker run

docker run containerized-etl

---

## 🔐 Environment Variables

Create a .env file:

* WEATHER_API_KEY=your_api_key
* AWS_ACCESS_KEY_ID=your_key
* AWS_SECRET_ACCESS_KEY=your_secret
* S3_BUCKET_NAME=your_bucket_name

---

## 📊 Output Example

* city,temp,humidity,timestamp
* Multan,38,25,2026-06-09 10:00:00
* Lahore,34,40,2026-06-09 10:00:01
* Islamabad,30,55,2026-06-09 10:00:02

---

## 🧪 Key Learnings

* Docker containerization for data pipelines
* API integration using Python
* Cloud storage automation (AWS S3)
* Building portable ETL systems
* Environment variable management

---

## 📈 Project Impact

This project demonstrates how modern data pipelines can be:

* Fully automated
* Easily deployable
* Environment independent
* Production ready

---

## 🔗 Repository

https://github.com/ubaidsaghir/etl-pipeline-containerized-docker

---

## 🌐 Author

[![GitHub](https://img.shields.io/badge/GitHub-ubaidsaghir-181717?logo=github&logoColor=white)](https://github.com/ubaidsaghir)

---




