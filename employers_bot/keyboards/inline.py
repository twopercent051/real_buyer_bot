from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class AuthorizationInline:

    @classmethod
    def main_menu_kb(cls):
        keyboard = [
            [InlineKeyboardButton(text="Знакомые покупатели", callback_data="familiar_customers")],
            [InlineKeyboardButton(text="Создать заявку", callback_data="create_ticket")],
            [InlineKeyboardButton(text="Мои заявки", callback_data="my_tickets")],
            [InlineKeyboardButton(text="Архив", callback_data="archive")],
            [InlineKeyboardButton(text="Баланс", callback_data="balance")],
            [InlineKeyboardButton(text="Поддержка", url="https://t.me/lentachold")],
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

