import media
import fresh_tomatoes

# creation of the movies
shaun = media.Movie(
    "Shaun of the Dead",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA0NDk0NV5BMl"
    "5BanBnXkFtZTcwOTA0OTQzMw@@._V1_SY1000_CR0,0,621,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=LIfcaZ4pC-4")

othe_guys = media.Movie(
    "The Other Guys",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc0NDQzNTA2Ml5BMl"
    "5BanBnXkFtZTcwNzI2OTQzMw@@._V1_.jpg",
    "https://www.youtube.com/watch?v=D6WOoUG1eNo")

hot_fuzz = media.Movie(
    "Hot Fuzz",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTIxODg2NDU1MF5BMl"
    "5BanBnXkFtZTcwOTc3MDM0MQ@@._V1_.jpg",
    "https://www.youtube.com/watch?v=ayTnvVpj9t4")

movies = [shaun, othe_guys, hot_fuzz]

# creation of the movies page
fresh_tomatoes.open_movies_page(movies)
