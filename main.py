import datetime
import threading
import urllib.request

import mysql.connector
import requests
import telebot
from bs4 import BeautifulSoup

import constants

now = datetime.datetime.now()
now_month = now.month
now_day = now.day
print("Текущий месяц: %d" % now_month)
print("Текущий день: %d" % now_day)

try:
    db = mysql.connector.connect(
        host="209.250.253.38",
        user="gpbot_user",
        passwd="DHUIEh#$4647",
        port="3306",
        database="gpbot_db"
    )
    print(db)
    cursor = db.cursor()
except Exception as e:
    print(e)
    print("Ошибка подключения к базе данных")

id = []
status = []
day_off = []

try:
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    for x in result:
        print(x)

    cursor.execute("SELECT id_user FROM user")
    result = cursor.fetchall()
    id.clear()
    for x in result:
        # print(x)
        id.append(x)
    print(id)

    cursor.execute("SELECT status FROM user")
    result = cursor.fetchall()
    status.clear()
    for x in result:
        # print(x)
        status.append(x)
    print(status)

    cursor.execute("SELECT offtime FROM user")
    result = cursor.fetchall()
    day_off.clear()
    for x in result:
        # print(x)
        day_off.append(x)
    print(day_off)
except Exception as e:
    print(e)
    print("Ошибка выбора элементов с базы данных(перед старт)")

global defalt_status
defalt_status = 0
global defalt_data
defalt_data = 0

cheker = 0
bot = telebot.TeleBot(constants.token)


# def thread(my_func):
#     def wrapper(*args, **kwargs):
#         my_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs, daemon=True)
#         my_thread.start()
#
#     return wrapper
#
#
# @thread
# def go(nomer):
#     for x in range(1, 200):
#         print("Поток номер" + str(nomer) + "число" + str(x) + "\n")

