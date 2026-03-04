# 1. Gör ett valfritt program som suddar skärmen med os.system(‘cls’) vid flera tillfällen. Du kan även uppdatera ett gammalt program
# 2. Använd sleep()-kommandot i valfritt projekt och spara som nytt filnamn sleep() används när du vill att programmet väntar innan det fortsätter
# 3. Gör ett välkomstprogram som väntar på en knapptryckning (utan ENTER) innan det avslutas getwch()
# 4. Gör en modul som ändrar färg (kolla projekt här på CR)
# 5. Skapa ett färgstarkt program som använder färg samt något mer du lärt dig (se colors.txt nedan)
# 6. Uppdatera gärna något annat gammalt program med getwch() och färger!
# 7. ÖVERKURS: Skapa en egen modul och importera till ett program


import os

list = ["oliver","är","inte","rolig"]

while True:
    os.system('cls')        

    print(list)

    val = input("(+) för att addera (-) för att ta bort").lower()

    if val =="+":
        namn = input("vad vill du lägga till : ")
        list.append(namn)
        os.system('cls')
        print(f"la till {namn}")


    elif val == "-":
        namn = input("Vad vill du ta bort? : ")
        if namn in list:
            list.remove(namn)
            os.system('cls')
            print(f" Tog bort '{namn}'!")
        else:
            print("Namnet finns inte i listan.")

    elif val == "q":
        os.system('cls')
        break

    else:
        print("error")
        


