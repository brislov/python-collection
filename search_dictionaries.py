import time


def find(query, dictionary):
    """ Find key(query) in dictionary. Can handle nested dictionaries and returns a generator list of tuples with
    each tuple consisting of path, key and value for each find. """
    for key, value in dictionary.items():
        if key == query:
            path = key
            yield (path, key, value)
        elif isinstance(value, dict):
            for p, k, v in find(query, value):  # recursion
                yield (key + ' -> ' + p, k, v)


def search_dictionaries(*dictionaries):
    """ Loop for searching keys in passed through dictionaries. """
    while True:
        query = input('Search key: ')

        # Type "quit" to end loop
        if query.startswith('quit'):
            break

        found = False
        times = 0
        str_out = ''
        start_time = time.clock()

        for dictionary in dictionaries:
            for path, key, value in find(query, dictionary):
                found = True
                times += 1
                str_out += '\t{}{}: {}\n'.format(path[:-len(key)], key, value)

        # Search time in ms
        elapsed_time = (time.clock() - start_time) * 10**6

        str_out += '\n\tFound = {}, Times = {} \tin {} ms\n'.format(found, times, elapsed_time)

        print(str_out)
