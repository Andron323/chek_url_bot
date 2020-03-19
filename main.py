import constants
import telebot
import requests
from bs4 import BeautifulSoup as BS
import sched
import time

# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080",
# }
#
# requests.get("http://www.google.com/", proxies=proxies)

id = []
# 398051266

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

s = sched.scheduler(time.time, time.sleep)


@bot.message_handler(commands=["start"])
def handle_commanddd(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row("/start", "/admin")
    user_markup.row("/addapp", "/dellapp")
    user_markup.row("/chekapp", "/seemyapps")
    bot.send_message(message.chat.id, "Привет!", reply_markup=user_markup)
    if message.chat.id not in id:
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron323 и сообщите ваш ID:\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Начнем работу!")

        def do_my_cod(sc):
            try:
                print("Doing")
                list_of_apps = open('problem.txt', 'r').readlines()
                leng = len(list_of_apps)
                print(leng)
                list_of_apps.clear()
                for nambers in range(leng):
                    with open('problem.txt', 'r') as f:
                        for i in range(int(nambers)):
                            f.readline()
                        x = f.readline()
                        print(x)
                        f.close()
                        try:
                            r = requests.get("https://play.google.com/store/search?q=" + str(x))
                            html = BS(r.content, "html.parser")
                        except Exception as e:
                            print(e)
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
                        except Exception as e:
                            print(e)
                            print("........Приложение удалено!........ ", x)
                            bot.send_message(message.chat.id, "........Приложение удалено!........")
                            bot.send_message(message.chat.id, "........Удаляю приложение с базы........")
                            try:
                                with open('problem.txt', 'r') as o:
                                    data = o.readlines()
                                data = filter(lambda line: x not in line, data)
                                with open('problem.txt', 'w') as o:
                                    o.write("".join(data))
                                    bot.send_message(message.chat.id, "Приложение успешно удалено!")
                                    bot.send_message(message.chat.id, x)
                            except Exception as e:
                                print(e)
                                print("........Ошибка,удаления, проверте правильность ввода........")
                                bot.send_message(message.chat.id,
                                                 "........Ошибка,удаления, проверте правильность ввода........")

                        try:
                            print(mass[int(namber_of_el)], " Элемент под этим номером")
                        except Exception as e:
                            print(e)
                            print("........Ошибка,проверки приложений, Google Play ничего не нашел ........ ", x)
                            bot.send_message(message.chat.id,
                                             "........Ошибка,проверки приложений, Google Play ничего не "
                                             "нашел........")
                        try:
                            if mass[int(namber_of_el)] == str(x):
                                print("........Нашел приложение!........ ", x)
                                bot.send_message(message.chat.id, "........Нашел приложение!........")
                                bot.send_message(message.chat.id, x)
                            # print(massiv.count(str(name_of_app)))
                        except Exception as e:
                            print(e)
                            print("........Скорей всего оно удалено ........ ", x)
                            bot.send_message(message.chat.id,
                                             "........Ошибка,проверки приложений, Google Play ничего не "
                                             "нашел........")
            except Exception as e:
                print(e)
                print("........Критическая ошибка при проверки, обратитесь в плоддержку........ " + x)
                bot.send_message(message.chat.id,
                                 "........Критическая ошибка при проверки, обратитесь в плоддержку........")
            s.enter(15, 1, do_my_cod, (sc,))

        s.enter(15, 1, do_my_cod, (s,))
        s.run()


# @bot.message_handler(commands=["stop"])
# def handle_command(message):
# hid_markup = telebot.types.ReplyKeyboardRemove()
# bot.send_message(message.chat.id, "Заходи еще!"
# "Уведомления отключены, информация удалена!", reply_markup=hid_markup)\


@bot.message_handler(commands=["admin"])
def handle_command(message):
    sent = bot.send_message(message.chat.id, 'Введите пароль администратора')
    bot.register_next_step_handler(sent, admin_user)


def admin_user(message):
    in_pas = message.text
    if in_pas == constants.pas:
        bot.send_message(message.chat.id, 'Принято! ID пользователя добавлен\n'
                                          'Для начала работы нажмите:\n'
                                          '/start')
        id.append(message.chat.id)
        print(id)
    else:
        bot.send_message(message.chat.id, 'Не верный пароль!\n'
                                          'Попробуйте еще раз;\n'
                                          '/admin ')


@bot.message_handler(commands=["addapp"])
def handle_command(message):
    if message.chat.id not in id:
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron323 и сообщите ваш ID:\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        sent = bot.send_message(message.chat.id, 'Введите название приложения учитывая реристры и специальные знаки!')
        bot.register_next_step_handler(sent, hello)


def hello(message):
    try:
        open('problem.txt', 'a').write(message.text + "\n")
        bot.send_message(message.chat.id, 'Приложение успешно добавлено!')
    except Exception as e:
        print(e)
        print("........Ошибка,попробуйте снова........")
        bot.send_message(message.chat.id, "........Ошибка,попробуйте снова........")


@bot.message_handler(commands=["chekapp"])
def handle_command(message):
    if message.chat.id not in id:
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron323 и сообщите ваш ID:\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        sent = bot.send_message(message.chat.id, 'Я проверю это приложение один раз в реальном времени\n'
                                                 'Оно не будет занесено в список ваших приложений и не будет '
                                                 'проверяться\n\n '
                                                 'Введите название приложения учитывая реристры и специальные знаки!')
        bot.register_next_step_handler(sent, chek_app)


def chek_app(message):
    try:
        open('onetestapp.txt', 'w').write(message.text + "\n")
        bot.send_message(message.chat.id, 'Понял,обрабатываю'
                                          'Подожди немного!')
        name_of_app = message.text
        try:
            r = requests.get("https://play.google.com/store/search?q=" + str(name_of_app))
            html = BS(r.content, "html.parser")
        except Exception as e:
            print(e)
            print("Совпадений нет,проверте правильность введения названия")
            bot.send_message(message.chat.id, "Совпадений нет,проверте правильность введения названия")
        n = 0
        massiv = []
        namber_of_element = 0
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
            print("........Нашел приложение!........")
            bot.send_message(message.chat.id, "........Нашел приложение!........")
        # print(massiv.count(str(name_of_app)))
    except Exception as e:
        print(e)
        print("........Ошибка,попробуйте снова........")
        bot.send_message(message.chat.id, "........Ошибка,попробуйте снова........")


@bot.message_handler(commands=["seemyapps"])
def handle_command(message):
    if message.chat.id not in id:
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron323 и сообщите ваш ID:\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        try:
            list_of_apps = open('problem.txt', 'r').read()
            bot.send_message(message.chat.id, 'Понял,обрабатываю\n'
                                              'Подожди немного!\n')
            bot.send_message(message.chat.id, list_of_apps)
            print(list_of_apps)
        except Exception as e:
            print(e)
            print("........Ваш список пуст........")
            bot.send_message(message.chat.id, "........Ваш список пуст........")


@bot.message_handler(commands=["dellapp"])
def handle_command(message):
    if message.chat.id not in id:
        bot.send_message(message.chat.id, "У вас нет доступа к данному боту\n"
                                          "Обратитесь к разработчику\n"
                                          "@andron323 и сообщите ваш ID:\n")
        bot.send_message(message.chat.id, message.chat.id)
    else:
        try:
            sent = bot.send_message(message.chat.id,
                                    'Введите название приложения учитывая реристры и специальные знаки!\n\n'
                                    '                Внимание!!! \n'
                                    'Я не отслеживаю правильность введения названия в даном разделе'
                                    'рекомендую проверить удаление командой: \n'
                                    '/seemyapps \n'
                                    'после завершения удаления')
            bot.register_next_step_handler(sent, enter_app_to_dell)
        except Exception as e:
            print(e)
            print("........Ошибка,удаления, проверте правильность ввода........")
            bot.send_message(message.chat.id, "........Ошибка,удаления, проверте правильность ввода........")


def enter_app_to_dell(message):
    try:
        with open('problem.txt', 'r') as f:
            data = f.readlines()
        data = filter(lambda line: message.text not in line, data)
        with open('problem.txt', 'w') as f:
            f.write("".join(data))
            bot.send_message(message.chat.id, "Приложение успешно удалено!")
    except Exception as e:
        print(e)
        print("........Ошибка,удаления, проверте правильность ввода........")
        bot.send_message(message.chat.id, "........Ошибка,удаления, проверте правильность ввода........")


if __name__ == "__main__":
    bot.polling(none_stop=True)
