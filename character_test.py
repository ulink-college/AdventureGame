from character import Enemy



dave = Enemy("Dave", "A smelly zombie")
dave.set_weakness("milk")

dave.describe()
dave.talk()
fightWith = input("What will you fight with? \n")
dave.fight(fightWith)