from random import choice


def parse_jobs(job):
    title = job['title']
    raw_date = job['created_at'].split('T')[0]
    year, month, day = raw_date.split('-')
    link = job['html_url']
    emoji = choice([
                    '👩🏿‍💻', '👨🏿‍💻',
		    '👨🏻‍💻','👩🏻‍💻'
		   ])

    msg = f'{emoji} Vaga: {title}\n'\
          f'📅 Data de publicação: {day}/{month}/{year}\n'\
          f'ℹ️ Mais informações: {link}\n\n'

    return msg


