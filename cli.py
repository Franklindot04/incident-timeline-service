import requests
import argparse

BASE_URL = "http://localhost:8000"

def create_incident(id, title, severity):
    payload = {
        "id": id,
        "title": title,
        "severity": severity
    }
    response = requests.post(f"{BASE_URL}/incidents/", json=payload)
    print(response.json())

def list_incidents():
    response = requests.get(f"{BASE_URL}/incidents/")
    print(response.json())

def update_incident(id, title, severity):
    payload = {
        "id": id,
        "title": title,
        "severity": severity
    }
    response = requests.put(f"{BASE_URL}/incidents/{id}", json=payload)
    print(response.json())

def delete_incident(id):
    response = requests.delete(f"{BASE_URL}/incidents/{id}")
    print(response.json())

def filter_incidents(severity=None, limit=10, offset=0):
    params = {}
    if severity:
        params["severity"] = severity
    params["limit"] = limit
    params["offset"] = offset

    response = requests.get(f"{BASE_URL}/incidents/filter", params=params)
    print(response.json())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Incident CLI")
    parser.add_argument("--create", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--delete", action="store_true")
    parser.add_argument("--filter", action="store_true")   # ← added
    parser.add_argument("--id", type=int)
    parser.add_argument("--title")
    parser.add_argument("--severity")
    parser.add_argument("--limit", type=int, default=10)   # ← added
    parser.add_argument("--offset", type=int, default=0)   # ← added

    args = parser.parse_args()

    if args.create:
        create_incident(args.id, args.title, args.severity)
    elif args.list:
        list_incidents()
    elif args.update:
        update_incident(args.id, args.title, args.severity)
    elif args.delete:
        delete_incident(args.id)
    elif args.filter:
        filter_incidents(args.severity, args.limit, args.offset)
    else:
        print("Use --create, --list, --update, --delete, or --filter")
