print("Hej och välkommen!")
name = input("Namn: ")
age = int(input("Ålder: "))

if age <= 18:
    print(f"Hej {name}, som är {age}år gammal.\nDu får inte rösta.")
else:
    print(f"Hej {name}, som är {age}år gammal.\nDu får rösta")
