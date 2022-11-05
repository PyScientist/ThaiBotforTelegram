import telebot

def main(token):

    thai_bot = telebot.TeleBot(token)
    print(F'launching bot with {token}')

    @thai_bot.message_handler(commands=['start'])
    def start_message(message):
        thai_bot.send_message(message.chat.id, 'Welcome to Thai inform droid! \n'
                                               'Use /help to find out my abilities')

    @thai_bot.message_handler(commands=['help'])
    def help_message(message):
        thai_bot.send_message(message.chat.id, 'Routine actions:\n'
                                               '/start - bot initiation\n'
                                               '/help - help\n'
                                               'Specific actions and procedures:\n'
                                               '/calcbmi - calculate of obdy mass index\n'
                                               '/returncurracies - return THB to USD ratio\n'
                                               '/returnwf - return weather')

    @thai_bot.message_handler(content_types=['text'])
    def message_reply(message):
        if message.text == '/calcbmi':
            msg = thai_bot.send_message(message.chat.id, "please provide your hight in cm and weight in kg in format weight:hight")
            thai_bot.register_next_step_handler(msg, calculate_bmi)
        elif message.text == 'Hi':
             thai_bot.send_message(message.chat.id, 'Hello Stranger!')
        else:
            thai_bot.send_message(message.chat.id, 'Hello Stranger! i dont understand you plese type /help for help!')


    def calculate_bmi(message):
        try:
            weight, hight = [float(i) for i in message.text.split(":")]
            error = False
        except:
            error = True
        if (weight > 30) and (weight < 150) and (hight > 100) and (hight < 300):
            error, bmi = False, weight/((hight/100)**2)
        else:
            error = True
        if error == False:
            if (bmi<=25) and (bmi >= 18.5):
                reply = 'all good your bmi is perfect, it is between 18.5 and 25'
            elif bmi < 18.5:
                reply = 'your weight is too low you need include in diet more fat and protein'
            elif bmi > 25:
                reply = 'your weight is too big you need to exclude from diet the fat and carbohydrates'
            thai_bot.send_message(message.chat.id, F'{reply}; bmi is {bmi}')
        if error == True:
            thai_bot.send_message(message.chat.id, 'Your input is wrong, please try again.')
    thai_bot.polling()

if __name__ == "__main__":
    token = '5745863146:AAHI4Hepkx1bsrnXNkiTq2sUHpV-oIDOLmI'
    main(token)
