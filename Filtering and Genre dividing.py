import pandas as pd
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
ru = pd.read_csv('Russian_Songs.csv')
# print(ru.isnull().sum())
# print(ru.duplicated().sum())

en = pd.read_csv('English_Songs.csv')
# print(en.isnull().sum())
# print(en.duplicated().sum())

# print(ru['artist'].value_counts()[:100])
# print(en['artist'].value_counts()[:100])

# Список артистов, которых нужно удалить из датасета
non_musical_artists = [
    "Emily Dickinson", "Abraham Lincoln", "William Shakespeare",
    "Charles Dickens", "(Leo Tolstoy)", "Thomas Hardy",
    "Walt Whitman", "Mark Twain", "Robert Burns", "Holy Bible (KJV)", 'Genius English Translations',
    'Genius Russian Translations ( )'
]
# print('Количество англоязычных документов изначально:  ', len(en))
# print('Количество русскоязычных документов изначально:  ', len(ru))

ru = ru[~ru['artist'].isin(non_musical_artists)]
en = en[~en['artist'].isin(non_musical_artists)]

# print('Количество англоязычных документов после удаления непесенных текстов:  ', len(en))
# print('Количество русскоязычных документов после удаления непесенных текстов:  ', len(ru))

ru_rock = ru[ru['tag'] == 'rock']
ru_pop = ru[ru['tag'] == 'pop']
ru_rap = ru[ru['tag'] == 'rap']

en_rock = en[en['tag'] == 'rock']
en_pop = en[en['tag'] == 'pop']
en_rap = en[en['tag'] == 'rap']

ru_rock.to_csv('Rus_Rock.csv', index=False)
ru_pop.to_csv('Rus_Pop.csv', index=False)
ru_rap.to_csv('Rus_Rap.csv', index=False)

en_rock.to_csv('Eng_Rock.csv', index=False)
en_pop.to_csv('Eng_Pop.csv', index=False)
en_rap.to_csv('Eng_Rap.csv', index=False)