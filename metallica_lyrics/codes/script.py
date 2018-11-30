import pandas as pd
import unicodecsv 

######## Part 1 - Creating of metallica subset ########
with open('../datasets/songdata.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    lyrics_list = list(reader)

lyrics_df = pd.DataFrame(lyrics_list)

# the following function returns a dataframe with the condition that the artist is metallica
metallica_lyrics = lyrics_df.loc[lyrics_df['artist'] == 'Metallica']
metallica_lyrics = metallica_lyrics.drop(columns='link') #this column won't be necessary


######## Part 2 - Creating words set ########
words = set() 
# https://stackoverflow.com/questions/18936957/count-distinct-words-from-a-pandas-data-frame
metallica_lyrics['text'].str.lower().str.split().apply(words.update) 
print("Number of unique words: ", len(words))

#TODO: colocar as palavras num dataframe contando as repetições 