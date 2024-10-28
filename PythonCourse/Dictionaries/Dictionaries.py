#słowniki
#Dictionaries

print('\n\ndefault dictionary created by me')
print('================================')
Dict_One = {'Poland':'Warsaw', 'Thailand':'Bangkok', 'USA':'Washington', 'France':'Paris',
            'Spain': 'Madrit', 'Canada':'Ottawa', 'Mexico':'Mexico', 'Egipt':'Cairo',
            'Rep of Congo':'Kinshasa', 'Russia':'Moscov', 'Ukraine':'Kiev',
            'Jupiter':['IO', 'Europa', 'Ganimedes', 'No Name Moon']}
print(f'\n{Dict_One}\n\n\n')

spain_cap = Dict_One['Spain']
spain_cap2 = Dict_One.get('Spain')

print(f'{spain_cap} {spain_cap2}')

#OPTION ONE - adding
#add new key and value to existing dictionary (Dict_One)
Dict_One['Germany'] = 'Berlin'

#OPTION TWO - adding
Dict_One.update({'India':'New Deli'})
print('\n\nupdated dictionary created by me')
print('================================')
print(Dict_One)

print('\n\nelements on my dictionary')
print('================================')
print(len(Dict_One))

print('\n\nJupiter moons')
print('================================')
Jup_moons = Dict_One['Jupiter']
print(Jup_moons)


