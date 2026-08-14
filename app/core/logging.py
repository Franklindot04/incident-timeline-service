import logging
import json
from app.core.config import settings


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = {
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        return json.dumps(log)


def configure_logging():
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())

    logging.basicConfig(
        level=settings.log_level,
        handlers=[handler],
        force=True,
    )

    return logging.getLogger("incident-service")


logger = configure_logging()
