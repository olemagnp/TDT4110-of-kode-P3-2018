
def payment(ticket_price, num_tickets):
    price = ticket_price * num_tickets
    if num_tickets > 3:
        price *= 0.9
    return price


def get_price(concert):
    with open('prices.txt', 'r') as f:
        for line in f.readlines():
            info = line.strip().split(';')
            if info[0] == concert:
                return int(info[1])
    return -1


def ticket(buyer, concert, num_tickets):
    ticket_price = get_price(concert)
    total = payment(ticket_price, num_tickets)

    ticket_string = '*' * 40 + '\n'
    ticket_string += 'Uka 2015\n'
    ticket_string += '*' * 40 + '\n'
    ticket_string += 'Navn:'.rjust(17) + buyer.rjust(23) + '\n'
    ticket_string += 'Konsert:'.rjust(17) + concert.rjust(23) + '\n'
    ticket_string += 'Antall billetter:'.rjust(17) + str(num_tickets).rjust(23) + '\n'
    ticket_string += 'Total pris:'.rjust(17) + (str(total) + " kr").rjust(23)

    print(ticket_string)


def write_to_file(buyer, concert, num_tickets, filename):
    ticket_price = get_price(concert)
    total_price = payment(ticket_price, num_tickets)

    data_string = concert + ";"
    data_string += str(num_tickets) + ";"
    data_string += str(total_price) + ";"
    data_string += buyer + "\n"

    with open(filename, 'a') as f:
        f.write(data_string)


write_to_file("Ole-Magnus", "The Rectorats", 8, "concerts.txt")
ticket("Ole-Magnus", "The Rectorats", 8)