import kagglehub
path = kagglehub.dataset_download("carlosgdcj/genius-song-lyrics-with-language-information")
print("Path to dataset files:", path)

import pandas as pd
import os
from tqdm import tqdm

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

directory_path = 'C:\\Users\zheka\.cache\kagglehub\datasets\carlosgdcj\genius-song-lyrics-with-language-information\\versions\\1'
files = os.listdir(directory_path)
file_path = os.path.join(directory_path, 'song_lyrics.csv')
chunks_en = list()
chunks_ru = list()

for chunk in tqdm(pd.read_csv(file_path,
                              chunksize=10000,
                              usecols=['title', 'tag', 'artist',
                                       'year', 'lyrics', 'language', 'views'])):
    # Обработка чанка
    filtered_en_chunk=chunk[chunk['language'].isin(['en'])]
    chunks_en.append(filtered_en_chunk)

    filtered_ru_chunk = chunk[chunk['language'].isin(['ru'])]
    chunks_ru.append(filtered_ru_chunk)
#
# # Объединение чанков в один DataFrame
df_en = pd.concat(chunks_en, axis=0)
df_en.to_csv('English_Songs.csv', index=False)

df_ru = pd.concat(chunks_ru, axis=0)
df_ru.to_csv('Russian_Songs.csv', index=False)


dfru = pd.read_csv('Russian_Genius_Songs.csv')
dfen = pd.read_csv('English_Genius_Songs.csv')
df1 = pd.read_csv('Russian_Songs.csv')
df2 = pd.read_csv('English_Songs.csv')
assert len(dfru) == len(df1)
assert len(dfen) == len(df2)









