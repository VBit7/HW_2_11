import pydantic

class ContactResponseSchema(pydantic.BaseModel):
    id: int
    model: str
    image_url: str
    fuel_tank_volume: int
