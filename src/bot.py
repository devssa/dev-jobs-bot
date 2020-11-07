import telebot
import env
from services.github_api import GitHubApi

bot = telebot.TeleBot(env.TOKEN)
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
            env.NOT_JOBS_MSG,
            disable_web_page_preview=True,
        )


@bot.message_handler(commands=['about'])
def about_me(message):
    bot.send_message(message.chat.id, env.ABOUT_MSG)


if __name__ == '__main__':
    bot.polling()
