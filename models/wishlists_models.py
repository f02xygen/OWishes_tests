from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID

from models.item_models import ItemOutModel

class WhishlistWithStatsModel(BaseModel):
    id: UUID
    owner_id: UUID
    title: str
    description: str
    event_date: datetime
    slug: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    total_items: int
    reserved_items: int


class CreateWishlistRequestModel(BaseModel):
    title: str
    description: str
    event_date: datetime

class WishlistDetailModel(BaseModel):
    id: UUID
    owner_id: UUID
    title: str
    description: str
    event_date: datetime
    slug: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
    items: list[ItemOutModel]

class WishListOutModel(BaseModel):
    id: UUID
    owner_id: UUID
    title: str
    description: str
    event_date: datetime
    slug: str
    is_active: bool
    created_at: datetime
    updated_at: datetime