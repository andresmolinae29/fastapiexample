from typing import Optional, List
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=20)
    overview: str = Field(default= 'Ujum', min_length=5, max_length=30)
    year: int = Field(default=2023, le=9999, gt=1900)
    rating: float
    category: str = Field(min_length=4, max_length=15)

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'title': 'My movie',
                'overview': 'Description movie',
                'year': 2022,
                'rating': 9.4,
                'category': 'Thriller'
            }
        }