# ----------------------------------------------------------------------------/start----------------------------------------------------------------------------------
@bot.message_handler(commands=["start"])
def handle_commanddd(message):
    chen_id_ = "(" + str(message.chat.id) + ",)"
    if str(chen_id_) not in str(id):
        try:
            db = mysql.connector.connect(
                host="209.250.253.38",
                user="gpbot_user",
                passwd="DHUIEh#$4647",
                port="3306",
                database="gpbot_db"
            )
            print(db)
            cursor = db.cursor()
        except Exception as e:
            print(e)
            print("Ошибка подключения к базе данных")
        try:
            sql = "INSERT INTO user (id_user, status, offtime) VALUES (%s, %s, %s)"
            val = (message.chat.id, defalt_status, defalt_data)
            cursor.execute(sql, val)
            db.commit()
            print(cursor.rowcount, "Запись добавена")
        except Exception as e:
            print(e)
            print("Пользователь уже существует")
    else:
        print("Пользователь уже существует")

    try:
        cursor.execute("SELECT * FROM user")
        result = cursor.fetchall()
        for x in result:
            print(x)

        cursor.execute("SELECT id_user FROM user")
        result = cursor.fetchall()
        id.clear()
        for x in result:
            # print(x)
            id.append(x)
        print(id)

        cursor.execute("SELECT status FROM user")
        result = cursor.fetchall()
        status.clear()
        for x in result:
            # print(x)
            status.append(x)
        print(status)

        cursor.execute("SELECT offtime FROM user")
        result = cursor.fetchall()
        day_off.clear()
        for x in result:
            # print(x)
            day_off.append(x)
        print(day_off)
    except Exception as e:
        print(e)
        print("Ошибка выбора элементов с базы данных")
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("✅ ДОБАВИТЬ", "❌ УДАЛИТЬ")
    user_markup.row("✍🏻 ВРУЧНУЮ", "📖 СПИСОК")
    user_markup.row("👑 ТАРИФЫ", "🛎 ПОДДЕРЖКА")
    bot.send_message(message.chat.id, "Привет!", reply_markup=user_markup)
    try:
        file = open(str(message.chat.id) + "problem.txt")
        file = open(str(message.chat.id) + "url.txt")
    except Exception as e:
        print(e)
        kreate = open(str(message.chat.id) + 'problem.txt', 'tw', encoding='utf-8')
        kreate.close()
        kreate2 = open(str(message.chat.id) + 'url.txt', 'tw', encoding='utf-8')
        kreate2.close()
    chen_id = "(" + str(message.chat.id) + ",)"
    print(chen_id)
    print(id)
    if str(chen_id) not in str(id):
        bot.send_message(message.chat.id, "В данный момент Вы не можете использовать бота\n"
                                          "Обратитесь к разработчику\n"
                                          "@rallen, сообщите ваш ID:\n"
                                          "После активации аккаунта\n"
                                          "нажмите /start")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Бот активен, приступим к работе")

        def chek_data():
            threading.Timer(21600.0, chek_data).start()
            print("Работает")

            now2 = datetime.datetime.now()
            global now_month2
            now_month2 = now2.month
            global now_day2
            now_day2 = now2.day

            try:
                db = mysql.connector.connect(
                    host="209.250.253.38",
                    user="gpbot_user",
                    passwd="DHUIEh#$4647",
                    port="3306",
                    database="gpbot_db"
                )
                print(db)
                cursor = db.cursor()
            except Exception as e:
                print(e)
                print("Ошибка подключения к базе данных")

            nomber = 0
            try:
                cursor.execute("SELECT id_user FROM user")
                result = cursor.fetchall()
                id.clear()
                r = 0
                for x in result:
                    r = r + 1
                    # print(x)
                    if str(x) == str(chen_id):
                        nomber = (r - 1)
                    id.append(x)
                print(id)
                print(nomber, "nomber for data in mas")

                cursor.execute("SELECT offtime FROM user")
                result = cursor.fetchall()
                day_off.clear()
                for x in result:
                    # print(x)
                    day_off.append(x)
                print(day_off)
                global do_kogda
                do_kogda = day_off[int(nomber)]
                lenf = sum(1 for line in open(str(message.chat.id) + 'problem.txt', 'r'))

                cursor.execute("SELECT status FROM user")
                result = cursor.fetchall()
                status.clear()
                for x in result:
                    # print(x)
                    status.append(x)
                print(status, "status")
                global now_status2
                now_status2 = status[int(nomber)]
                print(now_status2, "now_status")
            except Exception as e:
                print(e)
                print("Ошибка выбора элементов с базы данных(при ежедневной проверке)")

            print(int(lenf))
            print(str(do_kogda))
            print(str("(" + str(now_day) + ",)"))
            if int(lenf) > 1 and str(do_kogda) == str("(" + str(now_day2) + ",)"):
                try:
                    db = mysql.connector.connect(
                        host="209.250.253.38",
                        user="gpbot_user",
                        passwd="DHUIEh#$4647",
                        port="3306",
                        database="gpbot_db"
                    )
                    print(db)
                    cursor = db.cursor()
                except Exception as e:
                    print(e)
                    print("Ошибка подключения к базе данных")

                try:
                    sql = "UPDATE user SET status = %s WHERE offtime = %s"
                    val = ("0", str(now_day2))
                    cursor.execute(sql, val)
                    db.commit()
                    print(cursor.rowcount, "record(s) affected")
                except Exception as e:
                    print(e)
                    print("Ошибка обновления данных в бд")

                bot.send_message(message.chat.id, "Ваша подписка на бота закончилась\n"
                                                  "Продлите подписку либо удалите лишние приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif str(do_kogda) == str("(" + str(now_day2) + ",)"):

                try:
                    db = mysql.connector.connect(
                        host="209.250.253.38",
                        user="gpbot_user",
                        passwd="DHUIEh#$4647",
                        port="3306",
                        database="gpbot_db"
                    )
                    print(db)
                    cursor = db.cursor()
                except Exception as e:
                    print(e)
                    print("Ошибка подключения к базе данных")

                try:
                    sql1 = "UPDATE user SET status = %s WHERE offtime = %s"
                    val1 = ("0", str(now_day2))
                    cursor.execute(sql1, val1)
                    db.commit()
                    print(cursor.rowcount, "record(s) affected")
                except Exception as e:
                    print(e)
                    print("Ошибка обновления данных в бд")
                bot.send_message(message.chat.id, "Ваша подписка на бота закончилась\n"
                                                  "Продлите подписку либо удалите лишние приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif now_status2 == (3,):
                print("Статус ВИП")
            elif now_status2 == (2,):
                print("Статус Премиум+")
            elif now_status2 == (1,) and lenf > 5:
                bot.send_message(message.chat.id, "Количество приложений в вашем списке не\n"
                                                  "соответствует количеству,предусмотренного\n"
                                                  "вашим тарифом\n"
                                                  "Возможно закончился срок действия вашего тарифа\n"
                                                  "Продлите подписку либо удалите лишние приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif now_status2 == (0,) and lenf > 1:
                bot.send_message(message.chat.id, "Количество приложений в вашем списке не\n"
                                                  "соответствует количеству,предусмотренного\n"
                                                  "вашим тарифом\n"
                                                  "Возможно закончился срок действия вашего тарифа\n"
                                                  "Продлите подписку либо удалите лишние приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            else:
                print("Oll good")

        chek_data()

        # def do_my_cod(sc):
        def do_my_cod():
            threading.Timer(600.0, do_my_cod).start()
            try:
                lenf = sum(1 for line in open(str(message.chat.id) + 'problem.txt', 'r'))
            except Exception as e:
                print(e)
                print("Ошибка доступа к файлу")
            if int(lenf) > 1 and str(do_kogda) == str("(" + str(now_day2) + ",)"):
                print("Срок действия тарифа истек")
            elif now_status2 == (1,) and lenf > 5:
                print("Срок действия тарифа истек/лишнее приложение")
            elif now_status2 == (0,) and lenf > 1:
                print("Срок действия тарифа истек/лишнее приложение")
            else:
                try:
                    print("Doing ", message.chat.id)
                    list_of_apps = open(str(message.chat.id) + 'problem.txt', 'r').readlines()
                    leng = len(list_of_apps)
                    list_of_url = open(str(message.chat.id) + 'url.txt', 'r').readlines()
                    leng_url = len(list_of_url)
                    print(leng_url)
                    # if leng == 0:
                    #     print("Список пуст,я жду")
                    # else:
                    # list_of_apps.clear() не помню зачем надо
                    for nambers in range(leng):
                        print(nambers, "nambers")
                        with open(str(message.chat.id) + 'problem.txt', 'r') as f:
                            for i in range(int(nambers)):
                                f.readline()
                            x = f.readline()
                            print(x)
                            f.close()
                            try:
                                r = requests.get("https://play.google.com/store/search?q=" + str(x) + "&c=apps")
                                html = BeautifulSoup(r.content, "html.parser")
                            except Exception as e2:
                                print(e2)
                                print("Совпадений нет,проверте правильность введения названия")
                                bot.send_message(message.chat.id, "Совпадений нет,проверте правильность введения названия")

                            massiv_url = []
                            with open(str(message.chat.id) + 'url.txt', 'r') as p:
                                for i in range(int(nambers)):
                                    p.readline()
                                y = p.readline()
                                print(y)
                                p.close()
                                try:
                                    for el in html.find_all('img'):
                                        link = el['data-src']
                                        # link2 = str(link)
                                        massiv_url.append(link+"\n")
                                    print(massiv_url)
                                except Exception as e:
                                    print(e)
                                if y not in massiv_url:
                                    print("........Этого приложения нету в Google Play........")
                                    bot.send_message(message.chat.id, "Приложение перестало быть доступным для загрузки")
                                    bot.send_message(message.chat.id, "Мы очищаем список ваших приложений от недоступного "
                                                                      "приложения")
                                    try:
                                        with open(str(message.chat.id) + 'problem.txt', 'r') as o:
                                            data = o.readlines()
                                        data = filter(lambda line: x not in line, data)
                                        with open(str(message.chat.id) + 'problem.txt', 'w') as o:
                                            o.write("".join(data))

                                        with open(str(message.chat.id) + 'url.txt', 'r') as m:
                                            data2 = m.readlines()
                                        data2 = filter(lambda line: y not in line, data2)
                                        with open(str(message.chat.id) + 'url.txt', 'w') as m:
                                            m.write("".join(data2))
                                            bot.send_message(message.chat.id, "Приложение удалено из вашего списка")
                                            bot.send_message(message.chat.id, x)
                                    except Exception as e2:
                                        print(e2)
                                        print("........Ошибка,удаления, проверте правильность ввода........")
                                        bot.send_message(message.chat.id,
                                                             "Невозможно удалить приложение, проверьте правильность его названия")
                                else:
                                    print("Приложение есть,все хорошо!")
                except Exception as e2:
                    print(e2)
                    print("........Критическая ошибка при проверки, обратитесь в поддержку........ " + x)
                    bot.send_message(message.chat.id,
                                         "Возникла ошибка при работе, обратитесь в поддержку")
                # s.enter(15, 1, do_my_cod, (sc,))

        do_my_cod()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------admin------------------------------------------------------------------------------------
@bot.message_handler(commands=["admin"])
def handle_command(message):
    sent = bot.send_message(message.chat.id, 'Введите пароль администратора')
    bot.register_next_step_handler(sent, admin_user)


def admin_user(message):
    in_pas = message.text
    if in_pas == constants.pas:
        sent = bot.send_message(message.chat.id, 'Принято!\n'
                                                 'Впишите ID\n')
        bot.register_next_step_handler(sent, entr_id)
        # id.append(message.chat.id)
        # print(id)
    else:
        bot.send_message(message.chat.id, 'Не верный пароль!\n'
                                          'Попробуйте еще раз;\n'
                                          '/admin ')


def entr_id(message):
    global id_of_new_user
    id_of_new_user = message.text
    sent = bot.send_message(message.chat.id, 'Принято!\n'
                                             'Впишите статус в формате: 1\n')
    bot.register_next_step_handler(sent, entr_status)


def entr_status(message):
    global user_status
    user_status = message.text
    sent = bot.send_message(message.chat.id, 'Принято!\n'
                                             'Впишите дату до когда действует\n '
                                             '(вчерашним днем)\n '
                                             'в формате: 28\n')
    bot.register_next_step_handler(sent, date_end)


def date_end(message):
    user_data_end = message.text
    try:
        db = mysql.connector.connect(
            host="209.250.253.38",
            user="gpbot_user",
            passwd="DHUIEh#$4647",
            port="3306",
            database="gpbot_db"
        )
        print(db)
        cursor = db.cursor()
    except Exception as e:
        print(e)
        print("Ошибка подключения к базе данных")
    try:
        sql = "UPDATE user SET status = %s WHERE id_user = %s"
        val = (str(user_status), str(id_of_new_user))
        cursor.execute(sql, val)
        db.commit()

        sql = "UPDATE user SET offtime = %s WHERE id_user = %s"
        val = (str(user_data_end), str(id_of_new_user))
        cursor.execute(sql, val)
        db.commit()

        bot.send_message(message.chat.id, 'Принято!\n'
                                          'Данные добавлены')

    except Exception as e2:
        print(e2)
        bot.send_message(message.chat.id, 'Ошибка добавления, попробуйте еще раз\n'
                                          '/admin')


# ----------------------------------------------------------------------✅ДОБАВИТЬ----------------------------------------------------------------------------------------
@bot.message_handler(content_types=["text"])
def handle_command(message):
    if message.text == "✅ ДОБАВИТЬ":
        try:
            file = open(str(message.chat.id) + 'problem.txt')
            file = open(str(message.chat.id) + 'url.txt')
        except Exception as e:
            print(e)
            kreate = open(str(message.chat.id) + 'problem.txt', 'tw', encoding='utf-8')
            kreate.close()
            kreate2 = open(str(message.chat.id) + 'url.txt', 'tw', encoding='utf-8')
            kreate2.close()
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "В данный момент Вы не можете использовать бота\n"
                                              "Обратитесь к разработчику\n"
                                              "@rallen, сообщите ваш ID:\n"
                                              "После активации аккаунта\n"
                                              "нажмите /start")
            bot.send_message(message.chat.id, message.chat.id)
        else:
            try:
                db = mysql.connector.connect(
                    host="209.250.253.38",
                    user="gpbot_user",
                    passwd="DHUIEh#$4647",
                    port="3306",
                    database="gpbot_db"
                )
                print(db)
                cursor = db.cursor()
            except Exception as e:
                print(e)
                print("Ошибка подключения к базе данных")
            try:
                nomber = 0
                cursor.execute("SELECT id_user FROM user")
                result = cursor.fetchall()
                id.clear()
                r = 0
                for x in result:
                    r = r + 1
                    # print(x)
                    if str(x) == str(chen_id):
                        nomber = (r - 1)
                    id.append(x)
                print(id)
                print(nomber, "nomber for status in mas")

                cursor.execute("SELECT status FROM user")
                result = cursor.fetchall()
                status.clear()
                for x in result:
                    # print(x)
                    status.append(x)
                print(status, "status")
                global now_status
                now_status = status[int(nomber)]
                print(now_status, "now_status")
                lenf = sum(1 for line in open(str(message.chat.id) + 'problem.txt', 'r'))
                print(lenf, "lenf")
                if now_status == (3,):
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая регистры и специальные знаки!\n'
                                            'Например: не webviewappname, а WebViewAppName')
                    bot.register_next_step_handler(sent, hello)
                elif now_status == (2,):
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая регистры и специальные знаки!\n'
                                            'Например: не webviewappname, а WebViewAppName')
                    bot.register_next_step_handler(sent, hello)
                elif now_status == (1,) and lenf <= 4:
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая регистры и специальные знаки!\n'
                                            'Например: не webviewappname, а WebViewAppName')
                    bot.register_next_step_handler(sent, hello)
                elif now_status == (0,) and lenf <= 0:
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая регистры и специальные знаки!\n'
                                            'Например: не webviewappname, а WebViewAppName')
                    bot.register_next_step_handler(sent, hello)
                else:
                    bot.send_message(message.chat.id,
                                     'Вы исчерпали доступное количество приложений для проверки\n'
                                     'Перейдите в пункт "👑 ТАРИФЫ" в главном меню \n'
                                     'и обновите вашу подписку на более высокий уровень \n')
            except Exception as e:
                print(e)
                print("Ошибка обращения к бд")
    elif message.text == "✍🏻 ВРУЧНУЮ":
        try:
            file = open(str(message.chat.id) + 'onetestapp.txt')
        except Exception as e:
            print(e)
            kreate = open(str(message.chat.id) + 'onetestapp.txt', 'tw', encoding='utf-8')
            kreate.close()
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "В данный момент Вы не можете использовать бота\n"
                                              "Обратитесь к разработчику\n"
                                              "@rallen, сообщите ваш ID:\n"
                                              "После активации аккаунта\n"
                                              "нажмите /start")
            bot.send_message(message.chat.id, message.chat.id)
        else:
            sent = bot.send_message(message.chat.id, 'Я проверю это приложение один раз в реальном времени\n'
                                                     'Оно не будет занесено в список ваших приложений и не будет '
                                                     'проверяться автоматически\n\n '
                                                     'Введите название приложения учитывая регистры и специальные знаки!\n'
                                                     'Например: не webviewappname, а WebViewAppName')
            bot.register_next_step_handler(sent, chek_app)
    elif message.text == "📖 СПИСОК":
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "В данный момент Вы не можете использовать бота\n"
                                              "Обратитесь к разработчику\n"
                                              "@rallen, сообщите ваш ID:\n"
                                              "После активации аккаунта\n"
                                              "нажмите /start")
            bot.send_message(message.chat.id, message.chat.id)
        else:
            try:
                list_of_apps = open(str(message.chat.id) + 'problem.txt', 'r').read()
                bot.send_message(message.chat.id, 'Мы проверяем список ваших приложеий!\n')
                bot.send_message(message.chat.id, list_of_apps)
                print(list_of_apps)
            except Exception as e:
                print(e)
                print("........Ваш список пуст........")
                bot.send_message(message.chat.id, "В вашем списке нет никаких приложений!")
    elif message.text == "❌ УДАЛИТЬ":
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "В данный момент Вы не можете использовать бота\n"
                                              "Обратитесь к разработчику\n"
                                              "@rallen, сообщите ваш ID:\n"
                                              "После активации аккаунта\n"
                                              "нажмите /start")
            bot.send_message(message.chat.id, message.chat.id)
        else:
            try:
                try:
                    file = open(str(message.chat.id) + "problem.txt")
                except Exception as e:
                    print(e)
                    kreate = open(str(message.chat.id) + 'problem.txt', 'tw', encoding='utf-8')
                    kreate.close()
                sent = bot.send_message(message.chat.id,
                                        'Введите название приложения учитывая регистры и специальные знаки!\n'
                                        'Например: не webviewappname, а WebViewAppName\n')
                bot.register_next_step_handler(sent, enter_app_to_dell)
            except Exception as e:
                print(e)
                print("........Ошибка,удаления, проверте правильность ввода........")
                bot.send_message(message.chat.id, "Мы не нашли совпадений,\n"
                                                  " проверте правильность введения названия учитывая регистр!")
    elif message.text == "👑 ТАРИФЫ":
        chen_id = "(" + str(message.chat.id) + ",)"
        nomber = 0
        try:
            db = mysql.connector.connect(
                host="209.250.253.38",
                user="gpbot_user",
                passwd="DHUIEh#$4647",
                port="3306",
                database="gpbot_db"
            )
            print(db)
            cursor = db.cursor()
        except Exception as e:
            print(e)
            print("Ошибка подключения к базе данных")
        try:
            cursor.execute("SELECT id_user FROM user")
            result = cursor.fetchall()
            id.clear()
            r = 0
            for x in result:
                r = r + 1
                # print(x)
                if str(x) == str(chen_id):
                    nomber = (r - 1)
                id.append(x)
            print(id)
            print(nomber, "nomber for status in mas")

            cursor.execute("SELECT status FROM user")
            result = cursor.fetchall()
            status.clear()
            for x in result:
                # print(x)
                status.append(x)
            print(status, "status")

            cursor.execute("SELECT offtime FROM user")
            result = cursor.fetchall()
            day_off.clear()
            for x in result:
                # print(x)
                day_off.append(x)
            print(day_off)
        except Exception as e:
            print(e)
            print("Ошибка обращения к бд")
        now_status = status[int(nomber)]
        off_data = day_off[int(nomber)]
        print(now_status, "now_status")
        print(off_data, "off_data")
        if now_status == (3,):
            now_status = 3
        if now_status == (2,):
            now_status = 2
        if now_status == (1,):
            now_status = 1
        if now_status == (0,):
            now_status = 0
        if off_data == (0,):
            off_data = "Бессрочно"
        bot.send_message(message.chat.id, "Привет!\n"
                                          f'Ваш текущий тариф: {now_status}\n'
                                          f'Действует до: {off_data}\n'
                                          "\nДля пользования этим ботом, вы должны выбрать один из тарифов: \n"
                                          "\n"
                                          "0 - ОБЫЧНЫЙ: Бесплатно, отслеживание\n"
                                          "одного приложения, доступо всем\n"
                                          "пользователям автоматически.\n"
                                          "\n"
                                          "1 - ПРЕМИУМ: 5 USD/месяц, отслеживание пяти\n"
                                          "приложений\n"
                                          "\n"
                                          "2 - 👑 ПРЕМИУМ +: 10 USD/месяц, отслеживание безлимитного\n"
                                          "количества приложений\n"
                                          "\n"
        # "3- 👑 ВИП 👑: Отслеживание безлимитного\n"
        # "количества приложений.\n"
        # "\n"
                                          "Для заказа/изменения тарифа, пишите:\n"
                                          "@rallen \n"
                                          f'и сообщите ваш ID: {message.chat.id}')

    elif message.text == "🛎 ПОДДЕРЖКА":
        bot.send_message(message.chat.id, "Привет, мы рады тебя видеть!\n"
                                          "Если у Вас возникли вопросы, напишите нам: \n"
                                          "@rallen\n")


