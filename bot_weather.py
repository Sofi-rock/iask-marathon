import telebot
import requests

# 🔑 Встав сюди свій OpenWeather API ключ
OPENWEATHER_API_KEY = "8ac000cd844f5e1a4518fcd187713de3"

bot = telebot.TeleBot("7743815742:AAHFz4QsFIWhqZzrpREIe2_JPhWNIuTHNOA")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ua"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description']
        return (
            f"🌆 Місто: {city}\n"
            f"🌡 Температура: {temp}°C\n"
            f"🤔 Відчувається як: {feels_like}°C\n"
            f"☁️ Стан: {weather_desc}"
        )
    else:
        return "❌ Не вдалося знайти місто. Перевірте назву."

# Команда /start і /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши /weather [місто], щоб дізнатись погоду по Україні.")

# Команда /weather
@bot.message_handler(commands=['weather'])
def weather(message):
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "Напиши місто після команди, наприклад: /weather Київ")
    else:
        city = " ".join(parts[1:])
        bot.reply_to(message, get_weather(city))

bot.infinity_polling()
