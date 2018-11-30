# -*- coding: utf-8 -*-
import pandas as pd
import unicodecsv

#created this just for readability
#def subset_df(column: str, condition: str, df):
#    return df.loc[df[column] == condition]

with open('../datasets/songdata.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    lyrics_list = list(reader)

lyrics_df = pd.DataFrame(lyrics_list)

# the following function returns a dataframe with the condition that the artist is metallica
metallica_lyrics = lyrics_df.loc[lyrics_df['artist'] == 'Metallica']
#metallica_lyrics = subset_df('artist', 'Metallica', lyrics_df)
metallica_lyrics = metallica_lyrics.drop(columns='link')