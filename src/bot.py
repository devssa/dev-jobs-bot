import telebot
from env import TOKEN
from services.github_api import GitHubApi
from messages.msgs import about_msg, not_jobs_msg

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()

@bot.message_handler(commands=['jobs'])
def send_jobs(message):
    jobs = GitHubApi().get_jobs()

    if jobs:
        for job in jobs:
            bot.send_message(message.chat.id, job)
    else:
        bot.send_message(
            message.chat.id,
            not_jobs_msg,
            disable_web_page_preview=True,
        )


@bot.message_handler(commands=['about'])
def about_me(message):
    bot.send_message(message.chat.id, about_msg)


if __name__ == '__main__':
    bot.polling()
