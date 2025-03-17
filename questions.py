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

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)
    
    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
    
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
    
        user_answer = input("Respuesta: ") 
        
        if not user_answer.isdigit()  or not ( 1 <= int(user_answer) <= 4)   : # Se verifica si la respuesta es correcta
            print("La respuesta no es un numero o esta fuera de rango")
            sys.exit(1)
            
        user_answer= int(user_answer) -1;
            
        if user_answer == correct_answers_index[question_index]:
            print("¡Correcto!")
            break
        else:
            print ("Respuesta incorrecta")
# Si el usuario no responde correctamente después dE 2 intentos, se muestra la respuesta correcta
    print(" La respuesta correcta es:")
    print(answers[question_index] [correct_answers_index[question_index]])
    
# Se imprime un blanco al final de la pregunta
print()
