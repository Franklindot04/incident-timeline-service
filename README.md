# Incident Timeline Service

A lightweight FastAPI microservice for tracking incidents, their severity, and timestamps.

## Features
- **[Create incidents](ca://s?q=Create_incidents)**  
- **[List incidents](ca://s?q=List_incidents)**  
- **[Validate severity levels](ca://s?q=Validate_severity_levels)**  
- **[Simple CLI client](ca://s?q=Explain_CLI_client)**  
- **[Health check endpoint](ca://s?q=Health_check_endpoint)**  
- **[CI pipeline with pytest](ca://s?q=CI_pipeline_with_pytest)**  

## API Endpoints

### Health
`GET /health`

### Create Incident
`POST /incidents/`
```json
{
  "id": 1,
  "title": "Database outage",
  "severity": "high"
}
```

### List Incidents
`GET /incidents/`

## CLI Usage

### Create Incident
```python
python cli.py --create --id 1 --title "DB outage" --severity high
```

### List Incidents
```python
python cli.py --list
```

## Architecture Diagram 
```
+------------------------+
|      CLI Client        |
+-----------+------------+
            |
            v
+------------------------+
|      FastAPI App       |
+-----------+------------+
            |
            v
+------------------------+
|   Incident Model       |
+-----------+------------+
            |
            v
+------------------------+
|   In-Memory Store      |
+------------------------+
```
