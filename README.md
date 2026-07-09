# Cloud Infrastructure Monitoring & Incident Management Platform

A real-time infrastructure monitoring dashboard built using Flask, SQLite, Chart.js, and psutil.

## Features

- Real-time CPU monitoring
- Real-time Memory monitoring
- Real-time Disk monitoring
- Historical metrics storage
- Incident detection and logging
- Incident dashboard
- REST APIs for metrics and incidents
- Automatic chart refresh
- SQLite database integration

## Tech Stack

### Backend
- Python
- Flask
- psutil
- SQLite

### Frontend
- HTML
- JavaScript
- Chart.js

### Database
- SQLite

## Project Architecture

```
Browser Dashboard
       |
       v
    Flask API
       |
       +----------------+
       |                |
       v                v
  SQLite DB       psutil Collector
       |
       v
 Historical Metrics
 & Incident Logs
```

## APIs

### Get Current Metrics

```http
GET /metrics
```

Response:

```json
{
  "cpu": 25.4,
  "memory": 68.2,
  "disk": 41.7
}
```

### Get Historical Metrics

```http
GET /history
```

### Get Incidents

```http
GET /incidents
```

## Incident Detection

The system automatically creates incidents when resource usage exceeds configured thresholds.

### CPU

```text
CPU > 80%
```

### Memory

```text
Memory > 90%
```

### Disk

```text
Disk > 90%
```

## Dashboard Features

- CPU Usage Chart
- Memory Usage Chart
- Disk Usage Chart
- Historical Monitoring
- Live Updates
- Incident Tracking

## Project Structure

```
cloud-infrastructure-monitor/
│
├── app.py
├── monitor.py
├── database.py
├── monitor.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── dashboard.html
│
└── static/
```

## Installation

```bash
git clone <repository-url>
cd cloud-infrastructure-monitor
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask psutil
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Future Enhancements

- Docker Containerization
- Kubernetes Deployment
- Health Score Monitoring
- Incident Severity Levels
- Alert Notifications
- Export Metrics to CSV
- Cloud Deployment

## Resume Description

Developed a real-time Cloud Infrastructure Monitoring & Incident Management Platform using Flask, SQLite, Chart.js, and psutil. Implemented automated system metrics collection, historical data storage, incident detection, REST APIs, and live monitoring dashboards for CPU, memory, and disk utilization.
