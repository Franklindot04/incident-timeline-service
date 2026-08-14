def get_version() -> str:
    with open("VERSION", "r") as f:
        return f.read().strip()
