
def mad_libs():
    number = 1
    while number < 5:
        adjective = input('Write down random adjective ') #przymiotnik
        verb = input('Write down random verb ') #czasownik
        noun = input('Write down random noun ') #rzeczownik
        adverb = input('Write down random adverb ') #przysłówek

        print('You look really ' + adjective)
        print('You always like ' + verb)
        print('You look like ' + noun)
        print('You speak %s in english' % adverb)

c = mad_libs()
print(c)