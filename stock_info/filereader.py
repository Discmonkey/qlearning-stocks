import os


def read_file(filepath=None):
    if filepath is None:
        filepath = os.path.join((os.path.dirname(__file__)), 'stock_monitor')

    with open(filepath) as f:
        all_stocks = [line.strip() for line in f]

    return all_stocks


if __name__ == '__main__':
    print(read_file())