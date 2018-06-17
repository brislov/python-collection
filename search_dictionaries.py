import time


def find(query, dictionary, path=''):
    """ Find key(query) in dictionary.

    :param query: Key to search for
    :param dictionary: Dictionary to search in
    :param path: Used for saving path during recursion
    :return: path, key, value
    """
    for key, value in dictionary.items():
        if key == query:
            yield path + '{', key, value

        elif isinstance(value, dict):
            path += '{\'' + key + '\': '
            for result in find(query, value, path):   # recursion
                yield result


def run(*dictionaries):
    """ A loop for searching keys in passed through dictionaries.

    :param dictionaries: Dictionaries to pass through
    :return: None
    """
    while True:
        query = input('Search key:')

        # Enter "quit" to end loop
        if query.startswith('quit'):
            break

        start_time = time.clock()

        found = False
        times = 0
        for dictionary in dictionaries:
            for path, key, value in find(query, dictionary):

                if key == query:
                    found = True
                    times += 1

                # Output dictionary structure
                output = '{}\'{}\': {}'.format(path, key, value)
                for char in output:
                    if char == '{':
                        output += '}'

                print(output)

        # Search time in ns
        duration = (time.clock() - start_time) * 1000000

        print('Found = {}, Times = {} in {} ns\n'.format(found, times, duration))
