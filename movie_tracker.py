import requests
import json, operator

def list_of_popular_movies_by_vote_average():
  # get API and make request
  popular_movie_api = 'https://api.themoviedb.org/3/movie/popular?api_key=e2ebf69d07d1c0ac3760bf3aa16b2cd6&language=en-US&page=1'
  data = requests.get(popular_movie_api)
  data = data.json()

  vote_average_list = []
  for i in range(20):
    # Parse JSON for all vote_average values
    vote_average = data['results'][i]['vote_average']
    # append each value to a list
    vote_average_list.append(vote_average)

  # sort list by high -> low vote_average
  vote_average_list.sort()
  vote_average_list.reverse()

  popular_movies = []

  # get movie title for each corresponding vote average
  for num in vote_average_list:
    for i in range(20):
      if (data['results'][i]['vote_average'] == num):
        popular_movies.append(data['results'][i]['title'])

  # print the top 5 movies (first 5 in the list)
  print("The 5 most popular movies right now are: ", popular_movies[:5])
