from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.core.logging import logger


def http_error_handler(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        logger.error(f"HTTP error: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail}
        )

    logger.error(f"Unexpected error type in http_error_handler: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


def general_error_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )
