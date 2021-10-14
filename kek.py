

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton



BOT_TOKEN = ""


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)



itembtn1 = types.KeyboardButton('F.A.Q')
itembtn2 = types.KeyboardButton('Местонахождение')
itembtn3 = types.KeyboardButton('Поддержать авторов')




keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(itembtn1, itembtn2, itembtn3)
#keyboard = types.ReplyKeyboardMarkup.add(itembtn3)

inline_btn_1 = InlineKeyboardButton('Что такое Eco-Box?', callback_data='btn1')
inline_btn_2 = InlineKeyboardButton('Как работает Eco-Box?', callback_data='btn2')
inline_btn_3 = InlineKeyboardButton('Какая главная задача контейнера?', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('Почему мне стоит купить Eco-Box?', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('Какая цена контейнера?', callback_data='btn5')
inline_btn_6 = InlineKeyboardButton('Где будет стоять контейнер?', callback_data='btn6')

# inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
# inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)
# inline_kb3 = InlineKeyboardMarkup().add(inline_btn_3)
# inline_kb4 = InlineKeyboardMarkup().add(inline_btn_4)



inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1, inline_btn_2, inline_btn_3, inline_btn_4, inline_btn_5, inline_btn_6)


inline_kb_full.row()




@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 1:
        await bot.send_message(callback_query.from_user.id,'Eco-Box - это умный контейнер для сортировки мусора')
    elif code == 2:
        await  bot.send_message(callback_query.from_user.id,'Внутри контейнера есть камера, которая распознаёт мусор.\nДалее активируются моторы, которые сдвигают мусор к определённой ячейке.\nПосле всего выше перечисленого открываются сервоприводы из-за чего мусор падает в определённый отсек. ')
    if code == 3:
        await bot.send_message(callback_query.from_user.id,'Главной задачей контейнера является разделение мусора без участия людей')
    elif code  == 4:
        await bot.send_message(callback_query.from_user.id,'Потому что покупая Eco-Box, вы делаете мир чище')
    if code == 5:
        await bot.send_message(callback_query.from_user.id,'Цена нашего контейнера зависит от комплектации.\nВерсия на 3 отсека стоит 500тыс. руб, на 5 отсеков стоит 600тыс. руб.')
    elif code == 6:
        await bot.send_message(callback_query.from_user.id,'Основное место для контейнера это места большой посещаемости')
    # else:
    #     await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


@dp.message_handler(text=['F.A.Q'])
async def process_command_2(message: types.Message):
    await message.answer("Вот одни из часто задавемых вопросов:", reply_markup=inline_kb_full)



@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await bot.send_message(message.chat.id,"Привет!👋\n Я помогу тебе ответить на часто задаваемые вопросы проекту Eco-Box.", reply_markup=keyboard)
# @bot.message.handler(commands=['start'])
# def danil(message: Message):
#    bot.send_message(message.chat.id,"HI" )

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(text=['Местонахождение'])
async def message_chzv(message: types.Message):
    await  message.answer("На данный момент эта функция в разработке.\nПриносим свои извинения")

@dp.message_handler(text=['Поддержать авторов'])
async def message_chzv(message: types.Message):
    await  message.answer("Деньги можно отправить на данный счет:\n+79600404465")


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_message(message: types.Message):
    await message.answer("Я не понимаю тебя")

if __name__ == '__main__':
    executor.start_polling(dp)

