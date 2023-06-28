import asyncio

from config import settings
from handlers.authorization import router as authorization_router
from handlers.phone_confirmation import router as phone_confirmation_router
from handlers.echo import router as echo_router
from misc.scheduler import scheduler_jobs
# from models.redis_connector import RedisConnector as rds

from create_bot import bot, dp, scheduler, logger, register_global_middlewares

user_routers = [
    authorization_router,
    phone_confirmation_router
]


async def main():
    logger.info("Starting bot")
    scheduler_jobs()
    # rds.redis_start()
    dp.include_routers(
        *user_routers,
        echo_router
    )

    try:
        scheduler.start()
        register_global_middlewares(dp, settings)
        # await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()
        scheduler.shutdown(True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
