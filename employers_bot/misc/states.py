from aiogram.fsm.state import State, StatesGroup


class UserFSM(StatesGroup):
    home = State()
    phone_confirm = State()
