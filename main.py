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
        host="q2gen47hi68k1yrb.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="sftt638drm8psv1v",
        passwd="ncshyhrvpqatr5xp",
        port="3306",
        database="sx98ct5sc1nucpjd"
    )
    print(db)
    cursor = db.cursor()
except Exception as e:
    print(e)
    print("Ошибка подключения к базе данных")

# cursor.execute("CREATE DATABASE users")

# cursor.execute("SHOW DATABASES")
# for x in cursor:
#   print(x)

# cursor.execute("CREATE TABLE user (id_user INT, status INT)")

# cursor.execute("SHOW TABLES")
# for x in cursor:
#   print(x)

# cursor.execute("ALTER TABLE user ADD COLUMN (id INT AUTO_INCREMENT PRIMARY KEY, id_user INT UNIQUE)")


# sql = "INSERT INTO user (id_user, status, offtime) VALUES (%s, %s, %s)"
# val = (398051266, 2, "2020.04.22")
# cursor.execute(sql, val)
# db.commit()
# print(cursor.rowcount, "Запись добавена")

# sql = "INSERT INTO user (id_user, status, offtime) VALUES (%s, %s, %s)"
# val = [
#   (338051266, 2, "2020.04.22"),
#   (394051266, 2, "2020.04.22"),
#   (398071266, 2, "2020.04.22"),
#   (378058266, 2, "2020.04.22"),
# ]
# cursor.executemany(sql, val)
# db.commit()
# print(cursor.rowcount, "was inserted.")

id = []
status = []
day_off = []


try:
    cursor.execute("SELECT * FROM user")
    result = cursor.fetchall()
    for x in result:
        print(x)

    cursor.execute("SELECT id FROM user")
    result = cursor.fetchall()
    for x in result:
        print(x)

    cursor.execute("SELECT id_user FROM user")
    result = cursor.fetchall()
    id.clear()
    for x in result:
        print(x)
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
# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080",
# }
#
# requests.get("http://www.google.com/", proxies=proxies)

# global id_of_new_user
# id_of_new_user = 10
# global user_status
# user_status = 10
# 398051266

global defalt_status
defalt_status = 0
global defalt_data
defalt_data = 0

cheker = 0
bot = telebot.TeleBot(constants.token)


# try:
#     r = requests.get("https://docs.google.com/spreadsheets/d/1OF_eQiUhIGTtpkB5e9qX8woUVLS4sQeVzvJt_CeuIUw/edit?usp=sharing")
#     html = BS(r.content, "html.parser")
#     # print(html)
# except Exception as e:
#     print(e)
# for el in html.select(".cell-input"):
#     print(html)
#     print("fghjkl")
#     users = el.select(".cell-input.editable")[0].text
#     id.append(users)
#     print(users)


