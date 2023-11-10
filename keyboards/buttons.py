from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ======================================================================================================================
cancel_button = KeyboardButton('Отмена')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button)

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('да'),
                                          KeyboardButton('нет'))
# ======================================================================================================================
back = KeyboardButton('/<назад')
# ======================================================================================================================
yesno = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2).add(KeyboardButton('Да'),
                     KeyboardButton('Нет'),
                     cancel_button)

# ======================================================================================================================
start = ReplyKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            row_width=2).add(KeyboardButton('/Товары'),
                                             KeyboardButton('/Написать_отзыв'),
                                             KeyboardButton('/Заказать'),
                                             KeyboardButton('/Примерить'),
                                             KeyboardButton('/О_нас!'))



finish_load_photos = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add \
    (KeyboardButton('/Это_все_сохранить_фото'))

# ======================================================================================================================

OrderWhereCategory = ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True,
                                         row_width=2).add(KeyboardButton('/Обувь'),
                                                          KeyboardButton('/Нижнее_белье'),
                                                          KeyboardButton('/Акссесуары'),
                                                          KeyboardButton('/Верхняя_одежда'),
                                                          KeyboardButton('/Штаны'),
                                                          back)


city_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                  one_time_keyboard=True,
                                  row_width=2
                                  ).add(KeyboardButton('Бишкек'),
                                        KeyboardButton('ОШ'),
                                        KeyboardButton('Москва 1-филиал'),
                                        KeyboardButton('Москва 1-филиал'))

# ======================================================================================================================
all_products = ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True,
                                     row_width=2).add(KeyboardButton("/Товары_Бишкек!"))


all_categories = ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True,
                                     row_width=2).add(KeyboardButton('Обувь'),
                                                      KeyboardButton('Нижнее_белье'),
                                                      KeyboardButton('Акссесуары'),
                                                      KeyboardButton('Верхняя_одежда'),
                                                      KeyboardButton('Штаны'),
                                                      KeyboardButton('Все_товары!'),
                                                      cancel_button)

price_categories = ReplyKeyboardMarkup(resize_keyboard=True,
                                       one_time_keyboard=True,
                                       row_width=2
                                       ).add(KeyboardButton('До_2000сом'),
                                             KeyboardButton('2000_4000сом'),
                                             KeyboardButton('4000_6000сом'),
                                             KeyboardButton('+6000сом'),
                                             KeyboardButton("/Все_цены!"))
# ======================================================================================================================




# ======================================================================================================================





