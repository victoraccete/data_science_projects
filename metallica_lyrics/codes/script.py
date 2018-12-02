#import os
#os.chdir('C:/Users/Victor/data_science_projects/metallica_lyrics/codes')
import pandas as pd
import unicodecsv 
import stringAux as straux

#############################################
### Part 1 - Creating a metallica subset ####
#############################################
with open('../datasets/songdata.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    lyrics_list = list(reader)
    
lyrics_df = pd.DataFrame(lyrics_list)
lyrics_df = lyrics_df.drop(columns = 'link') # this column won't be necessary
# the following function returns a dataframe provided that the artist is metallica
metallica_df = lyrics_df.loc[lyrics_df['artist'] == 'Metallica']

###########################################
### Part 2 - Storing all words in a set ###
###########################################
metallica_list = list(metallica_df['text'])
all_words = straux.generate_string_list(metallica_list)

###################################################
### Part 3 - Removing the clutter from the data ###
###################################################
all_words = straux.remove_verses(all_words)
all_words = straux.remove_chorus(all_words)
all_words = straux.clean_strings(all_words)
all_words = straux.remove_empty_elements(all_words)

########################################################
### Part 4 - Creating cleaned dataframe and plotting ###
########################################################
words_df = pd.DataFrame(all_words).rename(columns = {0: 'word'})
words_df = words_df['word'].value_counts()
most_frequent_words = words_df.iloc[0:50]

#TODO: plot most frequent words as a bar plot