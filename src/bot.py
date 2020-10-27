import telebot
from env import TOKEN
from services.github_api  import GitHubApi

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['vagas'])
def send_jobs(message):
    jobs = GitHubApi().get_jobs()[:10]
    for job in jobs:
        bot.reply_to(message, job)


if __name__ == '__main__':
    bot.polling()
