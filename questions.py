import random
import sys
# Preguntas para el juego
questions = [
" ¿Que funcion se usa para obtener la longitud de una cadena en Python?",
" ¿Cual de las siguientes opciones es un número entero en Python?",
" ¿Como se solicita entrada del usuario en Python?",
" ¿Cual de las siguientes expresiones es un comentarioválido en Python?",
" ¿Cual es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo ordenque las preguntas

answers = [
           ("size()", "len()", "length()", "count()"),
           ("3.14", "'42'", "10", "True"),
           ("input()", "scan()", "read()", "ask()"),
           ( "// Esto es un comentario",
            "/* Esto es un comentario */",
            "-- Esto es un comentario",
            "# Esto es un comentario",
            ),
           ("=", "==", "!=", "==="),
        ]
# Índice de la respuesta correcta para cada pregunta, el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
puntaje = 0;

#Selecciona k preguntas al azar junto al indice de su rta correcta y las respuestas disponibles
questions_to_ask = random.sample(list(zip(questions,
answers, correct_answers_index)), k=3)

# Itera sobre la tupla creada anteriormente

for answer,answer_list, correct_index in questions_to_ask:
    
    #Imprimo la pregunta con sus opciones
    print(f"Pregunta: {answer}")
    for i, rta in enumerate(answer_list):
        print(f"{i+1}. {rta}")
    
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
    
        user_answer = input("Respuesta: ") 
        
        if not user_answer.isdigit()  or not ( 1 <= int(user_answer) <= 4)   : # Se verifica si la respuesta es correcta
            print("La respuesta no es un numero o esta fuera de rango")
            sys.exit(1)
            
        user_answer= int(user_answer) -1;
            
        if user_answer == correct_index:
            puntaje+=1
            print("¡Correcto!, sumaste 1 punto de recompensa y tu acumulado es de: " + f"{puntaje}")
            break
        else:
            puntaje= puntaje - 0.5
            print ("Respuesta incorrecta!! Restaste 0.5 de tu acumulado y tu actual es: " + f"{puntaje}")
            
# Si el usuario no responde correctamente después dE 2 intentos, se muestra la respuesta correcta
    print(" La respuesta correcta es:")
    print(answer_list[correct_index])
print("el puntaje conseguido fue de: "+ f"{puntaje}");     
# Se imprime un blanco al final de la pregunta
print()
