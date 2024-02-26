from aiogram import types, Dispatcher
import buttons
from config import Admins, Developers, Director


async def support(message: types.Message):
    await message.answer("Здесь будет контакты поддержки!")


async def back(message: types.Message):
    await message.answer('Вы возвратились назад!', reply_markup=buttons.start)


async def backadmins(message: types.Message):
    if message.from_user.id in Admins or Director or Developers:
        await message.answer('Вы возвратились назад!', reply_markup=buttons.startForAdmins)


async def about(message: types.Message):
    if message.from_user.id in Admins:
        await message.answer(text='Добро пожаловать в захватывающий мир OSOR – где стиль встречает инновации! \n\n'
                                  'OSOR – не просто бренд, а настоящее искусство самовыражения через моду. 🌟\n '
                                  'Наши коллекции объединяют смелость, элегантность и последние тренды, создавая уникальный '
                                  'стиль для каждого. 💫\n\n'
                                  'OSOR исследует грани традиционного и смело переопределяет их, '
                                  'придавая классическим элементам современный шарм. Наши дизайны – это не просто одежда, '
                                  'это сочетание выдающегося качества материалов, утонченных деталей и страсти к инновациям. 🎨\n\n'
                                  'Мы верим, что стиль - это индивидуальное выражение личности, и каждая вещь OSOR создана, '
                                  'чтобы подчеркнуть вашу уникальность. Наши коллекции отражают динамичность современной жизни, '
                                  'предлагая яркие решения для любого повода. ✨\n\n'
                                  'Ознакомьтесь с нашими последними трендами, обновлениями и коллекциями, и дайте своему '
                                  'стилю засиять с OSOR! ✨\n\n'
                                  'Проблемы, которые могут возникнуть ⬇️\n'
                                  '"Не выходит из категорий" - пропишите команду /cancel\n\n'
                                  'Вы админ/менеджер❗', reply_markup=buttons.startForAdmins)


    else:
        await message.answer('Добро пожаловать в захватывающий мир OSOR – где стиль встречает инновации! \n\n'
                             'OSOR – не просто бренд, а настоящее искусство самовыражения через моду. 🌟\n '
                             'Наши коллекции объединяют смелость, элегантность и последние тренды, создавая уникальный '
                             'стиль для каждого. 💫\n\n'
                             'OSOR исследует грани традиционного и смело переопределяет их, '
                             'придавая классическим элементам современный шарм. Наши дизайны – это не просто одежда, '
                             'это сочетание выдающегося качества материалов, утонченных деталей и страсти к инновациям. 🎨\n\n'
                             'Мы верим, что стиль - это индивидуальное выражение личности, и каждая вещь OSOR создана, '
                             'чтобы подчеркнуть вашу уникальность. Наши коллекции отражают динамичность современной жизни, '
                             'предлагая яркие решения для любого повода. ✨\n\n'
                             'Ознакомьтесь с нашими последними трендами, обновлениями и коллекциями, и дайте своему '
                             'стилю засиять с OSOR! ✨'
                             '\n\n'
                             'Проблемы, которые могут возникнуть ⬇️\n'
                             '"Не выходит из категорий" - пропишите команду /cancel'
                             '\n\n'
                             'Дополнительная ориентировка насчет филиалов - "/Ориентировка_по_боту"',
                             reply_markup=buttons.start)


async def send_products(message: types.Message):
    await message.answer("Вы зашли в рассылку товаров в канал!", reply_markup=buttons.send_products)


# ==================================================================================================================


async def price_categories(message: types.Message):
    await message.answer("Выберите снизу ценовую категорию! ⬇️", reply_markup=buttons.price_categories)


async def order_products(message: types.Message):
    await message.answer("Вы зашли в заказы товара! \n"
                         "Здесь можете заполнить данные о товаре \nкоторый хотите заказть! ⬇️")




async def shoes(message: types.Message):
    await message.answer(f'Вы зашли в категорию "{message.text[1::]}"! \n'
                         'Здесь будут все товары этой категории! ⬇'
                         '\n'
                         'В котором можно будет заполнить данные товара и свои данные(ФИО, номер телефона и т.д)',
                         reply_markup=buttons.all_categories)


async def price(message: types.Message):
    price_all_categories = ['До_2000сом', '2000_4000сом', '4000_6000сом', '+6000сом']
    if message.text in price_all_categories:
        await message.answer(f"Здесь будут все товары ценовой категории {message.text}! ⬇")

    else:
        pass


async def all_price(message: types.Message):
    await message.answer("Здесь будут товары всех ценовых категорий! ⬇")


async def all_products(message: types.Message):
    await message.answer("Выберите филиал 📍", reply_markup=buttons.all_products)


async def ButtonClient(message: types.Message):
    await message.answer('Вы перешли к клиентским кнопкам!', reply_markup=buttons.start)



# ==================================================================================================================

def register_start(dp: Dispatcher):
    dp.register_message_handler(back, commands=['<назад'])
    dp.register_message_handler(backadmins, commands=['Назад'])
    dp.register_message_handler(about, commands=['О_нас!', 'about'])
    # ======================================================================
    dp.register_message_handler(order_products, commands=['Заказать'])
    dp.register_message_handler(shoes, commands=['Обувь', 'Нижнее_белье', 'Акссесуары', 'Верхняя_одежда', 'Штаны'])
    # ======================================================================
    dp.register_message_handler(all_products, commands=['Товары'])
    dp.register_message_handler(price_categories, commands=['Все_товары!'])
    dp.register_message_handler(all_price, commands=['Все_цены!'])
    dp.register_message_handler(send_products, commands=['Рассылка'])
    # ======================================================================
    dp.register_message_handler(ButtonClient, commands=['Клиентские_кнопки!'])
