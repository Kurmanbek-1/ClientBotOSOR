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

back_button = KeyboardButton('<Назад')
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

finish_load_photos = ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True).add(KeyboardButton('/Это_все_сохранить_фото'),
                                                                     cancel_button)

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
                                        KeyboardButton('Ош'),
                                        KeyboardButton('Москва'),
                                        back_button)

# ======================================================================================================================

all_categories = ReplyKeyboardMarkup(resize_keyboard=True,
                                     one_time_keyboard=True,
                                     row_width=2).add(KeyboardButton('Обувь'),
                                                      KeyboardButton('Нижнее_белье'),
                                                      KeyboardButton('Акссесуары'),
                                                      KeyboardButton('Верхняя_одежда'),
                                                      KeyboardButton('Штаны'),
                                                      cancel_button)

all_categories_bishkek = ReplyKeyboardMarkup(resize_keyboard=True,
                                             one_time_keyboard=True,
                                             row_width=2).add(KeyboardButton('Обувь_Бишкек'),
                                                              KeyboardButton('Нижнее_белье_Бишкек'),
                                                              KeyboardButton('Акссесуары_Бишкек'),
                                                              KeyboardButton('Верхняя_одежда_Бишкек'),
                                                              KeyboardButton('Штаны_Бишкек'),
                                                              back_button)

all_categories_osh = ReplyKeyboardMarkup(resize_keyboard=True,
                                         one_time_keyboard=True,
                                         row_width=2).add(KeyboardButton('Обувь_Ош'),
                                                          KeyboardButton('Нижнее_белье_Ош'),
                                                          KeyboardButton('Акссесуары_Ош'),
                                                          KeyboardButton('Верхняя_одежда_Ош'),
                                                          KeyboardButton('Штаны_Ош'),
                                                          back_button)

all_categories_moscow = ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True,
                                            row_width=2).add(KeyboardButton('Обувь_Москва'),
                                                             KeyboardButton('Нижнее_белье_Москва'),
                                                             KeyboardButton('Акссесуары_Москва'),
                                                             KeyboardButton('Верхняя_одежда_Москва'),
                                                             KeyboardButton('Штаны_Москва'),
                                                             back_button)

# ======================================================================================================================
