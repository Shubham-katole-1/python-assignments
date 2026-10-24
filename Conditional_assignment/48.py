#  Write a program to print language choice using match case.

Language = input("Choose language (english, hindi, marathi , bhojpuri): ")

match Language:
    case "english":
        print("English selected")
    case "hindi":
        print("Hindi selected")
    case "marathi":
        print("Marathi selected")
    case "bhojpuri":
        print("Bhojpuri")
    case _:
        print("Invalid language choice")