# s = sched.scheduler(time.time, time.sleep)


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
    except Exception as e:
        print(e)
        kreate = open(str(message.chat.id) + 'problem.txt', 'tw', encoding='utf-8')
        kreate.close()
    chen_id = "(" + str(message.chat.id) + ",)"
    print(chen_id)
    print(id)
    if str(chen_id) not in str(id):
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron3239, сообщите ваш ID:\n"
                                          "После предоставления доступа\n"
                                          "нажмите /start\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Начнем работу!")

        def chek_data():
            threading.Timer(3600.0, chek_data).start()
            print("Работает")

            now2 = datetime.datetime.now()
            global now_month2
            now_month2 = now2.month
            global now_day2
            now_day2 = now2.day

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
                global  do_kogda
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
                    sql = "UPDATE user SET status = %s WHERE offtime = %s"
                    val = ("0", str(now_day2))
                    cursor.execute(sql, val)
                    db.commit()
                    print(cursor.rowcount, "record(s) affected")
                except Exception as e:
                    print(e)
                    print("Ошибка обновления данных в бд")

                bot.send_message(message.chat.id, "У вас закончилось время действия тарифа\n"
                                                  "Продлите его или же удалите приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif str(do_kogda) == str("(" + str(now_day2) + ",)"):

                try:
                    sql1 = "UPDATE user SET status = %s WHERE offtime = %s"
                    val1 = ("0", str(now_day2))
                    cursor.execute(sql1, val1)
                    db.commit()
                    print(cursor.rowcount, "record(s) affected")
                except Exception as e:
                    print(e)
                    print("Ошибка обновления данных в бд")
                bot.send_message(message.chat.id, "У вас закончилось время действия тарифа\n"
                                                  "Продлите его или же удалите приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif now_status2 == (3,):
                print("Статус ВИП")
            elif now_status2 == (2,) and lenf > 10:
                bot.send_message(message.chat.id, "Количество приложений в вашем списке не\n"
                                                  "соотвецтвует количеству,предусмотренного\n"
                                                  "вашим тарифом\n"
                                                  "Возможно, закончился срок действия вашего тарифа\n"
                                                  "Продлите его или же удалите приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif now_status2 == (1,) and lenf > 5:
                bot.send_message(message.chat.id, "Количество приложений в вашем списке не\n"
                                                  "соотвецтвует количеству,предусмотренного\n"
                                                  "вашим тарифом\n"
                                                  "Возможно, закончился срок действия вашего тарифа\n"
                                                  "Продлите его или же удалите приложения\n"
                                                  "с листа проверок до разрешенного количества\n"
                                                  "по текущему тарифу\n"
                                                  "Ознакомится с дополнительной информацией\n"
                                                  "можно в разделе главного меню\n"
                                                  "👑 ТАРИФЫ\n")
            elif now_status2 == (0,) and lenf > 1:
                bot.send_message(message.chat.id, "Количество приложений в вашем списке не\n"
                                                  "соотвецтвует количеству,предусмотренного\n"
                                                  "вашим тарифом\n"
                                                  "Возможно, закончился срок действия вашего тарифа\n"
                                                  "Продлите его или же удалите приложения\n"
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
            elif now_status2 == (3,):
                print("Статус ВИП")
            elif now_status2 == (2,) and lenf > 10:
                print("Срок действия тарифа истек/лишнее приложение")
            elif now_status2 == (1,) and lenf > 5:
                print("Срок действия тарифа истек/лишнее приложение")
            elif now_status2 == (0,) and lenf > 1:
                print("Срок действия тарифа истек/лишнее приложение")
            else:
                try:
                    print("Doing ", message.chat.id)
                    list_of_apps = open(str(message.chat.id) + 'problem.txt', 'r').readlines()
                    leng = len(list_of_apps)
                    print(leng)
                    # if leng == 0:
                    #     print("Список пуст,я жду")
                    # else:
                    # list_of_apps.clear() не помню зачем надо
                    for nambers in range(leng):
                        with open(str(message.chat.id) + 'problem.txt', 'r') as f:
                            for i in range(int(nambers)):
                                f.readline()
                            x = f.readline()
                            print(x)
                            f.close()
                            try:
                                # r = requests.get("https://play.google.com/store/search?q=" + str(x))
                                r = requests.get("https://play.google.com/store/search?q=" + str(x) + "&c=apps")
                                html = BeautifulSoup(r.content, "html.parser")
                            except Exception as e2:
                                print(e2)
                                print("Совпадений нет,проверте правильность введения названия")
                                # bot.send_message(message.chat.id, "Совпадений нет,проверте правильность введения названия")
                            n = 0
                            mass = []
                            namber_of_el = 0
                            for el in html.select(".RZEgze"):
                                # print(el)
                                n = n + 1
                                t_min = el.select(".WsMG1c.nnK0zc")[0].text
                                # k = [t_min for i in range(n)]
                                mass.append(t_min + "\n")
                                # t_min2 = el.select(".temperature .min")[n].text
                                print(n, t_min)
                            print(mass)
                            try:
                                namber_of_el = mass.index(str(x))
                            except Exception as e2:
                                print(e2)
                                print("........Приложение удалено!........ ", x)
                                bot.send_message(message.chat.id, "........Приложение удалено!........")
                                bot.send_message(message.chat.id, "........Удаляю приложение с базы........")
                                try:
                                    with open(str(message.chat.id) + 'problem.txt', 'r') as o:
                                        data = o.readlines()
                                    data = filter(lambda line: x not in line, data)
                                    with open(str(message.chat.id) + 'problem.txt', 'w') as o:
                                        o.write("".join(data))
                                        bot.send_message(message.chat.id, "Приложение успешно удалено!")
                                        bot.send_message(message.chat.id, x)
                                except Exception as e2:
                                    print(e2)
                                    print("........Ошибка,удаления, проверте правильность ввода........")
                                    bot.send_message(message.chat.id,
                                                     "........Ошибка,удаления, проверте правильность ввода........")

                            try:
                                print(mass[int(namber_of_el)], " Элемент под этим номером")
                            except Exception as e2:
                                print(e2)
                                print("........Google Play ничего не нашел ........ ", x)
                                bot.send_message(message.chat.id,
                                                 "........Google Play ничего не "
                                                 "нашел........")
                            try:
                                if mass[int(namber_of_el)] == str(x):
                                    print("........Нашел приложение!........ ", x)
                                    # bot.send_message(message.chat.id, "........Нашел приложение!........")
                                    # bot.send_message(message.chat.id, x)
                            except Exception as e1:
                                print(e1)
                                print("........Скорей всего оно удалено ........ ", x)
                                bot.send_message(message.chat.id,
                                                 "........Скорей всего оно удалено........")
                                bot.send_message(message.chat.id, x)
                except Exception as e2:
                    print(e2)
                    print("........Критическая ошибка при проверки, обратитесь в поддержку........ " + x)
                    bot.send_message(message.chat.id,
                                     "........Критическая ошибка при проверки, обратитесь в поддержку........")
                # s.enter(15, 1, do_my_cod, (sc,))

        do_my_cod()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# t = Timer(10.0, do_my_cod)
# s.enter(15, 1, do_my_cod, (s,))
# s.run()


# @bot.message_handler(commands=["stop"])
# def handle_command(message):
# hid_markup = telebot.types.ReplyKeyboardRemove()
# bot.send_message(message.chat.id, "Заходи еще!"
# "Уведомления отключены, информация удалена!", reply_markup=hid_markup)\

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
        except Exception as e:
            print(e)
            kreate = open(str(message.chat.id) + 'problem.txt', 'tw', encoding='utf-8')
            kreate.close()
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                              "Обратитесь к разработчику\n"
                                              "@andron3239 и сообщите ваш ID:\n")
            bot.send_message(message.chat.id, message.chat.id)
        else:
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
                                            'Введите название приложения учитывая реристры и специальные знаки!')
                    bot.register_next_step_handler(sent, hello)
                elif now_status == (2,) and lenf <= 9:
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая реристры и специальные знаки!')
                    bot.register_next_step_handler(sent, hello)
                elif now_status == (1,) and lenf <= 4:
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая реристры и специальные знаки!')
                    bot.register_next_step_handler(sent, hello)
                elif now_status == (0,) and lenf <= 0:
                    sent = bot.send_message(message.chat.id,
                                            'Введите название приложения учитывая реристры и специальные знаки!')
                    bot.register_next_step_handler(sent, hello)
                else:
                    bot.send_message(message.chat.id,
                                     'Вы исчерпали доступное количество мест в списке приложений\n'
                                     'Перейдите в пункт "👑 ТАРИФЫ" в главном меню \n'
                                     'и закажите новый тариф или тариф более высокого уровня \n')
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
            bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                              "Обратитесь к разработчику\n"
                                              "@andron3239 и сообщите ваш ID:\n")
            bot.send_message(message.chat.id, message.chat.id)
        else:
            sent = bot.send_message(message.chat.id, 'Я проверю это приложение один раз в реальном времени\n'
                                                     'Оно не будет занесено в список ваших приложений и не будет '
                                                     'проверяться\n\n '
                                                     'Введите название приложения учитывая реристры и специальные знаки!')
            bot.register_next_step_handler(sent, chek_app)
    elif message.text == "📖 СПИСОК":
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                              "Обратитесь к разработчику\n"
                                              "@andron3239 и сообщите ваш ID:\n")
            bot.send_message(message.chat.id, message.chat.id)
        else:
            try:
                list_of_apps = open(str(message.chat.id) + 'problem.txt', 'r').read()
                bot.send_message(message.chat.id, 'Понял,обрабатываю\n'
                                                  'Подожди немного!\n')
                bot.send_message(message.chat.id, list_of_apps)
                print(list_of_apps)
            except Exception as e:
                print(e)
                print("........Ваш список пуст........")
                bot.send_message(message.chat.id, "........Ваш список пуст........")
    elif message.text == "❌ УДАЛИТЬ":
        chen_id = "(" + str(message.chat.id) + ",)"
        print(chen_id)
        print(id)
        if str(chen_id) not in str(id):
            bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                              "Обратитесь к разработчику\n"
                                              "@andron3239 и сообщите ваш ID:\n")
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
                                        'Введите название приложения учитывая реристры и специальные знаки!\n')
                bot.register_next_step_handler(sent, enter_app_to_dell)
            except Exception as e:
                print(e)
                print("........Ошибка,удаления, проверте правильность ввода........")
                bot.send_message(message.chat.id, "........Ошибка,удаления, проверте правильность ввода........")
    elif message.text == "👑 ТАРИФЫ":
        chen_id = "(" + str(message.chat.id) + ",)"
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
                                          "\nДля потльзования этим ботом, вы должны выбрать один из тарифов: \n"
                                          "\n"
                                          "0 - ОБЫЧНЫЙ: Бесплатно, отслеживание\n"
                                          "одного приложения, доступо всем\n"
                                          "пользователям автоматически.\n"
                                          "\n"
                                          "1 - ПРЕМИУМ: 5 USD/месяц, отслеживание пяти\n"
                                          "приложений\n"
                                          "\n"
                                          "2 - ПРЕМИУМ +: 10 USD/месяц, отслеживание десяти\n"
                                          "приложений\n"
                                          "\n"
                                          "3- 👑 ВИП 👑: Бесплатно, отслеживание безлимитного\n"
                                          "количества приложений.\n"
                                          "\n"
                                          "Для заказа/изменения тарифа, пишите:\n"
                                          "@iBUYAPPS \n"
                                          f'и сообщите ваш ID: {message.chat.id}')

    elif message.text == "🛎 ПОДДЕРЖКА":
        bot.send_message(message.chat.id, "Привет, Друг!\n"
                                          "Если у тебя возникли вопросы, напиши нам: \n"
                                          "@ibuyapps\n")


