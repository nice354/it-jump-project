import vk_api, json, random, time

vk = vk_api.VkApi(token="b285cce2a8e87ab1e485ef1eada50293c74d66ec816cfe4d3fdc35fb4c4f9bde3eec015e767ddcefd10c3")

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [
        [
        get_button(label="Инфо", color="positive"),
        get_button(label="Дать совет", color="positive"),
            ],
            [
        get_button(label="Дать ещё совет ", color="default"),
        get_button(label="Дать третий совет", color="default"),
             ],
             [
        get_button(label="Дать четвёртый совет", color="primary"),
        get_button(label="Дать пятый совет", color="primary"),
             ],
             [
        get_button(label="Поддеражать автора", color="negative"),
        get_button(label="Дать весёлый совет :D", color="negative"),
        ]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unread"})

    if messages["count"] >= 1:

        id = messages["items"][0]["last_message"]["from_id"]
        text = messages["items"][0]["last_message"]["text"]


        if text.lower() == "привет":
            vk.method("messages.send", {"peer_id": id, "message": "Я здесь!", "random_id": random.randint(1, 999999)})
        elif text == "Клавиатура":
            vk.method("messages.send", {"peer_id": id, "message": "Держи свою клаву!", "random_id": random.randint(1, 999999), "keyboard": keyboard})
        elif text == "Инфо":
            vk.method("messages.send", {"peer_id": id, "message":  "Здравствуй, друг я бот Витёк, могу дать мотивирующий совет. Команда моих создателей называется Vitech", "random_id": random.randint(1, 999999)})
        elif text == "Дать совет":
            vk.method("messages.send", {"peer_id": id, "message": "Единственной уважительной причиной, по которой вы можете сдаться, является ваша смерть. До тех пор, пока вы живы (здоровы и свободны), у вас есть выбор, чтобы совершать попытки до окончательного успеха.", "random_id": random.randint(1, 999999)})
        elif text == "Дать ещё совет":
            vk.method("messages.send", {"peer_id": id, "message": "Вероятность освоения чего-то с первого раза очень мала. Все требует времени, чтобы этому научиться, и вы будете совершать ошибки. Учитесь на них.", "random_id": random.randint(1, 999999)})
        elif text == "Дать третий совет":
            vk.method("messages.send", {"peer_id": id, "message": "Зачастую, когда вы чувствуете, что хотите сдаться, вы находитесь так близко к тому, чтобы сделать огромный прорыв. В любой момент своего времени вы всегда находитесь лишь на волосок от успеха.", "random_id": random.randint(1, 999999)})
        elif text == "Пока":
            vk.method("messages.send", {"peer_id": id, "message": "Пока :(", "random_id": random.randint(1, 999999)})
        elif text == "Как дела":
            vk.method("messages.send", {"peer_id": id, "message": "Бот Витёк негодует D:", "random_id": random.randint(1, 999999)})
        elif text == "Дать четвёртый совет":
            vk.method("messages.send", {"peer_id": id, "message": "Когда вы достигнете всего, чего намеревались достичь, вы можете использовать свой успех, чтобы совершать изменения в мире или в жизни отдельных людей.", "random_id": random.randint(1, 999999)})
        elif text == "Дать пятый совет":
            vk.method("messages.send", {"peer_id": id, "message": "Если вы не хотите быть известным, как кто-то другой, то это слабость, и говорит о том, что вы сдаетесь. Выходите и показывайте себя остальному миру, а также самому себе. Вы можете и добьетесь того, что намеревались сделать. Вы потерпите неудачу только тогда, когда сдадитесь.", "random_id": random.randint(1, 999999)})
        elif text == "Поддеражать автора":
            vk.method("messages.send", {"peer_id": id, "message": "89600404465 киви", "random_id": random.randint(1, 999999)})
        elif text == "Где ты работаешь":
            vk.method("messages.send", {"peer_id": id, "message": "Я работаю в Байтике.", "random_id": random.randint(1, 999999)})
        elif text == "Дать весёлый совет :D":
            vk.method("messages.send", {"peer_id": id, "message": "Будь как протон: оставайся позитивным!", "random_id": random.randint(1, 999999)})
        elif text == "Витёк":
            vk.method("messages.send", {"peer_id": id, "message": "Да это я, бот Витёк", "random_id": random.randint(1, 999999)})
        elif text == "Какую еду ты любишь":
            vk.method("messages.send", {"peer_id": id, "message": "Я люблю роллы, но это не всё.", "random_id": random.randint(1, 999999)})
        elif text == "Какие игры ты любишь":
            vk.method("messages.send", {"peer_id": id, "message": "Я люблю змейку.", "random_id": random.randint(1, 999999)})
        elif text == "Помощь":
            vk.method("messages.send", {"peer_id": id, "message": "Вот мои команды:1 напиши клавиатура.2 Нажми на кнопку и получи ответ.3 задай свои вопрос по типу: где ты работаешь ", "random_id": random.randint(1, 999999)})
        elif text == "Что ты любишь":
            vk.method("messages.send", {"peer_id": id, "message": "Я люблю Гвидона вана Россума", "random_id": random.randint(1, 999999)})
        elif text == "Корпорация зла":
            vk.method("messages.send", {"peer_id": id, "message": "Apple", "random_id": random.randint(1, 999999)})
        elif text == "Спасибо":
            vk.method("messages.send", {"peer_id": id, "message": "Спасибо в карман не положишь (кнопка Поддеражать автора)", "random_id": random.randint(1, 999999)})
        elif text == "Ок":
            vk.method("messages.send", {"peer_id": id, "message": "oll korrect- Википедия.", "random_id": random.randint(1, 999999)})
        elif text == "Посоветуй канал на ютубе":
            vk.method("messages.send", {"peer_id": id, "message": "Руслан Гительман", "random_id": random.randint(1, 999999)})
        elif text == "Господи":
            vk.method("messages.send", {"peer_id": id, "message": "Роберт Эллиот Кан?", "random_id": random.randint(1, 999999)})
        elif text == "Ты бот":
            vk.method("messages.send", {"peer_id": id, "message": "Я настоящий живой мужчина. Забрался в ваше устройство, сижу.", "random_id": random.randint(1, 999999)})
        elif text == "Салам":
            vk.method("messages.send", {"peer_id": id, "message": "Кто меня звал?", "random_id": random.randint(1, 999999)})
        elif text == "Freelance BOT":
            vk.method("messages.send", {"peer_id": id, "message": "Да, слышал про это убожество", "random_id": random.randint(1, 999999)})
        elif text == "Кто такой бот Олег":
            vk.method("messages.send", {"peer_id": id, "message": "https://github.com/Draqneel", "random_id": random.randint(1, 999999)})
        elif text == "Посоветуй песню":
            vk.method("messages.send", {"peer_id": id, "message": "DEUTSCHLAND by Rammstein", "random_id": random.randint(1, 999999)})
        elif text == "Скажи 300":
            vk.method("messages.send", {"peer_id": id, "message": "Слишком банально!", "random_id": random.randint(1, 999999)})
        elif text == "150+150":
            vk.method("messages.send", {"peer_id": id, "message": "Меня так просто не обманешь!", "random_id": random.randint(1, 999999)})
        elif text == "600:2":
            vk.method("messages.send", {"peer_id": id, "message": "Триста. Да, мы трактористы))", "random_id": random.randint(1, 999999)})
        elif text == "Типичный малолетний...":
            vk.method("messages.send", {"peer_id": id, "message": "Типичный плюс", "random_id": random.randint(1, 999999)})
        else:
            vk.method("messages.send", {"peer_id": id, "message": "Извените, вы скорее всего ошиблись","random_id": random.randint(1, 999999)})
