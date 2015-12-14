from random import choice, shuffle

def load_words(text_file):
    with open(text_file, 'r', encoding='utf8') as f:
        words = f.read().splitlines()
    return words

def get_matching(items):
    nouns = load_words('nouns.txt')
    words = load_words('words.txt')
    verbs = [word for word in words if word[-3::] == 'ing']
    shuffle(nouns)
    rand_nouns = [nouns.pop() for item in range(items)]
    matching = {rand_nouns[item]:[verb for verb in verbs if verb[0].upper() == rand_nouns[item][0].upper()] for item in range(items)}
    return matching

# def get_matching(items):
#     nouns = load_words('nouns.txt')
#     words = load_words('words.txt')

#     verbs = []
#     for word in words:
#         if word[-3::] == 'ing':
#             verbs.append(word)

#     rand_nouns = []
#     shuffle(nouns)
#     for item in range(items):
#         rand_nouns.append(nouns.pop())

#     matching = {}
#     for noun in rand_nouns:
#         matching[noun] = []
#         for verb in verbs:
#             if verb[0].upper() == noun[0].upper():
#                 matching[noun].append(verb)

#     return matching

def get_suffix(num):
    endings = {1:'st',2:'nd',3:'rd',4:'th'}
    if 10 < num < 20 or num % 10 > 3 or num % 10 == 0:
        return 'th'
    else:
        return endings[num%10]

def display_song(days):
    matching = get_matching(days-5)

    print('On the', str(days) + get_suffix(days), 'day of Christmas, my true love sent to me')

    nouns = list(matching.keys())
    for day in range(days,0,-1):
        if day  <= 5:
            break
        else:
            print(day, nouns[day-6]+'s', 'a', choice(matching[nouns[day-6]]))
    print('5 Gold rings')
    print('4 Calling birds')
    print('3 French hens')
    print('2 Turtle Doves')
    print('and a Partridge in a pair tree')


days = int(input('How many days of Christmas are there?'))
display_song(days)
