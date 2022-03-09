import random

artigos = ["o", "a", "um", "uma", "uns", "do", "da", "no", "na"]

sujeitos = ["gato", "cachorro", "homem", "mulher", "pessoa", "elefante",
            "super-homem"]

verbos = ["cantar", "caminhar", "correr", "desenhar", "programar", 
         "andar", "estudar", "adivinhar"]

adverbios = ["apenas", "bastante", "demais", "de todo", "deveras", "mais",
            "quão", "quase", "abaixo", "acima"]

try:
    for i in [1, 2, 3, 4, 5]:
        at = random.choice(artigos)
        suj = random.choice(sujeitos)
        verb = random.choice(verbos)
        adverb = random.choice(adverbios)
        if random.randint(0, 1) == 0:
            print(at, suj, verb)
        else:
            print(at, suj, verb, adverb)
except IndexError as err:
        print(err)
    