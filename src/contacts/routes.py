import fastapi
import fastapi
import database

import contacts.models as models
import contacts.schemas as schemas

router = fastapi.APIRouter(prefix='/contacts', tags=["contacts"])

@router.get("/")
async def root(
    db=fastapi.Depends(database.get_database)
) -> list[schemas.ContactResponseSchema]:
    return [contact for contact in db.query(models.ContactModel).all()]


@router.get("/err")
async def test_err_route():
    raise fastapi.HTTPException(503, "Test error")
