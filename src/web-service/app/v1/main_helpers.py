from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import stripe

import logging

from app.v1.core.config import config
# from app.v1.api import subscription_tier_router
# from app.v1.api import speaker_router
# from app.v1.api import sub_speaker_router
# from app.v1.api import subscription_router
# from app.v1.api import generation_router
# from app.v1.api import payment_router 
# from app.v1.api import oauth_router
from app.v1.ui import ui
# from app.v1.api import audio_router
from app.v1.exception_handlers import register_exception_handlers
# from app.v1.services.oauth_service import OAuthService
# from app.v1.services.subscription_tier_service import SubscriptionTierService
# from app.v1.services.subscription_tier_speaker_service import SubscriptionTierSpeakerService
# from app.v1.services.speaker_service import SpeakerService
# from app.v1.models.speaker import SpeakerCreate
# from app.v1.models.subscription_tier import SubscriptionTierCreate
# from app.v1.models.oauth import UserCreate
# from app.v1.db.db import SessionLocal
# from app.v1.models.subscription_tier_speaker import SubscriptionTierSpeakerCreate
from app.v1.core.extensions import drive
 
def mount_static_directories(app: FastAPI):
    app.mount(
        "/static", 
        StaticFiles(directory=config.STATIC_DIR), 
        name="static"
        )
    app.mount(
        "/data", 
        StaticFiles(directory=config.DATA_DIR), 
        name="data"
    )

def add_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def register_routers(app: FastAPI):
    api_version: str = config.API_VERSION
    # app.include_router(subscription_tier_router.router, prefix=f"/api/{api_version}")
    # app.include_router(speaker_router.router, prefix=f"/api/{api_version}")
    # app.include_router(sub_speaker_router.router, prefix=f"/api/{api_version}")
    # app.include_router(subscription_router.router, prefix=f"/api/{api_version}")
    # app.include_router(generation_router.router, prefix=f"/api/{api_version}")
    # app.include_router(payment_router.router, prefix=f"/api/{api_version}", include_in_schema=False)
    app.include_router(ui.router, include_in_schema=False)
    # app.include_router(oauth_router.router, prefix=f"/api/{api_version}")
    # app.include_router(audio_router.router, prefix=f"/api/{api_version}")


def init_extensions(app: FastAPI) -> None:
    logging.info("Initializing extensions...")
    logging.info("Initializing Google Drive")
    drive.authenticate_from_credentials(config.GOOGLE_DRIVE_CREDENTIALS)
    logging.info("Google Drive initialized")
    logging.info("Initializing Stripe")
    stripe.api_key = config.STRIPE_SECRET_KEY
    logging.info("Stripe initialized")
    logging.info("Extensions initialized")


# def create_default_user():
#     logging.info("Creating default user")
#     with SessionLocal() as db:
#         oauth_service = OAuthService(db=db)
#         try:
#             oauth = oauth_service.get_oauth_by_email(email=config.DEFAULT_USER_EMAIL)
#         except HTTPException:
#             logging.info(f"Creating the default user: {config.DEFAULT_USER_NAME}")
#             oauth_service.create_oauth(
#                 user=UserCreate(
#                     name=config.DEFAULT_USER_NAME,
#                     email=config.DEFAULT_USER_EMAIL,
#                     password=config.DEFAULT_USER_PASSWORD,
#                     confirm_password=config.DEFAULT_USER_PASSWORD
#                 )
#             )
#             logging.info("Created the defaukt user")
#         else:
#             logging.info(f"The default user: {config.DEFAULT_USER_NAME} already exists")

# def create_basic_subscription_tier():
#     logging.info("Creating basic subscription tier")
#     with SessionLocal() as db:
#         subscription_tier_service = SubscriptionTierService(session=db)
#         subscription_tier = subscription_tier_service.get_subscription_tier_by_name(name="BASIC")
#         if not subscription_tier:
#             logging.info("Basic subscription tier does not exist")
#             logging.info("Creating Basic subscription tier")
#             basic_subscription_tier = SubscriptionTierCreate(
#                 name="BASIC",
#                 description="The Basic tier provides five generations with single male speaker.",
#                 rate_limit=5,
#                 max_text_len=20,
#                 max_audio_duration=30,
#                 max_generations=5,
#                 download_allowed=True,
#                 price=1.0
#             )
#             subscription_tier = subscription_tier_service.create_subscription_tier(
#                 subscription_tier=basic_subscription_tier)
#             logging.info("Basic subscription tier created")
#         else:
#             logging.info("Basic subscription tier already exists")
#     return subscription_tier

# def create_default_speaker() -> None:
#     logging.info("Creating default speaker")
#     data = {
#         "name": "abel",
#         "first_name": "Abel",
#         "last_name": "Mutua",
#         "description": "A narative speaker",
#         "dialect": "kikuyu",
#         "use": "For narrative",
#         "gender": "male"
#     }
#     with SessionLocal() as session:
#         service = SpeakerService(db=session)
#         speaker = service.get_speaker_by_name(name=data["name"])
#         if speaker:
#             logging.info("Default speaker already exists")
#             return speaker
#         speaker = service.create_speaker(speaker_create=SpeakerCreate(**data))
#         logging.info("Default speaker created")
#         return speaker
    
# def create_default_subscription_tier_speaker(speaker_id: str, subscription_tier_id: str) -> None:
#     with SessionLocal() as db:
#         service = SubscriptionTierSpeakerService(session=db)
#         try:
#             default = service.get_subscription_tier_speaker(subscription_tier_id=subscription_tier_id, speaker_id=speaker_id)
#         except HTTPException:
#             logging.info("Creating default speaker subdcription tier")
#             default = service.create_subscription_tier_speaker(
#                 SubscriptionTierSpeakerCreate(
#                     subscription_tier_id=subscription_tier_id, 
#                     speaker_id=speaker_id
#                 )
#             )
#         else:
#             logging.info("The default speaker subdcription tier already exists")
#             return
        

# def create_default_entities():
#     tier = create_basic_subscription_tier()
#     speaker = create_default_speaker()
#     create_default_subscription_tier_speaker(speaker_id=speaker.id, subscription_tier_id=tier.id)
#     create_default_user()

def setup_app(app: FastAPI):
    mount_static_directories(app)
    register_routers(app)
    register_exception_handlers(app)
    add_middleware(app)
    init_extensions(app)

    # create_default_entities()