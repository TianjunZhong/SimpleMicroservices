from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, StringConstraints

from .address import AddressBase
from .item import ItemBase


class McDonaldsBase(BaseModel):
    address: AddressBase = Field(
        default_factory=list,
        description="Location of the McDonald's store",
        json_schema_extra={
            "example": {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "street": "600 W 125th St",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10027",
                    "country": "US",
            }
        },
    )

    menu: List[ItemBase] = Field(
        default_factory=list,
        description="List of items offered in the store",
        json_schema_extra={
            "example": [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Big Mac",
                    "ingredients": [
                        "Mac Sauce",
                        "Diced Onions",
                        "Shredded Lettuce",
                        "Pickle",
                        "American Cheese",
                        "1/10 Lb Beef",
                        "Salt",
                        "Big Mac Bun"
                    ]
                }
            ]
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "address": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "street": "600 W 125th St",
                        "city": "New York",
                        "state": "NY",
                        "postal_code": "10027",
                        "country": "US",
                    },
                    "menu": [
                        {
                            "name": "Big Mac",
                            "ingredients": [
                                "Mac Sauce",
                                "Diced Onions",
                                "Shredded Lettuce",
                                "Pickle",
                                "American Cheese",
                                "1/10 Lb Beef",
                                "Salt",
                                "Big Mac Bun"
                            ]
                        }
                    ]
                }
            ]
        }
    }


class McDonaldsCreate(McDonaldsBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "address": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "street": "600 W 125th St",
                        "city": "New York",
                        "state": "NY",
                        "postal_code": "10027",
                        "country": "US",
                    },
                    "menu": [
                        {
                            "name": "Big Mac",
                            "ingredients": [
                                "Mac Sauce",
                                "Diced Onions",
                                "Shredded Lettuce",
                                "Pickle",
                                "American Cheese",
                                "1/10 Lb Beef",
                                "Salt",
                                "Big Mac Bun"
                            ]
                        }
                    ]
                }
            ]
        }
    }


class McDonaldsUpdate(BaseModel):
    """Partial update for a McDonalds; supply only fields to change."""
    address: Optional[AddressBase] = Field(
        None,
        description="Replace the store location",
        json_schema_extra={
            "example": {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "street": "600 W 125th St",
                    "city": "New York",
                    "state": "NY",
                    "postal_code": "10027",
                    "country": "US",
            }
        },
    )

    menu: Optional[List[ItemBase]] = Field(
        default_factory=list,
        description="List of items offered in the store",
        json_schema_extra={
            "example": [
                {
                    "name": "Big Mac",
                    "ingredients": [
                        "Mac Sauce",
                        "Diced Onions",
                        "Shredded Lettuce",
                        "Pickle",
                        "American Cheese",
                        "1/10 Lb Beef",
                        "Salt",
                        "Big Mac Bun"
                    ]
                }
            ]
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "address": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "street": "600 W 125th St",
                        "city": "New York",
                        "state": "NY",
                        "postal_code": "10027",
                        "country": "US",
                    },
                    "menu": [
                        {
                            "name": "Big Mac",
                            "ingredients": [
                                "Mac Sauce",
                                "Diced Onions",
                                "Shredded Lettuce",
                                "Pickle",
                                "American Cheese",
                                "1/10 Lb Beef",
                                "Salt",
                                "Big Mac Bun"
                            ]
                        }
                    ]
                }
            ]
        }
    }


class McDonaldsRead(McDonaldsBase):
    """Server representation returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated McDonald's store ID.",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "address": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "street": "600 W 125th St",
                        "city": "New York",
                        "state": "NY",
                        "postal_code": "10027",
                        "country": "US",
                    },
                    "menu": [
                        {
                            "name": "Big Mac",
                            "ingredients": [
                                "Mac Sauce",
                                "Diced Onions",
                                "Shredded Lettuce",
                                "Pickle",
                                "American Cheese",
                                "1/10 Lb Beef",
                                "Salt",
                                "Big Mac Bun"
                            ]
                        }
                    ]
                }
            ]
        }
    }
