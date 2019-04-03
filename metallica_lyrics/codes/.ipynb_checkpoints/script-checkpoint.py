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

###########################################
### Part 3 - Removing clutter from data ###
###########################################
all_words = straux.remove_verses(all_words)
all_words = straux.remove_chorus(all_words)
all_words = straux.clean_strings(all_words)
all_words = straux.remove_empty_elements(all_words)

###########################################
### Part 4 - Creating cleaned dataframe ###
###########################################
words_df = pd.DataFrame(all_words).rename(columns = {0: 'word'})
words_df = words_df['word'].value_counts()
most_frequent_words = words_df.iloc[0:50]

##############################################
### Part 5 - Plotting and configuring plot ###
##############################################
words_plot = most_frequent_words.plot.barh(x='Index', y='word', 
                                           sort_columns=True, figsize=(12,8), 
                                           title='50 most frequent words in examined Metallica\'s lyrics')
words_plot.set(xlabel='Count', ylabel='Words')
words_plot.invert_yaxis()

# The following for loop is to put the value aside each bar for clearer visualization 
# https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns
# http://robertmitchellv.com/blog-bar-chart-annotations-pandas-mpl.html
for i in words_plot.patches:
    # the +0.6 in the y position is to attempt to centralize it (it's +0.6 because the y axis is inverted)
    words_plot.annotate(str(i.get_width()), xy=(i.get_width(), i.get_y()+0.6), fontsize=8)

#######################################
### Part 6 - Exporting plot as pdf ###
#######################################
fig = words_plot.get_figure()
fig.savefig('../plot.pdf')