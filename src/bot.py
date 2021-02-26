import telebot
import env
from services.github_api import GitHubApi
from msgs import bot_msgs as msg
from random import choice

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
            msg.NOT_JOBS_MSG,
            disable_web_page_preview=None,
        )


@bot.message_handler(commands=['about'])
def about_me(message):
    bot.send_message(message.chat.id, msg.ABOUT_MSG)


@bot.message_handler(commands=['last'])
def get_last_jobs(message):
    num_jobs = message.text.split(' ')
    if (len(num_jobs) > 1):
        try:
            range_jobs = int(num_jobs[1])
            if (range_jobs <= 10 and range_jobs != 0):
                jobs = GitHubApi().last_jobs(range_jobs)
                bot.send_message(
                    message.chat.id,
                    jobs,
                    disable_web_page_preview=True
                )
            else:
                raise ValueError

        except ValueError:
            bot.send_message(message.chat.id, 'Informe um valor entre 1 e 10')
            bot.send_message(
                message.chat.id,
                jobs,
                disable_web_page_preview=True
            )


@bot.message_handler(commands=['hint'])
def get_hint(message):
    bot.send_message(
        message.chat.id,
        choice(msg.HINTS_MSG),
        disable_web_page_preview=True
    )


if __name__ == '__main__':
    bot.polling()
