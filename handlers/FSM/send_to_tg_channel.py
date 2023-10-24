# =======================================================================================================================
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

from config import Admins, bot, CHANNEL_ID
from keyboards import buttons


# =======================================================================================================================


class SendToChannelFSM(StatesGroup):
    title = State()
    text = State()
    photos = State()
    submit = State()


media_group = types.MediaGroup()

async def fsm_start(message: types.Message):
    if message.from_user.id in Admins:
        await SendToChannelFSM.title.set()
        await message.answer('Введите заголовок для рассылки в канал', reply_markup=buttons.cancel_markup)
    else:
        await message.answer("Вы не админ!!!")


async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title_for_channel'] = message.text
        await message.answer("Введите текст для рассылки в канал", reply_markup=buttons.cancel_markup)
        await SendToChannelFSM.next()


async def load_text(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text_for_channel'] = message.text
        await message.answer("Отправьте фото рассылки", reply_markup=buttons.cancel_markup)
        await SendToChannelFSM.next()


async def load_photos(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if "photos" in data:
            data["photos"].append(message.photo[-1].file_id)
        else:
            data["photos"] = [message.photo[-1].file_id]

    await message.answer(f"Фотография добавлена. Отправьте еще или завершите ввод",
                         reply_markup=buttons.finish_load_photos)


# Обработчик команды /done для завершения
async def finish_load_photos(message: types.Message, state: FSMContext):
    async with state.proxy() as data:

        for i in data['photos']:
            if i in media_group:
                pass
            media_group.attach_photo(types.InputMediaPhoto(i))


        print(media_group)
        await bot.send_media_group(chat_id=message.from_user.id, media=media_group)
        await message.answer("Всё правильно?", reply_markup=buttons.submit_markup)
        await SendToChannelFSM.next()


async def load_submit(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text.lower() == 'да':
            channel_id = CHANNEL_ID
            await bot.send_media_group(chat_id=channel_id, media=media_group)
            # await bot.send_message(chat_id=channel_id, text=f"{data['title_for_channel']}\n\n{data['text_for_channel']}")
            await state.finish()
        else:
            await message.answer("Отмена!")
            await state.finish()


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!')


def register_send_to_channel(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['news'])

    dp.register_message_handler(load_title, state=SendToChannelFSM.title)
    dp.register_message_handler(load_text, state=SendToChannelFSM.text)
    dp.register_message_handler(load_photos, state=SendToChannelFSM.photos, content_types=['photo'])
    dp.register_message_handler(finish_load_photos, commands=['Это_все_сохранить_фото'], state=SendToChannelFSM.photos)
    dp.register_message_handler(load_submit, state=SendToChannelFSM.submit)
