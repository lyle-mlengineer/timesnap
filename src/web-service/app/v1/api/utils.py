import json
import os
import re

from tubectrl import YouTube
from tubectrl.models import Video

from app.v1.core.config import config as BaseConfig
from .schemas import ExtractionResponse, Timestamp, Timestamps


def get_youtube(
    client_secret_file: str = BaseConfig.CLIENT_SECRET_FILE,
    credentials_path: str = BaseConfig.YOUTUBE_CREDENTIALS_PATH,
) -> YouTube:
    youtube: YouTube = None
    if credentials_path:
        print("youtube from credentails")
        youtube = YouTube()
        youtube.authenticate_from_credentials(credentials_path=credentials_path)
    else:
        print("youtube from path")
        youtube = YouTube(client_secret_file=client_secret_file)
        youtube.authenticate(client_secret_file)
    return youtube


def find_video(video_id: str, youtube: YouTube) -> Video:
    video: Video = youtube.find_video_by_id(video_id=video_id)
    return video


def get_video_description(video: Video) -> str:
    description: str = video.snippet.description
    return description


def parse_video_id(url: str) -> str:
    video_id: str
    try:
        video_id: str = url.split("=")[1].split("&")[0]
    except IndexError:
        video_id = url
    return video_id


def format_extraction_response(extraction_response: ExtractionResponse) -> str:
    response: str = ""
    response += "{\n"
    response += '  "videoId": "' + extraction_response.video_id + '",\n'
    response += '  "title": "' + extraction_response.title + '",\n'
    response += '  "timestamps": [\n'
    for timestamp in extraction_response.timestamps:
        response += "    {\n"
        response += '      "title": "' + timestamp.title + '",\n'
        response += '      "timestamp": "' + timestamp.timestamp + '"\n'
        response += "    },\n"
    response += "  ]\n"
    response += "}"
    return response


def post_process_title(title: str) -> str:
    title: str = re.sub(r"-", "", title)
    title = title.strip()
    return title


def get_timestamp_and_title(match_group: tuple) -> Timestamp:
    title: str = match_group[2]
    title = post_process_title(title=title)
    timestamp: str = match_group[0] + match_group[1]
    return Timestamp(title=title, timestamp=timestamp)


def extract_timestamps(description: str) -> list[Timestamp]:
    timestamps: list[Timestamp] = []
    pattern = r"(\d+:)+(\d+)(.+)"
    pattern_compiled = re.compile(pattern)
    matches = re.finditer(pattern_compiled, description)
    for match in matches:
        timestamp: Timestamp = get_timestamp_and_title(match.groups())
        timestamps.append(timestamp)
    return timestamps


def save_extraction_response(extraction_response: ExtractionResponse):
    file_name: str = os.path.join(BaseConfig.DATA_DIR, f"{extraction_response.video_id}.json")
    with open(file_name, "w") as file:
        json.dump(extraction_response.model_dump(), file, indent=4)


def load_extraction_response(video_id: str) -> ExtractionResponse:
    file_name: str = os.path.join(BaseConfig.DATA_DIR, f"{video_id}.json")
    with open(file_name, "r") as file:
        extraction_response: ExtractionResponse = ExtractionResponse(**json.load(file))
    return extraction_response


async def extract_video_timestamps(video_url: str) -> tuple[str, ExtractionResponse]:
    video_id: str = parse_video_id(video_url)
    if os.path.exists(os.path.join(BaseConfig.DATA_DIR, f"{video_id}.json")):
        extraction_response: ExtractionResponse = load_extraction_response(
            video_id=video_id
        )
    else:
        youtube: YouTube = get_youtube()
        video: Video = find_video(video_id=video_id, youtube=youtube)
        # print(video)
        description: str = get_video_description(video=video)
        timestamps: list[Timestamps] = extract_timestamps(description=description)
        for resolution in ["default", "high", "medium", "standard"]:
            for thumbnail in video.snippet.thumbnails:
                if thumbnail.resolution == resolution:
                    thumbnail_url: str = thumbnail.url
                    print(f"Thumbnail URL for resolution {resolution}: {thumbnail_url}")
                    break
        extraction_response = ExtractionResponse(
            video_id=video_id,
            title=video.snippet.title,
            timestamps=timestamps,
            thumbnail_url=thumbnail_url,
        )
        save_extraction_response(extraction_response=extraction_response)
    formatted_response = format_extraction_response(extraction_response)
    return formatted_response, extraction_response
