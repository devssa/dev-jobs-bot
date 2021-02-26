# Dev Jobs Bot


> _"Os seres humanos são alérgicos à mudança. Adoram dizer: 'Nós sempre fizemos isto desta maneira.' Eu tento lutar contra isso. É por isso que eu tenho um relógio na minha parede que roda no sentido anti-horário."_ </br>
> – Grace Hopper

<p align="center"><img src="https://media.giphy.com/media/7ziPSJRdBgA9sPMZLJ/giphy.gif" width="660" frameBorder="0"></p>
<p><a href="https://giphy.com/gifs/7ziPSJRdBgA9sPMZLJ">via GIPHY</a></p>

## Descrição

Dev Jobs Bot é um bot genérico que disponibiliza vagas de emprego que são divulgados no GitHub através das issues de um determinado repositório.
Antes de utilizar este bot em sua comunidade, recomendo este <a href="https://medium.com/tht-things-hackers-team/10-passos-para-se-criar-um-bot-no-telegram-3c1848e404c4">tutorial</a> de como criar um bot no Telegram.

## Como surgiu

Ao participar do grupo do Telegram da comunidade <a href="https://t.me/co0da4r">Onde Codar em Salvador</a>, eu percebi que as vagas eram inseridas em um repositório especifico da comunidade e divulgadas através das issues do mesmo. Percebi que este é um padrão na maioria das comunidades, e como quase toda comunidade tem um canal no Telegram (sim, é lá que os devs se escondem!) e reconhecendo este padrão... porque não unir o útil ao agradável e automatizar o acesso as vagas por terceiros direto do próprio telegram?

## Uso

### Configurações iniciais
É necessário renomear o env.example.py para env.py, e preencher todas as variáveis constantes com as seguintes informações:

* TOKEN: str => deve conter o token da API do telegram para se comunicar com o bot
* BOT_NAME: str => o nome do seu bot.
* COMMUNITY_SITE: str => o site da sua comunidade.
* COMMUNITY_GH: str => o link do GitHub da comunidade.
* COMMUNITY_GH_ISSUES: str => o link das issues do repositório de vagas no GitHub da comunidade.
* COMMUNITY_GH_API_ISSUES: str => o link da API do GitHub para acessar as issues do repositório de vagas.
  * Exemplo: https://api.github.com/repos/{mantenedor}/{repositório}/issues.
* COMMUNITY_NAME: str => nome da comunidade. 

### Comandos

Copie esses comandos e insira na seção de comandos do bot, esta etapa é responsabilidade do BotFather, o deus dos Bots.
```
jobs - Verifique as vagas lançadas hoje!
last - Configura as últimas dez vagas
about - Sobre este bot
hint - Dicas da comunidade
```
Os comandos são auto-explicativos, certo? Preferi utilizar o inglês por convenção, se tiver algo contra... o Tio Sam vai bater na sua porta! Brincadeira, é só forkar e fazer o que você quiser hahahahaha.

## Agradecimentos 

Alguns módulos de código aberto foram utilizados neste projeto, é sempre bom fazer uma referência a quem facilita nosso dia-a-dia e contribui direta ou indiretamente para um mundo melhor.

* <a href="https://github.com/eternnoir/pyTelegramBotAPI">pyTelegramBotAPI</a>: fácil de usar, prático, poderoso e... pythônico (todos os metódos em snake_case, isso é poesia para mim).
* <a href="https://github.com/psf/requests">requests</a>: aquele módulo _massa_ pra quem quer fazer scraping, consumir APIs ou só tem preguiça de aprender o urllib, mesmo ele sendo mais rápido hahaha.
