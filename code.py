# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    values = dataset[start:end]
    return(values)

    if rows_and_columns == True:
        list_col = [15]
        list_row = [end-start]
        dimension = list_row + list_col
        print(dimension)
        
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    title = []
    duplicate = []
    unique = []

    for rows in dataset:
        title.append(rows[index_])
    for items in title:
        if title.count(items) > 1 and items not in duplicate:
            duplicate.append(items)
        else:
            unique.append(items)

    return duplicate
    return unique
    

def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    #lang = []
    movies_ = []
    for rows in dataset:
        #list of different movie lang 
        #if rows[3] not in lang:
        #    lang.append(rows[3])
        
        if rows[index_] == lang_:
            movies_.append(rows)
    
    return movies_
    #print(lang)

def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """

    rated_movies = []
    for rows in dataset:
        if float(rows[11]) >= rate_low and float(rows[11]) <= rate_high:
            rated_movies.append(rows)
    #print(len(rated_movies))
    return rated_movies


# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)


# The first row is header. Extract and store it in 'movies_header'.
movies_header = movies[0]
print(movies_header)

# Subset the movies dataset such that the header is removed from the list and store it back in movies
del movies[0]
#print(movies)


# Delete wrong data

# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
del movies[4553]


# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore = explore_data(movies,0,2, False)
#print(explore)


# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
dup_and_uni = duplicate_and_unique_movies(movies, 13)
#print(dup_and_uni)


# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
title = []
reviews = []

for rows in movies:
    title.append(rows[13])
    reviews.append(rows[12])


reviews_max = {title[i]: reviews[i] for i in range(len(title))}
#print(reviews_max)

# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 

unique_mov_dict = dict()
temp = []

for key, val in reviews_max.items():
    if key not in temp:
        temp.append(key)
        unique_mov_dict[key] = val

#print(unique_mov_dict)

movies_clean = list(unique_mov_dict.items())
#print(movies_clean)


# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en = movies_lang(movies, 3, "en")
#print(movies_en)

# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies = rate_bucket(movies_en, 8, 10)
print(high_rated_movies)





