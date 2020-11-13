# Rename this file to env.py

# TELEGRAM TOKEN
TOKEN = ''

# PERSONAL INFO
BOT_NAME = ''
COMMUNITY_SITE = ''
COMMUNITY_GH = ''
COMMUNITY_GH_ISSUES = ''
COMMUNITY_GH_API_ISSUES = ''
COMMUNITY_NAME = ''

# INSERT A MESSAGE HERE THAT SHOWS WHEN IT HAVE NO JOBS
NOT_JOBS_MSG = f"""
⚠ ️Nenhuma vaga foi divulgada hoje.

Verifique as vagas dos dias anteriores no repositório da comunidade.
Pode ser que as mesmas ainda não tenham sido preenchidas.

{COMMUNITY_GH_ISSUES}
"""

ABOUT_MSG = f"""
{BOT_NAME} é um bot para exibir as vagas da área de desenvolvimento e afins divulgadas no GitHub da comunidade {COMMUNITY_NAME}.

Site: {COMMUNITY_SITE}
GitHub: {COMMUNITY_GH}
"""
