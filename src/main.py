import fastapi
import uvicorn
import starlette.middleware.base

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

import contacts.routes
import contacts.exceptions
import database

import middlewares

app = fastapi.FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts.routes.router, prefix='/api')
# app.include_router(contacts.routes.router)

# app.add_middleware(
#     starlette.middleware.base.BaseHTTPMiddleware,
#     dispatch=middlewares.printer_middleware
# )
#
# app.add_exception_handler(
#     fastapi.HTTPException,
#     contacts.exceptions.item_not_found_error_handler
# )

@app.get("/")
def index():
    return {"message": "Contacts Application"}


@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(database.get_db)):
    try:
        # Make request
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Error connecting to the database")


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="localhost", port=8000, reload=True
    )
