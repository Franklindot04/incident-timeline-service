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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Incident CLI")
    parser.add_argument("--create", action="store_true")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--update", action="store_true")  # ← added here
    parser.add_argument("--id", type=int)
    parser.add_argument("--title")
    parser.add_argument("--severity")

    args = parser.parse_args()

    if args.create:
        create_incident(args.id, args.title, args.severity)
    elif args.list:
        list_incidents()
    elif args.update:
        update_incident(args.id, args.title, args.severity)
    else:
        print("Use --create, --list, or --update")
