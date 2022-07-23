from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

## Init Flask APp
app = Flask(__name__)

nivel = 0

@app.route('/', methods=['POST'])
def bot():
  ## GEt userhttps://cataas.com/cat message
    user_msg = request.values.get('Body', '').lower()
    ## Init bot response
    bot_resp= MessagingResponse()
    msg = bot_resp.message()
    # Applying bot logic
    print(user_msg)

    # medio ambiente, producción, finanzas
    selec_1 = ['1', '2', '3']
    global nivel

    if nivel == 0:

        if 'menu' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )

        elif '1' in user_msg:
            msg.body("¿Qué tema de medio ambiente te gustaria aprender?\n ")
            msg.body("a .- Hacer composta \n  volver .- Para volver")
            nivel = 1
        elif '2' in user_msg:
            msg.body("¿Qué tema de producción te gustaria aprender? \n ")
            msg.body("Aun en construcción \n volver .- Para volver")
            nivel = 2
        elif '3' in user_msg:
            msg.body("¿Qué tema de finanzas te gustaria aprender?\n")
            msg.body(" a .- La diferencia entre ahorro e inversión. \n b.- Porque es importante invertir. \n c.- Como se devalúa tú dinero si solo lo ahorras. \n volver .- Para volver")
            nivel = 3
            
        elif 'cat' in user_msg:
            msg.media('https://cataas.com/cat')
        elif 'volver' in user_msg:
            msg.body("Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area\n ")
            msg.body("1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver")
        else:
            msg.body("Asegurate de usar uno de los numeros del menú")
        
        # elif 'quote' in user_msg:
        #     r = requests.get('https://api.quotable.io/random')
        #     if r.status_code == 200:
        #         data = r.json()
        #         quote = f'{data["content"]} ({data["author"]})'
        #     else:
        #         quote = 'I could not retrieve a quote at this time, sorry.'
        #     msg.body(quote)

    # medio amiente
    if nivel == 1:
        if 'a' in user_msg:
            msg.body("volver .- para regresar")
            msg.media('https://i.ibb.co/PxGrFMq/Whats-App-Image-2022-07-22-at-10-24-26-PM.jpg')

        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0
        else:
            msg.body("Asegurate de usar uno de los numeros del menú")

    # finanzas
    if nivel == 2:
        if '1' in user_msg:
            msg.body("volver .- para regresar")
            # msg.media('https://i.ibb.co/PxGrFMq/Whats-App-Image-2022-07-22-at-10-24-26-PM.jpg')

        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0
        else:
            msg.body("Asegurate de usar uno de los numeros del menú")


        # finanzas
    if nivel == 3:
        if 'a' in user_msg:
            msg.body("La diferencia entre ahorro e inversión - texto")
            msg.body("volver .- Para volver")

        elif 'b' in user_msg:
            msg.body(" Porque es importante invertir  - texto")
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'c' in user_msg:
            msg.body("Como se devalúa tú dinero si solo lo ahorras.  - texto")
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0
        else:
            msg.body("Asegurate de usar uno de los numeros del menú")
        
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)