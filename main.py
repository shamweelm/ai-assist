from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from logger import get_logger
import uvicorn
from ai_assist.routes.chat_routes import chat_router
from ai_assist.routes.users_routes import users_router

logger = get_logger(__name__)

app = FastAPI()

# Add prefix to all routes
app.include_router(chat_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")


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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
