from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import ADMIN
from function.commands import Commands
from function.utils import Utils
from aiogram.fsm.context import FSMContext
from keybords.admin_kd import admin_kd
roater = Router()
cmd= Commands()


@roater.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext):
    if message.chat.type=="private":
        if message.from_user.id in ADMIN:
            await message.answer('hay', reply_markup=admin_kd)
    elif message.chat.type in 'group':
        if not cmd.group_exist(message.chat.id):
            await message.answer('теперь эта группа будет получать рассылку')
            cmd.add_group(message)



@roater.message()
async def echo_handler(message: Message):
    await message.answer(message.text)