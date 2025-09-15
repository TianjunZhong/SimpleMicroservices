from __future__ import annotations

from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    id: UUID = Field(
        default_factory=uuid4,
        description="Persistent Item ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"},
    )

    name: str = Field(
        ...,
        description="Name of the product",
        json_schema_extra={"example": "Big Mac"},
    )

    ingredients: List[str] = Field(
        default_factory=list,
        description="Ingredients used in the product",
        json_schema_extra={
            "example": [
                "Mac Sauce",
                "Diced Onions",
                "Shredded Lettuce",
                "Pickle",
                "American Cheese",
                "1/10 Lb Beef",
                "Salt",
                "Big Mac Bun"
            ]
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
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
        }
    }


class ItemCreate(ItemBase):
    """Creation payload; ID is generated server-side but present in the base model."""
    model_config = {
        "json_schema_extra": {
            "examples": [
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
        }
    }


class ItemUpdate(BaseModel):
    """Partial update; Item ID is taken from the path, not the body."""
    name: Optional[str] = Field(
        ...,
        description="Name of the product",
        json_schema_extra={"example": "Big Mac"},
    )

    ingredients: Optional[List[str]] = Field(
        default_factory=list,
        description="Ingredients used in the product",
        json_schema_extra={
            "example": [
                "Mac Sauce",
                "Diced Onions",
                "Shredded Lettuce",
                "Pickle",
                "American Cheese",
                "1/10 Lb Beef",
                "Salt",
                "Big Mac Bun"
            ]
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
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
        }
    }


class ItemRead(ItemBase):
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
        }
    }
