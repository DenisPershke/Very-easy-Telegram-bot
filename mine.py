import telebot
import random

# Замените 'YOUR_BOT_TOKEN' на ваш токен от BotFather
bot_token = ''
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    bot.reply_to(message, f"Привет, {user.first_name}! Я твій персональний бот. Щоб дізнатись про мої можливості, напишіть  /help.")

# Обработка команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Для користувачей-\n\n Я можу сгенерувати случайное число от 1 до 100. Відправьть мені команду /random.\n\n Для Інформации /info \n\n Update Skoro")

@bot.message_handler(commands=['info'])
def handle_text(message):
    bot.reply_to(message, 'Команда /Love, Командля для вибора рандомного числа /random, /help')
@bot.message_handler(commands=['random'])
def handle_random(message):
    random_number = random.randint(1, 100)
    bot.reply_to(message, f"Случайное число: {random_number}")

@bot.message_handler(func=lambda message: True)
def handle_text(message): 
    bot.reply_to(message, "Извини, я не понимаю эту команду. Попробуй команду /help для списка доступных команд.")

if __name__ == "__main__":
    bot.polling(none_stop=True)