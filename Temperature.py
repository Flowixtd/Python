def Temperature():
    while True:
        try:
            option = int(input("\nChoissisez une option de conversion :\n 1. Dégré Celsius en Fahrenheit\n 2. Dégré Celsius en Kelvin\n 3. Degré Fahrenheit en Celsius\n 4. Degré Fahrenheit en Kelvin\n 5. Kelvin en degré Celsius\n 6. Kelvin en Fahrenheit\nVotre choix : "))
        except ValueError:
            print("Veillez insérer une valeur entre 1 et 6 !")
            continue
        if option == 1:
            valeur = float(input("\nInsérer votre valeur : "))
            Celsius_Fahrenheit = (valeur*9/5)+32
            print(Celsius_Fahrenheit,"°F")
            break
        elif option == 2:
            valeur = float(input("\nInsérer votre valeur : "))
            Celsius_Kelvin = (valeur+273.15)
            print(Celsius_Kelvin,"K")
            break
        elif option == 3:
            valeur = float(input("\nInsérer votre valeur : "))
            Fahrenheit_Celsius = (valeur-32)*5/9
            print(Fahrenheit_Celsius,"°C")
            break
        elif option == 4:
            valeur = float(input("\nInsérer votre valeur : "))
            Fahrenheit_Kelvin = (valeur-32)*5/9+273.15
            print(Fahrenheit_Kelvin,"K")
            break
        elif option == 5:
            valeur = float(input("\nInsérer votre valeur : "))
            Kelvin_Celsius = (valeur-273.15)
            print(Kelvin_Celsius,"°C")
            break
        elif option == 6:
            valeur = float(input("\nInsérer votre valeur : "))
            Kelvin_Fahrenheit = (valeur-273.15)*9/5+32
            print(Kelvin_Fahrenheit,"°F")
            break

Temperature()