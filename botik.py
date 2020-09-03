import telebot
import time
from selenium import webdriver
from telebot import types
from PIL import Image

bot = telebot.TeleBot('1225868162:AAFzDPd9Tckx5lN7F2uYYy3WiBMjMdp9Dmo')

photo = r'screenshot.png'
angl_liga = 'https://www.google.ru/search?newwindow=1&ei=TeM6X7rIJNDMrgSpn6KICA&q=%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0+%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D0%B3%D0%B0+&oq=%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0+%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D0%B3%D0%B0+&gs_lcp=CgZwc3ktYWIQAzIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgQIABBHOgQIABBDOgcIABBDEIsDOgUIABCLAzoCCAA6BAgAEAo6BAgAEA06BggAEA0QHjoICAAQCBANEB46CAgAEBYQChAeUIDdAliM_gJg2YEDaANwAXgAgAFliAGDDJIBBDIwLjGYAQCgAQGqAQdnd3Mtd2l6uAECwAEB&sclient=psy-ab&ved=0ahUKEwj6ovv2hKPrAhVQposKHamPCIEQ4dUDCAw&uact=5#sie=lg;/g/11fj6snmjm;2;/m/02_tc;st;fp;1;;'
rus_liga = 'https://www.google.ru/search?newwindow=1&ei=PZQ7X9buDs-r3AP_-o-ABQ&q=%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0+%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D0%B3%D0%B0&oq=%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0+%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D0%B3%D0%B0&gs_lcp=CgZwc3ktYWIQAzIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIECAAQHjIICAAQBxAFEB4yCAgAEAcQBRAeMggIABAHEAUQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjoECAAQRzoFCAAQiwM6CQgAEAcQHhCLAzoECAAQDToICAAQBxAKEB46CAgAEAgQBxAeUKne8QFYmvDxAWDM8fEBaABwAXgAgAGOAYgB5QaSAQQxMS4xmAEAoAEBqgEHZ3dzLXdpergBAsABAQ&sclient=psy-ab&ved=0ahUKEwiWgc7VraTrAhXPFXcKHX_9A1AQ4dUDCAw&uact=5#sie=lg;/g/11hgcnjdr_;2;/m/04cz95;st;fp;1;;'
fr_liga = 'https://www.google.ru/search?newwindow=1&ei=uaM7X6HrKo243APf_LToBw&q=%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0+%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D0%B3%D0%B0&oq=%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0+%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D1%81%D0%BA%D0%B0%D1%8F+%D0%BB%D0%B8%D0%B3%D0%B0&gs_lcp=CgZwc3ktYWIQAzICCAAyBggAEAUQHjIGCAAQBRAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46BAgAEEc6BAgAEA06BggAEAcQHjoJCAAQBxAeEIsDOgUIABCLAzoICAAQCBAHEB5QnpIKWN2hCmD0ogpoAHABeACAAWuIAf8HkgEEMTIuMZgBAKABAaoBB2d3cy13aXq4AQLAAQE&sclient=psy-ab&ved=0ahUKEwjhq4G4vKTrAhUNHHcKHV8-DX0Q4dUDCAw&uact=5#sie=lg;/g/11k0stt2sn;2;/m/044hzk;st;fp;1;;'

def save_screnshot(url):
    chromedriver = r"C:\Users\gondo\Desktop\chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver)
    driver.get(url)
    driver.save_screenshot('sqreenshot.png')
    driver.quit()


def crop_screen():
    img = Image.open('sqreenshot.png')
    crop_img = img.crop((182, 211, 1090, 762))
    crop_img.save('sqreenshot.png')


@bot.message_handler(commands=['start'])
def echo_text(message):
    bot.send_message(message.chat.id, 'Добро пожаловать', reply_markup=keyboard())


def keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Английская лига')
    btn2 = types.KeyboardButton('Российская лига')
    btn3 = types.KeyboardButton('Французская лига')
    markup.add(btn1, btn2, btn3)
    return markup


@bot.message_handler(content_types=["text"])
def send_result(message):
    if message.text == 'Английская лига':
        if time.sleep(5):
            save_screnshot(angl_liga)
            crop_screen()
            bot.send_photo(message.chat.id, open('sqreenshot.png', 'rb'))
        else:
            bot.send_message(message.chat.id,'Не нажимайте так часто')
    elif message.text == 'Российская лига':
        save_screnshot(rus_liga)
        crop_screen()
        bot.send_photo(message.chat.id, open('sqreenshot.png', 'rb'))
    elif message.text == 'Французская лига':
        save_screnshot(fr_liga)
        crop_screen()
        bot.send_photo(message.chat.id, open('sqreenshot.png', 'rb'))


bot.polling()
