# Quiz QCM
# 4 à 16 ans
# entièrement paramétrable sans nécessiter connaissances en info
# doc utilisateur permettant aux animateurs  comprendre créer modifier eux-mêmes leurs quiz
# Il n'y a pas de limite pour le nombre de questions.
# Le nombre d'essai sera paramétrable.
# Les questions peuvent avoir plusieurs réponses possibles sans limite mais le joueur ne peut saisir qu'une seule réponse par question.
# Les écrans du jeu (le jeu par lui-même et l'affichage des résultats) garderont un aspect semblable aux écrans du jeu de géographie. (Annexe 2)
# Les points attribués à chaque question seront paramétrables.
# Lors de l'écriture de la solution, il faut rendre le jeu complètement paramétrable (ce qui n'est pas le cas dans le jeu ci dessous.) c'est-à-dire que la feuille de code développé doit s'adapter aux changements sans modification de code. Ainsi, le thème, les questions, les réponses, le nombre d'essai et les points seront donc définis dans un fichier séparé du code pour s'adapter au jeu (fichier .JSON par exemple)
# Lors de la phase de recette et lors de la démo, le jeu doit être capable de bien réagir aux données du recetteur. (Annexe 3)
# Le code sera documenté pour le comprendre du mieux possible.
# l faudra concevoir une notice utilisateur indiquant le mode opératoire pour adapter le jeu aux besoins de l'utilisateur.
# =========================================================================================================================
import json

# récupération des questions et des réponses dans le fichier JSON
with open("C:/Users/bapto/OneDrive/Bureau/AP-QUIZ-BRA/itération/1er itération/questionslibrary.json", "r") as f:
    data = json.load(f)


def nombre_question():
    # demande le nombre de question pour le quiz
    print("Combien shouaitez vous de question pour votre quizz ?")
    nombre_questions = int(input())
    return nombre_questions


def tri_questions():
    # tri pour garde que le contenue des questions et des réponses
    result = {}
    for item in data['questionslibrary']:
        result[item["questions"]] = item["answers"]
    return result


def main():
    questions = tri_questions()
    nombre_questions = nombre_question()
    print("*** Début du Quiz ***\n")
    nom = input(" Entrez votre nom: ").title()
    print()
    print("\nBien joué {0}, vous avez repondu à {1} sur {2} questions.".format(
        nom, quiz(questions, nombre_questions), nombre_questions))


def quiz(qs, nq):
    '''
    fonction de quizz et calcul des points
    paramètre d'entree: sq: type Dictionnaire 
    paramètre de sortie:
    '''
    points = 0
    for i, (qu, an) in enumerate(qs.items()):
        if i >= nq:
            break
        if input(qu).lower() == an.lower():
            points += 1
            print("Juste.")
        else:
            print("Oups, la bonne réponse est \"{}\".".format(an))
    return points


if __name__ == "__main__":
    main()
