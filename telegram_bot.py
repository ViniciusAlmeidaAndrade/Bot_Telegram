"""
Criado por https://github.com/Rodrigo-Kelven

Este Bot foi um exercicio proposto por Yure Faro!!!
"""

import telebot

# Substitua pelo seu token
token = 'COLOQUE SEU TOKEM AQUI'
bot = telebot.TeleBot(token)

# Variáveis para armazenar dados do usuário
nome = ''
idade = ''
n_cpf = ''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global nome, idade, n_cpf
    bot.reply_to(message, "Bem-vindo! Para criar seu cadastro, por favor me diga seu nome!:")
    bot.register_next_step_handler(message, process_name)

def process_name(message):
    global nome
    nome = message.text
    bot.reply_to(message, "Obrigado, {}! Agora, por favor, me diga sua idade!:".format(nome))
    bot.register_next_step_handler(message, process_age)

def process_age(message):
    global idade
    idade = message.text
    bot.reply_to(message, "Perfeito! Agora, por favor, me forneça seu CPF!:")
    bot.register_next_step_handler(message, process_cpf)

def process_cpf(message):
    global n_cpf
    n_cpf = message.text

    # Verificação básica para garantir que o CPF contém apenas dígitos
    if not n_cpf.isdigit() or len(n_cpf) != 11:
        bot.reply_to(message, "Por favor, digite um CPF válido com 11 dígitos seu energúmeno!.")
        bot.register_next_step_handler(message, process_cpf)  # Repetir a solicitação
        return

    send_telegram_msg()


def send_telegram_msg():
    msg_final = ('''
                Confirmação de cadastro,
                Nome: %s
                Idade: %s
                CPF: %s
                Obrigado por criar o seu cadastro!
                Seus dados serão utilizados para fins financeiros!
                ''' % (nome, idade, n_cpf))
    bot.send_message('COLOQUE SEU ID AQUI', msg_final, parse_mode="Markdown")

# Inicia o bot
bot.polling()