def hello(message):
    bot.send_message(message.chat.id, "Секундочку, поверяю приложение...")
    try:
        name_of_app = message.text
        try:
            # r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app))
            r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app) + "&c=apps")
            html = BeautifulSoup(r.content, "html.parser")
        except Exception as e:
            print(e)
            print("Совпадений нет,проверте правильность введения названия")
            bot.send_message(message.chat.id, "Совпадений нет,проверте правильность введения названия")
        n = 0
        k = 0
        massiv = []
        massivimg = []
        namber_of_element = 0
        namber_of_img = []
        for el in html.select(".RZEgze"):
            # print(el)
            n = n + 1
            t_min = el.select(".WsMG1c.nnK0zc")[0].text
            # k = [t_min for i in range(n)]
            massiv.append(t_min)
            # t_min2 = el.select(".temperature .min")[n].text
            print(n, t_min)
        print(massiv)
        try:
            namber_of_element = massiv.index(str(name_of_app))
        except Exception as e:
            print(e)
            print("........Этого приложения нету в Google Play........")
            bot.send_message(message.chat.id, "........Этого приложения нету в Google Play........")
        print(massiv[int(namber_of_element)], " Элемент под этим номером")
        if massiv[int(namber_of_element)] == str(name_of_app):
            try:
                for el in html.find_all('img'):
                    link = el['data-src']
                    k = k + 1
                    link2 = str(link)
                    massivimg.append(link2)
                    # t_min2 = el.select(".temperature .min")[n].text
                    print(k, link2)
            except Exception as e:
                print(e)
            print(massivimg)
            url = massivimg[int(1)]
            # url = "http://risovach.ru/upload/2014/02/mem/muzhik-bleat_43233947_orig_.jpg"
            img = urllib.request.urlopen(url).read()
            out = open("img.jpg", "wb")
            out.write(img)
            out.close()
            img2 = open('img.jpg', 'rb')
            bot.send_photo(message.chat.id, img2)
            bot.send_message(message.chat.id, name_of_app)
            # print(massiv.count(str(name_of_app)))
            open(str(message.chat.id) + 'problem.txt', 'a').write(message.text + "\n")
            bot.send_message(message.chat.id, 'Приложение успешно добавлено!')
    except Exception as e:
        print(e)
        print("........Ошибка,попробуйте снова........")
        bot.send_message(message.chat.id, "........Ошибка,попробуйте снова........")


