from itertools import permutations
from time import sleep
from random import randint,seed
from wörterbuch import worte
seed()

print("Salve latein 1")
name = input("Wie heisst du? ")
print("Salve",name)

anzahlWorte = len(worte)
print("In unserem Wörterbuch sind %d Wörter"%anzahlWorte)

#nochmal nachdenken....
gemischteWortliste = list(permutations(worte))
unserTest = gemischteWortliste[randint(0,len(gemischteWortliste)-1)]

richtig = 0
falsch = 0
for [latein,deutsch] in unserTest:
    richtung = randint(0,100)>=50
    if richtung==True:
        übersetzung = deutsch
        print("Was heisst >%s< auf deutsch?"%latein)
    else:
        übersetzung = latein
        print("Was heisst >%s< auf lateinisch?"%deutsch)
    antwort = input("")

    if(antwort==übersetzung):
        print("Deine Antwort >%s< war richtig!"%antwort)
        richtig = richtig +1
    else:
        print("Total falsch!")
        falsch = falsch +1
        sleep(3)
print("%d von %d Worten waren falsch beantwortet!"%(falsch, len(unserTest)))