def hello(message):
    bot.send_message(message.chat.id, "Ваше приложение проверяется!\n"
                                      "Нам нужно чуть больше времени на проверку...\n")
    try:
        name_of_app = message.text
        try:
            # r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app))
            r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app) + "&c=apps")
            html = BeautifulSoup(r.content, "html.parser")
        except Exception as e:
            print(e)
            print("Совпадений нет,проверте правильность введения названия")
            bot.send_message(message.chat.id, "Мы не смогли найти такого приложения,\n"
                                              "проверьте правильность его названия включая регист!.")
        n = 0
        a = 0
        k = 0
        massiv = []
        global massivimg
        massivimg = []
        namber_of_element = []
        namber_of_img = []
        for el in html.select(".RZEgze"):
            # print(el)
            n = n + 1
            t_min = el.select(".WsMG1c.nnK0zc")[0].text
            # k = [t_min for i in range(n)]
            massiv.append(t_min)
            # t_min2 = el.select(".temperature .min")[n].text
            # print(n, t_min)
        print(massiv)
        try:
            for nom in massiv:
                if nom == str(name_of_app):
                    namber_of_element.append(a)
                    print(a, nom)
                a = a + 1
            print(namber_of_element)
            # namber_of_element = massiv.index(str(name_of_app))
        except Exception as e:
            print(e)
            print("........Ошибка Google Play........")
        if str(message.text) not in massiv:
            print("........Этого приложения нету в Google Play........")
            bot.send_message(message.chat.id, "Такого приложения не найдено в Google Play")
        else:
            for app in namber_of_element:
                print(app)
                print(massiv[app])
                if massiv[app] == str(name_of_app):
                    try:
                        for el in html.find_all('img'):
                            link = el['data-src']
                            k = k + 1
                            link2 = str(link)
                            massivimg.append(link2)
                            # t_min2 = el.select(".temperature .min")[n].text
                            # print(k, link2)
                    except Exception as e:
                        print(e)
                    print(massivimg)
                    url = massivimg[app * 3]
                    # url = "http://risovach.ru/upload/2014/02/mem/muzhik-bleat_43233947_orig_.jpg"
                    img = urllib.request.urlopen(url).read()
                    out = open("img.jpg", "wb")
                    out.write(img)
                    out.close()
                    img2 = open('img.jpg', 'rb')
                    bot.send_photo(message.chat.id, img2)
                    bot.send_message(message.chat.id,
                                     f'№: {app}\n'
                                     f'{name_of_app}')
                    global reset_name_of_app
                    reset_name_of_app = name_of_app
            sent = bot.send_message(message.chat.id, 'Введите номер (№) вашего приложения\n'
                                                     'из предложенного выше списка\n'
                                                     'Например:1 или 8\n')
            bot.register_next_step_handler(sent, addAppImg)
    except Exception as e:
        print(e)
        print("........Ошибка,попробуйте снова........")
        bot.send_message(message.chat.id, "Упс, произошла какая-то ошибка, попробуйте еще раз.")


