from aiogram import Router
from aiogram.fsm.context import FSMContext

from create_bot import bot
from misc.states import UserFSM

router = Router()


async def enter_phone(user_id: int | str, state: FSMContext):
    text = "Введите ваш номер телефона. Номер телефона должен начинаться с +7 и принадлежать вам. Мы отправим " \
           "смс при необходимости подтверждения"
    await state.set_state(UserFSM.phone_confirm)
    await bot.send_message(chat_id=user_id, text=text)
