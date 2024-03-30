import fastapi
import fastapi
import database
# from src.database import get_db

from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

import contacts.models as models
import contacts.schemas as schemas

router = fastapi.APIRouter(prefix='/contacts', tags=["contacts"])


# @router.get("/")
# async def root(
#     db=fastapi.Depends(database.get_db)
#     # db=fastapi.Depends(get_db)
# ) -> list[schemas.ContactResponseSchema]:
#     return [contact for contact in db.query(models.ContactModel).all()]


@router.get("/err")
async def test_err_route():
    raise fastapi.HTTPException(503, "Test error")


# @router.get("/healthcheck")
# async def healthcheck(
#         # db=fastapi.Depends(database.get_db)
#         db: AsyncSession = Depends(database.get_db)):
#     try:
#         async with db() as session:
#             await session.execute("SELECT 1")
#     except Exception as e:
#         return {"status": "error", "message": str(e)}
#     return {"status": "ok"}