def addAppImg(message):
    try:
        open(str(message.chat.id) + 'problem.txt', 'a').write(reset_name_of_app + "\n")
        open(str(message.chat.id) + 'url.txt', 'a').write(massivimg[int(message.text)*3] + "\n")
        url = massivimg[int(message.text)*3]
        img = urllib.request.urlopen(url).read()
        out = open("img.jpg", "wb")
        out.write(img)
        out.close()
        img2 = open('img.jpg', 'rb')
        bot.send_photo(message.chat.id, img2)
        bot.send_message(message.chat.id, 'Ваше приложение успешно добавлено :)')
    except Exception as e:
        print(e)
        print("........Ошибка,неверный ввод номера приложения........")
        bot.send_message(message.chat.id, "Упс, вы ввели неверный номер приложения,попробуйте снова.")


# --------------------------------------------------------------✍🏻ВРУЧНУЮ------------------------------------------------------------------------------------------------


def chek_app(message):
    try:
        open(str(message.chat.id) + 'onetestapp.txt', 'w').write(message.text + "\n")
        bot.send_message(message.chat.id, 'Ваше приложение проверяется!\n'
                                          'Нам нужно чуть больше времени на проверку...\n')
        name_of_app = message.text
        try:
            # r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app))
            r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app) + "&c=apps")
            html = BeautifulSoup(r.content, "html.parser")
        except Exception as e:
            print(e)
            print("Совпадений нет,проверте правильность введения названия")
            bot.send_message(message.chat.id,
                             "Мы не смогли найти такого приложения, проверьте правильность его названия включая регистр.")
        n = 0
        a = 0
        k = 0
        massiv = []
        massivimg = []
        namber_of_element = []
        namber_of_img = []
        for el in html.select(".RZEgze"):
            # print(el)
            n = n + 1
            t_min = el.select(".WsMG1c.nnK0zc")[0].text
            # k = [t_min for i in range(n)]
            massiv.append(t_min)
            # t_min2 = el.select(".temperature .min")[n].text
            # print(n, t_min)
        print(massiv)
        try:
            if name_of_app not in massiv:
                bot.send_message(message.chat.id, "Мы не смогли найти такого приложения, скорей всего оно удалено")
            else:
                for nom in massiv:
                    if nom == str(name_of_app):
                        namber_of_element.append(a)
                        print(a, nom)
                    a = a + 1
                print(namber_of_element)
                # namber_of_element = massiv.index(str(name_of_app))
        except Exception as e:
            print(e)
            print("........Ошибка........")
            bot.send_message(message.chat.id, "Ошибка проверки,обратитесь в поддержку!")
        # print(massiv[int(namber_of_element)], " Элемент под этим номером")
        for app in namber_of_element:
            print(app)
            print(massiv[app])
            if massiv[app] == str(name_of_app):
                try:
                    for el in html.find_all('img'):
                        link = el['data-src']
                        k = k + 1
                        link2 = str(link)
                        massivimg.append(link2)
                        # t_min2 = el.select(".temperature .min")[n].text
                        # print(k, link2)
                except Exception as e:
                    print(e)
                print(massivimg)
                url = massivimg[app * 3]
                # url = "http://risovach.ru/upload/2014/02/mem/muzhik-bleat_43233947_orig_.jpg"
                img = urllib.request.urlopen(url).read()
                out = open("img.jpg", "wb")
                out.write(img)
                out.close()
                img2 = open('img.jpg', 'rb')
                print("........Нашел приложение!........")
                bot.send_message(message.chat.id, "Мы нашли такое приложение")
                bot.send_photo(message.chat.id, img2)
                bot.send_message(message.chat.id, name_of_app)
            # print(massiv.count(str(name_of_app)))
    except Exception as e:
        print(e)
        print("........Ошибка,попробуйте снова........")
        bot.send_message(message.chat.id, "Такого приложения не найдено "
                                          "в Google Play")


