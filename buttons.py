from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# ======================================================================================================================
cancel_button = KeyboardButton('/cancel')
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True,
                                    ).add(cancel_button)

submit_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True
                                    ).add(KeyboardButton('Да'),
                                          KeyboardButton('Нет'))
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
                            row_width=2).add(KeyboardButton('/Товары!'),
                                             KeyboardButton('/Написать_отзыв'),
                                             KeyboardButton('/Заказать'),
                                             KeyboardButton('/Примерить'),
                                             KeyboardButton('/Забронировать'),
                                             KeyboardButton('/О_нас!'),
                                             KeyboardButton('/Филиалы'))


startForAdmins = ReplyKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            row_width=2).add(KeyboardButton('/Клиентские_кнопки!'),
                                             KeyboardButton('/Рассылка'),
                                             KeyboardButton('/Все_отзывы!'),
                                             KeyboardButton('/Филиалы'))


send_products = ReplyKeyboardMarkup(resize_keyboard=True,
                            one_time_keyboard=True,
                            row_width=2).add(KeyboardButton('/Готовые_товары!'),
                                             KeyboardButton('/Вручную!'),
                                             KeyboardButton('/Назад'))


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
                                        KeyboardButton('Ош 2-филиал'),
                                        cancel_button)

# ======================================================================================================================

all_categories = ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True,
                                     row_width=2).add(KeyboardButton('Обувь'),
                                                      KeyboardButton('Нижнее_белье'),
                                                      KeyboardButton('Акссесуары'),
                                                      KeyboardButton('Верхняя_одежда'),
                                                      KeyboardButton('Штаны'),
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
