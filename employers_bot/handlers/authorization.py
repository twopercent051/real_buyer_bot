import aiohttp
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.fsm.context import FSMContext

from create_bot import bot
from handlers.phone_confirmation import enter_phone
from keyboards.inline import AuthorizationInline
from services.fastapi_connector import ConnectorDB

router = Router()


async def main_menu(user_id: str | int):
    text = "Главное меню"
    kb = AuthorizationInline.main_menu_kb()
    await bot.send_message(chat_id=user_id, text=text, reply_markup=kb)


@router.message(Command('start'))
async def user_start(message: Message, state: FSMContext):
    user = await ConnectorDB.get("/employers", data={"user_id": str(message.from_user.id)})
    if user:
        await main_menu(user_id=message.from_user.id)
    else:
        await enter_phone(user_id=message.from_user.id, state=state)

