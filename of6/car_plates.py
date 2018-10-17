import random


def generate_single_license():
    allowed_strings = ['BS', 'CV', 'EL', 'FY',
                       'KU', 'LE', 'NB', 'PC',
                       'SY', 'WC']
    return random.choice(allowed_strings) \
           + str(random.randint(10000, 99999))


def generate_license_numbers(amount):
    plates = []

    for i in range(amount):
        plate = generate_single_license()

        while plate in plates:
            plate = generate_single_license()

        plates.append(plate)
    return plates


def generate_license_plate_2(amount):
    plates = set()

    while len(plates) < amount:
        plates.add(generate_single_license())

    return plates

print(generate_license_numbers(10))
