from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from logger import get_logger

logger = get_logger(__name__)

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print("STARTUP Event to be added")


@app.exception_handler(HTTPException)
async def http_exception_handler(_, exc):
    return JSONResponse(
            status_code=exc.status_code,
            content={
                    "error_detail": exc.detail
                },
        )
