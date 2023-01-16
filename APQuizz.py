# pour gildas et robin:

# -doc
# -mode d'emploie
# -clean le code
# -clean les textes afficher
# -ajouter des themes avec de bonne question
# -coder les erreur(si j'amais la personne code n'importe quoi ca relance le prompt au lieu de cracher)(Gestion des exceptions et des erreurs)
# -verifier que toute les focntionnalité son présente

# et j'ai pas encore a réussi a coder ca
# "Il faut que la question soit validée uniquement si toutes les bonnes réponses, et seulement celles-ci sont cochées"
# mon code marche si une seule réponse est validé.


import json
import random


# récupération des questions et des réponses dans le fichier JSON
with open("C:/Users/bapto/OneDrive/Bureau/AP-QUIZ-BRA/questionslibrary.json", "r") as f:
    data = json.load(f)

main()


def main():
    # recupère les donnée ranger et mélanger dans la fonction tri
    questions = tri_questions()
    # recupère le nombre de question que tu veux
    nombre_questions = nombre_question()
    # recupère le nombre de choix par question
    nombreqcm = choix_nombre_QCM()

    print("*** Début du Quiz ***\n")
    # recupère le nom de l'utilisateur
    nom = input(" Entrez votre nom: ").title()
    # espace
    print()
    print("\nBien joué {0}, vous avez repondu à {1} sur {2} questions.".format(
        nom, quiz(questions, nombre_questions, nombreqcm), nombre_questions))
    print("veux tu faire une autre parti ?(oui/non)")
    restart = input()
    # relance le quiz
    if restart == "oui":
        main()
    # relance pas le quiz
    else:
        print("aurevoir")


def tri_questions():
    theme = choix_theme()
    # mélange les questions
    random.shuffle(data[theme])
    # tri pour garder que le contenu des questions et des réponses
    result = {}
    for item in data[theme]:
        result[item["text"]] = {"options": item["options"],
                                "answer": item["answer"]}
    return result


def choix_theme():
    # choisi un theme pour le quiz
    print("Sélectionnez un theme:")
    print("1. animaux")
    print("2. géographie")
    print("3. langues")
    choix = input()
    if choix == "1":
        theme = ""
    elif choix == "2":
        theme = "geographie"
    elif choix == "3":
        theme = "langues"
    else:
        variable = "Sélection non valide"
    print("vous avez choisi {} comme theme de quizz ! ".format(theme))
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


def quiz(qs, nq, nqcm):

    points = 0
    for i, (qu, an) in enumerate(qs.items()):
        if i >= nq:
            break
        print(qu)

        melangeOption = an['answer'].copy()
        melangeOption.extend(an['options'][:nqcm-len(an['answer'])])
        random.shuffle(melangeOption)

        for j, opt in enumerate(melangeOption):
            print(f"{j+1}. {opt}")

        answer = input("Recopier la bonne réponse :")
        print(an['answer'])
        if answer in an['answer']:
            print("Correct!")
            points += 1
        else:
            print("Incorrect!")
    return points


# pour gildas et robin
