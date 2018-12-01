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

##########################################################
### Part 2 - Storing all unique words across all songs ###
### obs: this part is unnecessary and doesn't reflect  ###
### the truth of the data because the data still has a ###
### lot of clutter in it                               ###
##########################################################
unique_words = set() 
# https://stackoverflow.com/questions/18936957/count-distinct-words-from-a-pandas-data-frame
metallica_df['text'].str.lower().str.split().apply(unique_words.update) 
print("Total of unique words across all", len(metallica_df), "songs:", len(unique_words))
unique_words = list(unique_words) # just to be able to see in the variable explorer

###########################################
### Part 3 - Storing all words in a set ###
###########################################
metallica_list = list(metallica_df['text'])
all_words = straux.generate_string_list(metallica_list)

###################################################
### Part 4 - Removing the clutter from the data ###
###################################################
all_words = straux.remove_verses(all_words)
all_words = straux.remove_chorus(all_words)
all_words = straux.clean_strings(all_words)
all_words = straux.remove_empty_elements(all_words)

########################################################
### Part 5 - Creating cleaned dataframe and plotting ###
########################################################
words_df = pd.DataFrame(all_words).rename(columns = {0: 'word'})