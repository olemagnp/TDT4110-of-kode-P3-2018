

def les_inn_bilinfo():
    make = input("Hvilket bilmerke var det? ")
    model = input("Hvilken modell var det? ")
    color = input("Hvilken farge var det? ")

    return [make, model, color]


def sjekk_bil(obs, actual):
    for i in range(len(obs)):
        if obs[i] != actual[i] and obs[i] != '?':
            return False
    return True

SKILTBOKSTAVER = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', '?')

def les_gyldig_vitneskilt():
    plate = input("Skriv inn skilt, 2 bokst + 5 tall (?=usikker) ")
    if len(plate) != 7:
        print("Et nummerskilt må være 7 tegn langt.")
        return les_gyldig_vitneskilt()

    if plate[0] not in SKILTBOKSTAVER or plate[1] not in SKILTBOKSTAVER:
        print("De to første tegnene må være gyldige skiltbokstaver.")
        return les_gyldig_vitneskilt()

    for i in range(2, 7):
        if not plate[i].isnumeric() and plate[i] != '?':
            print("De fem siste tegnene må være tall eller ?")
            return les_gyldig_vitneskilt()
    return plate


def match(obs, actual):
    for i in range(len(obs)):
        if obs[i] != actual[i] and obs[i] != '?':
            return False
    return True


def match_liste(obs, actuals):
    matching = []

    for plate in actuals:
        if match(obs, plate):
            matching.append(plate)

    return matching


def main():
    try:
        car_dict = {}
        with open('biler.txt', 'r') as f:
            for line in f.readlines():
                info = line.split()
                car_dict[info[0]] = info[1:]
        while True:
            car_info = les_inn_bilinfo()
            regnr = les_gyldig_vitneskilt()

            possible_matches = match_liste(regnr, car_dict.keys())
            for plate in possible_matches:
                if sjekk_bil(car_info, car_dict[plate]):
                    print(plate, "Eier:", car_dict[plate][-1])

            if input("Vil du registrere flere biler? (J/N)?") == 'N':
                break
    except FileNotFoundError:
        print("Fant ikke fila med biler")

main()