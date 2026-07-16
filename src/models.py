from pydantic import BaseModel, ConfigDict, Field


class Book(BaseModel):
    """
    Represents a book extracted from the website.
    """

    model_config = ConfigDict(
        frozen=True,
        str_strip_whitespace=True,
    )

    title: str = Field(
        min_length=1,
        max_length=300,
    )

    price: float = Field(
        gt=0,
    )

    availability: bool

    rating: int = Field(
        ge=1,
        le=5,
    )

    product_url: str