# --------------------------------------------------------------✍🏻ВРУЧНУЮ------------------------------------------------------------------------------------------------
# @bot.message_handler(content_types=["text"])
# def handle_command(message):
#     if message.text == "✍🏻 ВРУЧНУЮ":
#         try:
#             file = open(str(message.chat.id) + 'onetestapp.txt')
#         except Exception as e:
#             print(e)
#             kreate = open(str(message.chat.id) + 'onetestapp.txt', 'tw', encoding='utf-8')
#             kreate.close()
#         if message.chat.id not in id:
#             bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
#                                               "Обратитесь к разработчику\n"
#                                               "@andron3239 и сообщите ваш ID:\n")
#             bot.send_message(message.chat.id, message.chat.id)
#         else:
#             sent = bot.send_message(message.chat.id, 'Я проверю это приложение один раз в реальном времени\n'
#                                                      'Оно не будет занесено в список ваших приложений и не будет '
#                                                      'проверяться\n\n '
#                                                      'Введите название приложения учитывая реристры и специальные знаки!')
#             bot.register_next_step_handler(sent, chek_app)


def chek_app(message):
    try:
        open(str(message.chat.id) + 'onetestapp.txt', 'w').write(message.text + "\n")
        bot.send_message(message.chat.id, 'Понял,обрабатываю\n'
                                          'Подожди немного!')
        name_of_app = message.text
        try:
            # r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app))
            r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app) + "&c=apps")
            html = BeautifulSoup(r.content, "html.parser")
        except Exception as e:
            print(e)
            print("Совпадений нет,проверте правильность введения названия")
            bot.send_message(message.chat.id, "Совпадений нет,проверте правильность введения названия")
        n = 0
        k = 0
        massiv = []
        massivimg = []
        namber_of_element = 0
        namber_of_img = []
        for el in html.select(".RZEgze"):
            # print(el)
            n = n + 1
            t_min = el.select(".WsMG1c.nnK0zc")[0].text
            # k = [t_min for i in range(n)]
            massiv.append(t_min)
            # t_min2 = el.select(".temperature .min")[n].text
            print(n, t_min)
        print(massiv)
        try:
            namber_of_element = massiv.index(str(name_of_app))
        except Exception as e:
            print(e)
            print("........Приложение удалено!........")
            bot.send_message(message.chat.id, "........Приложение удалено!........")
        print(massiv[int(namber_of_element)], " Элемент под этим номером")
        if massiv[int(namber_of_element)] == str(name_of_app):
            try:
                for el in html.find_all('img'):
                    link = el['data-src']
                    k = k + 1
                    link2 = str(link)
                    massivimg.append(link2)
                    # t_min2 = el.select(".temperature .min")[n].text
                    print(k, link2)
            except Exception as e:
                print(e)
            print(massivimg)
            url = massivimg[int(1)]
            # url = "http://risovach.ru/upload/2014/02/mem/muzhik-bleat_43233947_orig_.jpg"
            img = urllib.request.urlopen(url).read()
            out = open("img.jpg", "wb")
            out.write(img)
            out.close()
            img2 = open('img.jpg', 'rb')
            print("........Нашел приложение!........")
            bot.send_message(message.chat.id, "........Нашел приложение!........")
            bot.send_photo(message.chat.id, img2)
            bot.send_message(message.chat.id, name_of_app)
        # print(massiv.count(str(name_of_app)))
    except Exception as e:
        print(e)
        print("........Ошибка,попробуйте снова........")
        bot.send_message(message.chat.id, "........Ошибка,попробуйте снова........")


