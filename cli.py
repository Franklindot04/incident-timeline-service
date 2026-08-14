import requests
import argparse

BASE_URL = "http://localhost:8000"


def create_incident(id, title, severity):
    try:
        payload = {
            "id": id,
            "title": title,
            "severity": severity
        }
        response = requests.post(f"{BASE_URL}/incidents/", json=payload)
        print(response.json())
    except Exception as e:
        print({"error": str(e)})


def list_incidents():
    try:
        response = requests.get(f"{BASE_URL}/incidents/")
        print(response.json())
    except Exception as e:
        print({"error": str(e)})


def update_incident(id, title, severity):
    try:
        payload = {
            "id": id,
            "title": title,
            "severity": severity
        }
        response = requests.put(f"{BASE_URL}/incidents/{id}", json=payload)
        print(response.json())
    except Exception as e:
        print({"error": str(e)})


def delete_incident(id):
    try:
        response = requests.delete(f"{BASE_URL}/incidents/{id}")
        print(response.json())
    except Exception as e:
        print({"error": str(e)})


def filter_incidents(severity=None, limit=10, offset=0):
    try:
        params = {}
        if severity:
            params["severity"] = severity
        params["limit"] = limit
        params["offset"] = offset

        response = requests.get(f"{BASE_URL}/incidents/filter", params=params)
        print(response.json())
    except Exception as e:
        print({"error": str(e)})


def severity_analytics():
    try:
        response = requests.get(f"{BASE_URL}/incidents/analytics/severity")
        print(response.json())
    except Exception as e:
        print({"error": str(e)})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Incident CLI")
    parser.add_argument("--create", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--update", action="store_true")
    parser.add_argument("--delete", action="store_true")
    parser.add_argument("--filter", action="store_true")
    parser.add_argument("--analytics", action="store_true")
    parser.add_argument("--id", type=int)
    parser.add_argument("--title")
    parser.add_argument("--severity")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--offset", type=int, default=0)

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
    elif args.analytics:
        severity_analytics()
    else:
        print("Use --create, --list, --update, --delete, --filter, or --analytics")
