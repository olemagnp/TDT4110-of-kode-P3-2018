import random


def sell_ticket(name, ticket, ticket_dict):
    if name in ticket_dict.keys():
        ticket_dict[name].append(ticket)
    else:
        ticket_dict[name] = [ticket]


def draw_numbers(min_ticket, max_ticket, n=5):
    drawn = set()
    while len(drawn) < n:
        drawn.add(random.randint(min_ticket, max_ticket))
    return drawn


def get_winners(ticket_dict, winning_tickets):
    winners = []
    for ticket in winning_tickets:
        for name, tickets in ticket_dict.items():
            if ticket in tickets:
                winners.append(name)
    return winners

ticket_dict = {}
sell_ticket('Ole-Magnus', 1, ticket_dict)
sell_ticket('Ole-Magnus', 2, ticket_dict)
sell_ticket('Geir Kåre', 3, ticket_dict)

winners = draw_numbers(1, 3, 2)

print(get_winners(ticket_dict, winners))
