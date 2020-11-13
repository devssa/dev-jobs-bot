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