# --------------------------------------------------------------------📖СПИСОК------------------------------------------------------------------------------------------
@bot.message_handler(commands=["seemyapps"])
def handle_command(message):
    if message.chat.id not in id:
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron3239 и сообщите ваш ID:\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        try:
            list_of_apps = open(str(message.chat.id) + 'problem.txt', 'r').read()
            bot.send_message(message.chat.id, 'Понял,обрабатываю\n'
                                              'Подожди немного!\n')
            bot.send_message(message.chat.id, list_of_apps)
            print(list_of_apps)
        except Exception as e:
            print(e)
            print("........Ваш список пуст........")
            bot.send_message(message.chat.id, "........Ваш список пуст........")


# --------------------------------------------------------------------------❌УДАЛИТЬ------------------------------------------------------------------------------------
# @bot.message_handler(content_types=["text"])
# def handle_commandsds(message):
#     if message.text == "❌ УДАЛИТЬ":
#         if message.chat.id not in id:
#             bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
#                                               "Обратитесь к разработчику\n"
#                                               "@andron3239 и сообщите ваш ID:\n")
#             bot.send_message(message.chat.id, message.chat.id)
#         else:
#             try:
#                 try:
#                     file = open(str(message.chat.id) + "problem.txt")
#                 except Exception as e:
#                     print(e)
#                     kreate = open(str(message.chat.id) + 'problem.txt', 'tw', encoding='utf-8')
#                     kreate.close()
#                 sent = bot.send_message(message.chat.id,
#                                         'Введите название приложения учитывая реристры и специальные знаки!\n\n'
#                                         '                Внимание!!! \n'
#                                         'Я не отслеживаю правильность введения названия в даном разделе'
#                                         'рекомендую проверить удаление командой: \n'
#                                         '/seemyapps \n'
#                                         'после завершения удаления')
#                 bot.register_next_step_handler(sent, enter_app_to_dell)
#             except Exception as e:
#                 print(e)
#                 print("........Ошибка,удаления, проверте правильность ввода........")
#                 bot.send_message(message.chat.id, "........Ошибка,удаления, проверте правильность ввода........")


def enter_app_to_dell(message):
    try:
        with open(str(message.chat.id) + 'problem.txt', 'r') as f:
            data = f.readlines()
            print(data)
            if str(message.text + "\n") not in data:
                bot.send_message(message.chat.id, "Такого приложения нет в списке")
            else:
                data = filter(lambda line: message.text not in line, data)
                print(data)
                with open(str(message.chat.id) + 'problem.txt', 'w') as f:
                    f.write("".join(data))
                    bot.send_message(message.chat.id, "Приложение успешно удалено!")
    except Exception as e:
        print(e)
        print("........Ошибка,удаления, проверте правильность ввода........")
        bot.send_message(message.chat.id, "........Ошибка,удаления, проверте правильность ввода........")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    bot.polling(none_stop=True)
