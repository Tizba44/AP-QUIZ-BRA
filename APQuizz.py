
from collections import Counter
import json
import random


# récupération des questions et des réponses dans le fichier JSON
with open("C:/Users/bapto/OneDrive/Bureau/AP-QUIZ-BRA/questionslibrary.json", "r") as f:
    data = json.load(f)


def main():
    # recupère les donnée ranger et mélanger dans la fonction tri
    theme = choix_theme()
    questions = tri_questions(theme)
    # recupère le nombre de question que tu veux
    nombre_questions = nombre_question()
    # recupère le nombre de choix par question
    nombreqcm = choix_nombre_QCM()

    print("*** Début du Quiz ***\n")
    # recupère le nom de l'utilisateur
    nom = input(" Entrez votre nom: ").title()
    # saut de ligne
    print()

    # dit le texte et affiche
    # -nom
    # -score et lance la fonction quiz qui lance le quiz
    # -et le nombre de quetion
    print("\nBien joué {0}, vous avez repondu à {1} sur {2} questions.".format(
        nom, quiz(nombre_questions, questions, nombreqcm), nombre_questions))

    # demande si tu veux refaire une parti
    print("veux tu faire une autre parti ?(oui/non)")
    restart = input()

    # relance le quiz
    if restart == "oui":
        main()

    # relance pas le quiz
    else:
        print("aurevoir")


def tri_questions(a):
    theme = a
    # mélange les questions
    random.shuffle(data[theme])
    # tri pour garder que le contenu des questions et des réponses
    result = {}
    for item in data[theme]:
        result[item["question"]] = {"faux": item["faux"],
                                    "vrai": item["vrai"]}
    return result


def choix_theme():
    print("Sélectionnez un theme:")
    compteur = 0

    for key, value in data.items():

        compteur += 1
        if type(value) == list:
            print(str(compteur)+"." + key)

    while True:
        try:
            choix = input(
                "Veuillez entrer un nombre entre 1 et " + str(compteur) + " : ")
            if 1 <= int(choix) <= int(compteur):
                break
            else:
                print("Veuillez entrer un nombre entre 1 et " + str(compteur))
        except ValueError:
            print("Veuillez entrer un nombre entier.")
    compteur = 0
    for key, value in data.items():
        compteur += 1
        if type(value) == list:
            if choix == str(compteur):
                theme = key
                print(theme)
    return theme


def nombre_question():
    # demande le nombre de question pour le quiz
    print("Combien shouaitez vous de question pour votre quizz ?")
    nombre_questions = int(input())
    return nombre_questions


def choix_nombre_QCM():
    # demande le nombre de choix par question
    print("Combien shouaitez de choix par Question (2 minimum)?")
    qcm = int(input())
    return qcm


def quiz(nombre_questions, questions, nombreqcm):
    # compte le nombre de point
    points = 0
    # crée une boucle qui parcourt les items (question et réponse) de la variable
    # "questions" en utilisant l'itérateur "enumerate" pour compter le nombre de questions.
    # qu =question  an = faux/vrai
    for i, (qu, an) in enumerate(questions.items()):
        # si le nombre de question est atteint alors on arrete le quiz
        if i == nombre_questions:
            break
        # recupère les bonne réponse en premier pour être sur d'avoi au moins une bonne réponse
        melangeOption = an['vrai'].copy()
        # comble avec des mauvaise réponse
        melangeOption.extend(an['faux'][:nombreqcm-len(an['vrai'])])
        # mélange le tout
        random.shuffle(melangeOption)
        # affiche les question QCM1
        print(f"{i+1}. {qu}")
        # affiche les choix des QCM
        for j, opt in enumerate(melangeOption):
            print(f"{j+1}. {opt}")
        answer = input(
            "Recopie la bonne réponse (si + d'une réponse écrire: reponse1,reponse2 ): ")
        correction = an['vrai']

        # ajoute les points
        points = points + corrige(answer, correction)

    return points


def corrige(answer, correction):
    # decoupe la réponse en fonction du séparateur ","
    answer = answer.split(',')
    # compte le nombre de bonnnne réponse et si c'est les même
    # (si on écrit dans le désordre les réponse c'est bon quand même)

    # Pour répondre a une question sans bonne réponse l'utilisateur peux taper rien  c'est = ['']
    # alors qu'un tableau vide = [] (dans le json) donc j'ai rajouter des condition pour que cela fonctionne
    # et j'ai mis rien a la place du vide pour que ça soit plus clair pour la boucle while/except
    if (answer == ["rien"] and correction == []):
        print("Correct!")
        # donne 1 point
        points = 1
    else:
        if Counter(answer) == Counter(correction):
            print("Correct!")
            # donne 1 point
            points = 1
        else:
            points = 0
            print("Incorrect!")
    return points


main()
