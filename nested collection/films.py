movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]

# 1>>> total_number_of_movies
movies_count=len( movies)
print("movie count",movies_count)

# 2>>> movies with genre drama
genre_filter=[m.get("title") for m in movies if "Drama" in m.get("genres")]
print(genre_filter)

# 3>>> latest movie 
def get_year(mov):
     return mov.get("year")
latest_movie_data=max(movies,key=get_year)
movie_year_filter=[m.get("title")for m in movies if m.get("year")==latest_movie_data.get("year")]
print(movie_year_filter)

# 4>>> top movie(movie with highest rating)
def get_rating(mov):
     return mov.get("rating")
top_movie_data=max(movies,key=get_rating)
top_rating_movies=[m.get("title")for m in movies if m.get ("rating")==top_movie_data.get("rating")]
print(top_rating_movies)

# 5>>> movies with language  malayalam
malayalam_movies=[m.get("title")for m in movies if m.get("language")=="Malayalam"]
print(malayalam_movies)

# 6>>> movies released after year 2016
year_filter=[m.get("title")for m in movies if m.get("year")>2016]
print(year_filter)

# 7>>> movie with lowest rating
lowest_rating_movie_data=min(movies,key=get_rating)
lowest_rating_movie=[m.get("title") for m in movies if m.get("rating")==1] 
print(lowest_rating_movie)

# 8>>> malayalam movie with genere action 
malayalam_action_movies=[m.get("title")for m in movies if "Drama" in m.get("genres") and m.get("language")=="Malayalam"]
print(malayalam_action_movies)

# 9>>>  movies released in same years
movie_dictionary={}
for m in movies:
   release_date=m.get("year")
   if release_date in movie_dictionary:
        movie_dictionary.get(release_date).append(m.get("title"))
   else:
       movie_dictionary[release_date]=[m.get("title")]
print(movie_dictionary)

# 10>>> oldest movie 
oldest_movie_data=min(movies,key=get_year)
oldest_movie_names=[m.get("title") for m in movies if m.get ("year")==oldest_movie_data.get("year")]
print(oldest_movie_names)

# 11>>> number of movis released in each year
years=[m.get("year") for m in movies]
year_count={y:years.count(y)for y in years}
print(year_count)

# 12>>> ["Drama","Action","Comedy"]    genres
genres={g for m in movies for g in m.get("genres")}
print(genres)

# 13>>> Action:2,"Drama":2
all_genres=[g for m in movies for g in m.get("genres")]
genre_count={g:all_genres.count(g) for g in all_genres}
print(genre_count)

#set,list,dictionary?
#set comphrension,list comphrension,dictionary comphrension

def get_title(m):
    return m.get("title")
sorted_movies=sorted(movies,key=get_title)
sorted_movies_title=[m.get("title") for m in sorted_movies]
print(sorted_movies_title)