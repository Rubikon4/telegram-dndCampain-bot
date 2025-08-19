import logging
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from app.core.config import settings
from app.bot.handlers import router as bot_router
from app.web.api import app as fastapi_app

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(bot_router)

# Встраиваем бота в FastAPI
@fastapi_app.post(settings.WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    data = await request.json()
    update = dp.feed_webhook_update(bot, data)
    return {"ok": True}

app = fastapi_app
