import logging
import redis
import betterlogging as bl

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import settings
from middlewares.config import ConfigMiddleware


# r = redis.Redis(host=config.rds.host, port=config.rds.port, db=config.rds.db)
# storage = RedisStorage(redis=r) if config.tg_bot.use_redis else MemoryStorage()
bot = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()
scheduler = AsyncIOScheduler()

logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))