# --------------------------------------------------------------------------❌УДАЛИТЬ------------------------------------------------------------------------------------          bot.send_message(message.chat.id, "........Ошибка,удаления, проверте правильность ввода........")


def enter_app_to_dell(message):
    try:
        schet = 0
        with open(str(message.chat.id) + 'problem.txt', 'r') as f:
            data = f.readlines()
            print(data)
            if str(message.text + "\n") not in data:
                bot.send_message(message.chat.id, "Такого приложения в вашем списке нет")
            else:
                for namber in data:
                    x = namber
                    print(x, "x")
                    if x == str(message.text+"\n"):
                        with open(str(message.chat.id) + 'url.txt', 'r') as p:
                            for i in range(int(schet)):
                                p.readline()
                            y = p.readline()
                            print(y)
                            p.close()
                            with open(str(message.chat.id) + 'problem.txt', 'r') as o:
                                data = o.readlines()
                            data = filter(lambda line: x not in line, data)
                            with open(str(message.chat.id) + 'problem.txt', 'w') as o:
                                o.write("".join(data))

                            with open(str(message.chat.id) + 'url.txt', 'r') as m:
                                data2 = m.readlines()
                            data2 = filter(lambda line: y not in line, data2)
                            with open(str(message.chat.id) + 'url.txt', 'w') as m:
                                m.write("".join(data2))
                                bot.send_message(message.chat.id, "Приложение удалено из вашего списка")
                                bot.send_message(message.chat.id, x)
                    else:
                        schet = schet+1
    except Exception as e:
        print(e)
        print("........Ошибка,удаления, проверте правильность ввода........")
        bot.send_message(message.chat.id,
                         "Мы не нашли совпадений, проверте правильность введения названия учитывая регистр")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    bot.polling(none_stop=True)
