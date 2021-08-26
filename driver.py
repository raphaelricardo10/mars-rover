from rover import Rover
from plateau import Plateau
import re

#Main menu
#Each infinite loop inside of it is a input checker
def menu() -> None:
    inputError = "Wrong input. Please, try again.\n\n"
    roverLst = []

    while True:
        ans = input("Insert the limits of the grid:\n")

        #checks the "digit space digit" format in user input
        if re.match(r"\d+\s\d+$", ans):
            limits = ans.split(" ", 1)
            limitX, limitY = [int(x) for x in limits]
            plat = Plateau(limitX, limitY)
            break
        else:
            print(inputError)

    while True:
        printStr = "Insert respectely the x, y and orientation values of the rover:\n"
        printStr += "If you want to stop adding rovers, just leave it in blank\n"

        ans = input(printStr)

        if ans == "":
            break

        #Checks the "Digit space digit space string" format in user input
        if re.match(r"\d+\s\d+\s[a-zA-Z]$", ans):
            roverData = ans.split(" ", 2)
            x, y = [int(x) for x in [roverData[0], roverData[1]]]
            o = roverData[2].upper()

            try:
                plat.checkPt(x, y)

            except Plateau.OutOfLimitsError:
                print("\nERROR: The selected position is off limits\n")
                continue

            except Plateau.CollisionDetectedError:
                print("\nERROR: The selected position is already occupied\n")
                continue
                
            if o not in Rover.Orientation._head:
                print(inputError)
                continue

            while True:
                ans = input("Insert the instruction string of the Rover:\n")

                #Checks the sequence of instructions format
                if re.match(r"[mrlMRL]+$", ans):
                    instructions = ans
                    roverLst.append(Rover(plat, x, y, o, instructions))
                    break
                else:
                    print(inputError)
        else:
            print(inputError)



    for rover in roverLst:
        try:
            rover.execInst(plat)
            print(f"{rover.x} {rover.y} {rover.Orientation.current}")

        except Plateau.CollisionDetectedError:    
            print(f"ERROR: Colision detected in [{rover.x}, {rover.y}].")
            print(f"Canceling movement of the{rover.name} {rover.id}.")
            rover.cancelMov()
        except Plateau.OutOfLimitsError:
            print(f"ERROR: Movement off limits detected in [{rover.x}, {rover.y}].")
            print(f"Canceling movement of the {rover.name} {rover.id}")
            rover.cancelMov()

menu()
