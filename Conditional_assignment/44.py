#. Write a program to check traffic signal actions using match case.

Signal = input("Enter traffic signal color: ")
Signal = Signal.lower()

match Signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go when safe")
    case _:
        print("Invalid signal color")