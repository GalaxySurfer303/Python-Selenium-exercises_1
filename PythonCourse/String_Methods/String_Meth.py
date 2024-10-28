print('\n\n')
print('GALAXY SURFER\'s learnigs\nSTRING METHODS')
print('\n\n')
print('split method')

name = 'Paczek Klejment Siwik'
method_name = name.split()

print(method_name)


NIP = '125-136-56-91'
NIP_s = NIP.split("-")
print(NIP_s)
print('\n\n')

print('strip method')
word = 'P A C Z E K '
print(word)

word_strip = word.strip()
print(f'{word_strip}\n\n')


print('endswith & startswith method')
url = 'www.paczek.com'
url_end = url.endswith('.com')
url_start = url.startswith('www')

print(f'{url}\n{url_end}\n{url_start}')
