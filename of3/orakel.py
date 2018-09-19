user_choice = None

while user_choice != "4":
    print("Velkommen til Orakeltjenesten. Mulige valg:")
    print("1. Send en mail om et problem")
    print("2. Få vår kontaktinfo")
    print("3. Søk om jobb her")
    print("4. Avslutt")

    user_choice = input("Hva vil du gjøre? ")

    if user_choice == "1":
        print("Sender en mail til orakel@ntnu.no")
    elif user_choice == "2":
        print("Vi kan nås på orakel@ntnu.no, eller i realfagsbiblioteket")
    elif user_choice == "3":
        print("Vi har ingen ledige jobber nå")

print("Takk for besøket")