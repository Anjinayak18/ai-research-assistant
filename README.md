# AI Research & Knowledge Assistant

## Overview

AI Research & Knowledge Assistant is a production-style FastAPI application that enables users to upload PDF documents, generate embeddings, perform semantic search, ask questions using Retrieval-Augmented Generation (RAG), summarize documents using Google Gemini, classify document types using Machine Learning, generate analytics, and export reports.

---

## Features

### Document Management
- Upload PDF documents
- Process documents
- Delete documents
- View uploaded documents

### AI Features
- Semantic Search
- Retrieval-Augmented Generation (RAG)
- AI Summarization
- Document Classification

### Machine Learning
- Dataset Preparation
- TF-IDF Vectorization
- Logistic Regression Classification

### Analytics
- Documents Processed
- Chunks Generated
- Vector Statistics
- Search Statistics

### Export
- CSV
- Excel
- PDF

### Deployment
- Docker
- Docker Compose

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLite
- SQLAlchemy
- ChromaDB
- Sentence Transformers
- Google Gemini API
- Scikit-learn
- Pandas
- OpenPyXL
- ReportLab
- Docker

---

## Project Structure

```
config/
data/
docs/
logs/
models/
routes/
src/
tests/

Dockerfile
docker-compose.yml
requirements.txt
main.py
README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-research-assistant.git

cd ai-research-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env`

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
uvicorn main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

## Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

## API Endpoints

### Documents

- POST /documents/upload
- GET /documents
- DELETE /documents/{id}

### Search

- GET /search
- POST /ask

### Analysis

- POST /analysis/summarize

### Analytics

- GET /analytics/overview

### Export

- GET /export/analytics/csv
- GET /export/analytics/excel
- GET /export/summary/pdf

---

## Author

Anji Katravath