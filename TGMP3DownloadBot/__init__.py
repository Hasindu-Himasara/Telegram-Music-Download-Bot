# TG_MP3_Download_Bot

import logging
from pyrogram import Client
from config import API_HASH, API_ID, BOT_TOKEN

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

MP3DownloadBot = Client("TGMP3DownloadBot", bot_token=2080924626:AAE-_tHwgNDLGPsQIYCoCotpYrrEq_5hmng, api_hash=09fb2bd3ee46019e911149d4970bfc47
, api_id=7744764)
