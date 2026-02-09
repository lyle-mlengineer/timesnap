from pydantic import BaseModel


class Timestamp(BaseModel):
    timestamp: str
    title: str


class Timestamps(BaseModel):
    timestamps: list[Timestamp]


class ExtractionResponse(BaseModel):
    video_id: str
    title: str
    timestamps: list[Timestamp]
    thumbnail_url: str
