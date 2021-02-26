import sys
sys.path.append('..')
import env

NOT_JOBS_MSG = f'''
⚠ ️Nenhuma vaga foi divulgada hoje.

Verifique as vagas dos dias anteriores no repositório da comunidade.
Pode ser que as mesmas ainda não tenham sido preenchidas.

{env.COMMUNITY_GH_ISSUES}
'''

ABOUT_MSG = f'''
{env.BOT_NAME} é um bot para exibir as vagas da área de desenvolvimento e afins divulgadas no GitHub da comunidade {env.COMMUNITY_NAME}.

Site: {env.COMMUNITY_SITE}
GitHub: {env.COMMUNITY_GH}
'''

HINTS_MSG = [
    '"Foque numa tecnologia e fique bom nela, '\
    'evite ficar pulando de uma tecnologia para outra."\n'\
    '— João Paulo',

    '"Seja curiosa(o) e esteja preparada(o) para estar sempre estudando'\
    ' algo novo."\n'\
    '— Elisete Vidotti\n\n'\
    'Github: lizvidotti91',

    '"Estudar sempre e persistência!"\n'\
    '— Jailton Dantas\n\n'\
    'GitHub: jndantas',

    '"Crie um currículo com um objetivo bem definido. '\
    'Por exemplo: back-end Java, front-end React"\n'\
    '— Anônimo',

    '"Git, inglês, e lógica de programação"\n'\
    '— Anônimo',

    '"Escolha aprender o básico de linguagens mainstream, e que tem bastante '\
    'mercado (tipo Javascript e PHP), aprende a fazer um pouco de tudo, '\
    'criar api, aprender um pouco de frontend, e se joga!\n'\
    '— Anônimo',

    '"Foco, acima de tudo, foco em seus objetivos!"\n'\
    '— Anônimo',

    '"Ame programação, sem amor você não dura muito nessa área"\n'\
    '— Anônimo',

    '"Tenha um portifólio no Github"\n'\
    '— Anônimo',

    '"Trabalhar nas soft-skills para mim é algo muito importante."\n'\
    '— Anônimo',

    '"Estude SQL."\n'\
    '— David Meth\n\n'\
    'Github Linkedin: me42th'
]

