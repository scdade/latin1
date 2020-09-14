from time import sleep
from random import randint,seed,shuffle
from wörterbuch import worte
seed()

print("Salve latein 1")
name = input("Wie heisst du? ")
print("Salve",name)

anzahlWorte = len(worte)
print("In unserem Wörterbuch sind %d Wörter"%anzahlWorte)

unserTest = list(worte)
shuffle(unserTest)


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

    if(antwort.lower()==übersetzung.lower()):
        print("Deine Antwort >%s< war richtig!"%antwort)
        richtig = richtig +1
    else:
        print("Total falsch! Richtig wäre %s gewesen"%übersetzung)
        falsch = falsch +1
        sleep(3)

print("%d von %d Worten waren falsch beantwortet!"%(falsch, len(unserTest)))
