# TimeSnap
## Overview
<img src="./assets/snaptube.png" class="img-responsive" alt="">

> This is an easy to use web service used to extract timestamps from YouTube videos. Built to teach beginners the process of data collection and annotation for the pretraining, finetuning and deployment of a transformer based small language model.

The application uses a small custom trained transformer model to extract timestamps from youtube videos.

The application includes:
1. User Management (both authentication and authorization using both password based and social oauth)
2. Payment processing
3. Rate limiting
4. A dashboard to monitor usage
5. Logging and tracing (open-telemtry and jaeger)

## Getting started
To use this application, you will need a YouTube API key, a computer with python installed.

1. Clone the GitHub repo
```sh
  git clone https://github.com/lyle-mlengineer/timesnap.git
```
2. Navigate to the project directory:
```sh
cd timesnap
```
3. Create the environment variables. Add them to the ```.env``` file.
4. Start the application:
```
uvicorn app.main:app
```
5. Navigate to ``http://localhost:8000`` to access the application.

## The application
- Uses FastApi and vanilla javascript
- Uses the YouTube API to process videos, playlists and channels
- Uses Redis for caching and for background processing
- Uses PostgreSQL for storage