# 1. Gör ett valfritt program som suddar skärmen med os.system(‘cls’) vid flera tillfällen. Du kan även uppdatera ett gammalt program
# 2. Använd sleep()-kommandot i valfritt projekt och spara som nytt filnamn sleep() används när du vill att programmet väntar innan det fortsätter
# 3. Gör ett välkomstprogram som väntar på en knapptryckning (utan ENTER) innan det avslutas getwch()
# 4. Gör en modul som ändrar färg (kolla projekt här på CR)
# 5. Skapa ett färgstarkt program som använder färg samt något mer du lärt dig (se colors.txt nedan)
# 6. Uppdatera gärna något annat gammalt program med getwch() och färger!
# 7. ÖVERKURS: Skapa en egen modul och importera till ett program



import os
import time
import msvcrt
from colors import colors as clr

min_lista = ["oliver", "är", "inte", "rolig"]

while True:
    os.system('cls')        
    
    print(f"{clr.BLUE}Tryck på valfri knapp för att gå vidare{clr.DEFAULT}")
    key = msvcrt.getwch()
    print(f"{clr.YELLOW}Du klickade på: {key}{clr.DEFAULT}")
    time.sleep(1)

    os.system('cls')
    time.sleep(1)
    
    print(f"\n{clr.BLUE}{min_lista}{clr.DEFAULT}\n")
    time.sleep(1)
    
    val = input("(+) för att addera (-) för att ta bort (q) för att avsluta: ").lower()

    if val == "+":
        namn = input(f"{clr.GREEN}Vad vill du lägga till: {clr.DEFAULT}")
        min_lista.append(namn)
        os.system('cls')
        time.sleep(1)
        print(f"{clr.BLUE}La till '{namn}'{clr.DEFAULT}")

    elif val == "-":
        namn = input(f"{clr.RED}Vad vill du ta bort?: {clr.DEFAULT}")
        if namn in min_lista:
            min_lista.remove(namn)
            os.system('cls')
            time.sleep(1)
            print(f"{clr.BLUE}Tog bort '{namn}'!{clr.DEFAULT}")
        else:
            print(f"{clr.RED}Namnet finns inte i listan.{clr.DEFAULT}")
            time.sleep(2)

    elif val == "q":
        os.system('cls')
        print("Hejdå!")
        break

    else:
        print(f"{clr.RED}Error: Ogiltigt val.{clr.DEFAULT}")
        time.sleep(2)