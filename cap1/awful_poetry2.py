import random, sys

artigos = ["o", "a", "um", "uma", "uns", "do", "da", "no", "na"]

sujeitos = ["gato", "cachorro", "homem", "mulher", "pessoa", "elefante",
            "super-homem"]

verbos = ["cantar", "caminhar", "correr", "desenhar", "programar", 
         "andar", "estudar", "adivinhar"]

adverbios = ["apenas", "bastante", "demais", "de todo", "deveras", "mais",
            "quão", "quase", "abaixo", "acima"]


lines = 5
if len(sys.argv) > 1:
    try:
        i = -1
        lines = int(sys.argv[1])
        while i < lines - 1:
            i += 1
            
    except IndexError as err:
            print(err)
    except ValueError as err:
        print('usage: awful_poetry2.py <number of lines>')

while lines:
        at = random.choice(artigos)
        suj = random.choice(sujeitos)
        verb = random.choice(verbos)
        adverb = random.choice(adverbios)

        if random.randint(0, 1) == 0:
            print(at, suj, verb)
        else:
            print(at, suj, verb, adverb)
        lines -= 1