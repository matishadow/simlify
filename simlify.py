import random


def simlify(string):
    if not isinstance(string, str):
        raise ValueError("Argument must be of type string")

    string_as_list = list(string)

    for i in range(len(string_as_list)):
        char = string_as_list[i]
        if char == 'O':
            string_as_list[i] = 'Ö'
        elif char == 'o':
            string_as_list[i] = 'ö'
        elif char == 'A':
            string_as_list[i] = random.choice(['Å', 'Ä'])
        elif char == 'a':
            string_as_list[i] = random.choice(['å', 'ä'])

    return "".join(string_as_list)


def main():
    lorem_ipsum = 'Proin vitae vestibulum lorem. Phasellus id odio ligula. Sed quis nulla in mi elementum ' \
                  'condimentum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lobortis ipsum eu ' \
                  'gravida ultricies. Vivamus ac posuere lacus. Duis eu ornare nisi, ac sodales risus. '

    print(lorem_ipsum)
    print(simlify(lorem_ipsum))

    return

main()
