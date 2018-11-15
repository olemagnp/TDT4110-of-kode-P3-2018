import sys


def read_stock(filename):
    stock_dict = {}

    try:
        with open(filename, 'r') as f:
            for line in f:
                info = line.split(';')

                if info[0] not in stock_dict:
                    stock_dict[info[0]] = {}

                stock_dict[info[0]][info[1]] = [float(info[2]), int(info[3])]
    except FileNotFoundError:
        print("Could not find file at '" + filename + "'")
        sys.exit(1)
    return stock_dict


def write_stock(stock, filename):
    stock_str = ""

    for make, model_info in stock.items():
        for model, info in model_info.items():
            stock_str += f"{make};{model};{info[0]};{info[1]}\n"

    with open(filename, 'w') as f:
        f.write(stock_str)

stock = read_stock('stock.txt')
write_stock(stock, 'new_stock.txt')
