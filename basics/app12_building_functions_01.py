lang = input('enter your prefered language:')
def greet(lang) :
    if lang == 'es':
        print('hola')
    elif lang == 'fr':
        print('bonjour')
    elif lang == 'ru':
        print('привет')
    elif lang == 'en':
        print('hello')

greet(lang)