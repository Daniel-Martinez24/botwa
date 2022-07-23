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
    sin_info = "Aun en construcción \n volver .- Para volver"
    error_t = "Asegurate de usar uno de los numeros o letras del menú"
    texto_vacio = "Aun no hay información"

    if nivel == 0:

        if 'hola' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )

        elif '1' in user_msg:
            msg.body("¿Qué tema de medio ambiente te gustaria aprender ")
            msg.body(
                "?"
                "\na .- Diferencia ente vidrio y cristal (para el reciclaje)"
                "\n b.-Tipos de desechos y cómo separarlos \nc.- Ejemplos de cómo las empresas pueden ayudar a facilitar el reciclaje  "
                "\nd .- Captación de agua en tiempos de lluvia"
                "\ne.-Economía circular  \nf.- Fast fashion y sus alternativas  "
                "\ng .- Tu basura orgánica también contamina "
                "\nh.-La bolsa de plástico no es el enemigo  \ni.- Policultivos vs. monocultivos  "
                "\nvolver .- Para volver"
            )
            nivel = 1
        elif '2' in user_msg:
            msg.body("Talleres para la realización de producto"
            "s"
            "\na .-Cómo preparar Yogurt Griego \nb.- Cómo preparar Flan"
                " \nc.- Cómo preparar Pastel Imposible"
                " \nd .- Cómo preparar Carlota de Limón  \ne.- Principios de las mermeladas"
                " \nf .- Tips para la fabricación de bisutería \ng.-Cómo deshidratar frutas"          
                " \nh .- Cómo preparar cecina \ni.- Tipos de costuras de ropa"
                " \nj .- Tejer vs bordar"             
                
                "\n volver .- Para volver")
            nivel = 2
        elif '3' in user_msg:
            msg.body("¿Qué tema de Comercializar productos te gustaria aprender")
            msg.body("?"
                "\na .- Finanzas basicas. \nb.- Ganancias y perdidas"
                " \nc.- Eficiencia de la Energía: hacer más con menos "
                " \nd .- Fijación de Precios. \ne.- Administración del Inventario"
                " \nf .- Correo Electrónico Comercial \ng.-Liderazgo Eficaz"             
                
                "\n volver .- Para volver")
            nivel = 3
            
        # elif 'cat' in user_msg:
        #     msg.media('https://cataas.com/cat')
        elif 'volver' in user_msg:
            msg.body("Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area\n ")
            msg.body("1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver")
        else:
            msg.body(error_t)
        
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
            msg.body( "Selecciona el numero que te interese"
                "\n1 Cómo saber si es vidrio o cristal fácilmente."
                "\n2 ¿Es posible tirar cristales rotos en el contenedor de vidrio?"
                "\n3 ¿Dónde se tira el vidrio?"
                "\n4 ¿Dónde se tira el cristal?"
                "\n5 ¿Qué es mejor, el vidrio o el cristal? Punto de vista del reciclaje."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
            # msg.media('https://i.ibb.co/PxGrFMq/Whats-App-Image-2022-07-22-at-10-24-26-PM.jpg')
        if 'b' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 ¿Por qué es importante separar la basura?"
                "\n2 Consejos para separar la basura en casa."
                "\n3 Envases y plástico."
                "\n.4 Vidrio."
                "\n5 Papel y Cartón."
                "\n6 Residuos orgánicos."
                "\n7 Restos y desechos."
                "\n8 Ropa."
                "\n9 Medicinas caducadas."
                "\n10 Aceite usado."
                "\n11 Punto limpio."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'c' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 ¿Qué residuos se generan?"
                "\n2 ¿Los residuos generados son reciclables?"
                "\n3 ¿Existen otras maneras para sustituirlos?"
                "\n4 Establecer formas de recolección."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        
        if 'd' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Tipos de superficie de captación."
                "\n2 Pendiente."
                "\n3 Replanteo."
                "\n4 Primeras aguas y filtro."
                "\n5 Extracción del agua."
                "\n6 Métodos de desinfección del agua."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")

        if 'e' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Rediseñar."
                "\n2 Reducir."
                "\n3 Reutilizar."
                "\n4 Reparar."
                "\n5 Renovar."
                "\n6 Recuperar."
                "\n7 Reciclar."
                "\n8 La importancia de las 7R para el medio ambiente."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0
        else:
            msg.body(error_t)

    # finanzas
    if nivel == 2:
        if 'a' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Diferencia entre yogurt natural y yogurt griego. "
                "\n2 Beneficios del yogurt griego. "
                "\n3 Yogurt griego con tres ingredientes. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
            # msg.media('https://i.ibb.co/PxGrFMq/Whats-App-Image-2022-07-22-at-10-24-26-PM.jpg')
        if 'b' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n2.1 Flan sin horno. "
                "\n2.2 Flan napolitano."
                "\n2.3 Flan tradicional. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'c' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n3.3 Pastel imposible en estufa a baño María. "
                "\n3.4 Pastel imposible de chocofresa."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'd' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n4.1 Carlota de limón sin horno."
                "\n4.2 Carlota de limón en vaso."
                "\n4.3 Carlota de limón con gelatina. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'e' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Flan sin horno. "
                "\n2 Flan napolitano."
                "\n3 Flan tradicional. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'f' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Elaboración de mermeladas. "
                "\n2 Pectinas: ¿qué y para qué son?"
                "\n3 Fases de elaboración."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'g' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Diseño: establece tu estilo."
                "\n2 Cómo conseguir un buen distribuidor."
                "\n3 Estudio de mercado. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'h' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Consejos para deshidratar fruta correctamente. "
                "\n2 Cómo deshidratar fruta en el horno."
                "\n3 Cómo deshidratar fruta en el microondas. "
                "\n4 Cómo deshidratar fruta al sol."
                "\n5 Cómo deshidratar fruta en el deshidratador. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'i' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Qué tipos de cecina hay. "
                "\n2 Cómo saber que mi cecina ya está."
                "\n3 Distintas maneras de preparar cecina."
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'j' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 ¿Para qué sirve cada tipo de costura?"
                "\n2 ¿Cuál es la costura más resistente?"
                "\n3 Importancia de la costura. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
        if 'k' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Diferencias entre tejer y bordar."
                "\n2 Beneficios de bordar y tejer. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")

        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0
        else:
            msg.body(error_t)


        # finanzas
    if nivel == 3:
        if 'a' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Qué es el ahorro, la inversión y sus diferencias. "
                "\n2 Por qué es mejor invertir que ahorrar. "
                "\n3 Qué es la inflación y cómo nos afecta. "
                "\n4 Qué es un presupuesto y su importancia."
                "\n5 Cómo funcionan las tarjetas de crédito. "
                "\n6 Por qué no se puede sólo imprimir dinero. "
                )
            msg.body("\n1 otro nivel \nvolver .- Para volver")
            nivel = 3.1

        elif 'b' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Qué es una ganancia."
                "\n2 Qué es la utilidad neta."
                "\n3 Qué son los costos y gastos."
                "\n4 Tipos de costos."
                "\n5 Qué son los estados financieros."
                )
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'c' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Cómo la innovación hará que tus costos bajen "
                "\n2 La clave del éxito es dedicar los recursos a hacer solo lo importante."
                "\n3 Tips de productividad para el emprendedor. "
                "\n4 Hábitos que te ayudan a incrementar tu productividad."
                "\n5 Principio de Pareto "
                "\n6 Principio de Lean."
                )
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'd' in user_msg: 
            msg.body( "Selecciona el numero que te interese"
                "\n1 Importancia de establecer el precio correcto. "
                "\n2 Factores que influyen en la fijación de precios."
                "\n3 Estudio de mercado: qué es y cómo hacer uno."
                "\n4 Qué diferencia mi producto de otros."
                )
            msg.body("volver .- Para volver")
            msg.media('https://i.ibb.co/w7kjSLR/FIJACION-DE-PRECIOS-2.png')
            nivel = 3
        elif 'e' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Tipos de inventario."
                "\n2 Control de inventario."
                "\n3 Presupuestos."
                )
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'f' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Importancia del correo electrónico comercial. "
                "\n2 Qué enviar y qué no enviar a tus clientes."
                "\n3 Tips para que mi correo electrónico comercial sea distinto a los demás. "
                )
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'g' in user_msg:
            msg.body( "Selecciona el numero que te interese"
                "\n1 Importancia del correo electrónico comercial. "
                "\n2 Qué enviar y qué no enviar a tus clientes."
                "\n3 Tips para que mi correo electrónico comercial sea distinto a los demás. "
                )
            msg.body("volver .- Para volver")
            nivel = 3
        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0
    if nivel == 3.1:
        if '1' in user_msg:
            msg.body(" *Qué es el ahorro, la inversión y sus diferencias.* ")
            msg.body(texto_vacio)
            msg.body("\n\nvolver .- Para volver")
        if '2' in user_msg:
            msg.body(" *Por qué es mejor invertir que ahorrar* ")
            msg.body(texto_vacio)
            msg.body("\n\nvolver .- Para volver")
        if '3' in user_msg:
            msg.body(" *Qué es la inflación y cómo nos afecta..* ")
            msg.body(texto_vacio)
            msg.body("\n\nvolver .- Para volver")
        if '4' in user_msg:
            msg.body(" *Qué es un presupuesto y su importancia.* ")
            msg.body(texto_vacio)
            msg.body("\n\nvolver .- Para volver")
        if '5' in user_msg:
            msg.body(" *Cómo funcionan las tarjetas de crédito. * ")
            msg.body(texto_vacio)
            msg.body("\n\nvolver .- Para volver")
        if '6' in user_msg:
            msg.body(" *Por qué no se puede sólo imprimir dinero. * ")
            msg.body(texto_vacio)
            msg.body("\n\nvolver .- Para volver")
        elif 'volver' in user_msg:
            msg.body(
                "Hola, bienvenida a nuestro menu, selecciona el area que te gustaría explorar, escribe el numero de area. \n"
                " 1 .- Cuidado de medio ambiente \n 2.- Producción \n 3.- Finanzas \n volver .- Para volver"
                )
            nivel = 0

        else:
            msg.body(error_t)
        
    return str(bot_resp)

if __name__ == '__main__':
    app.run(debug=True)