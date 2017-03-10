import fresh_tomatoes
import media

les_miserables = media.Movie(r"Les Miserables", r"Set in France during the early 19th century, the film tells the story of Jean Valjean, an ex-convict who, inspired by a kindly bishop, decides to turn his life around.", r"https://upload.wikimedia.org/wikipedia/en/b/b0/Les-miserables-movie-poster1.jpg", r"https://www.youtube.com/watch?v=YmvHzCLP6ug", "PG-13", "2h 38min", "Musical", "7.6")

interstellar = media.Movie("Interstellar", "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival. ", r"https://upload.wikimedia.org/wikipedia/ro/thumb/b/bc/Interstellar_film_poster.jpg/260px-Interstellar_film_poster.jpg", r"https://www.youtube.com/watch?v=Rt2LHkSwdPQ","PG-13", "2h 49min", "Sci-Fi", "8.6")

arrival = media.Movie("Arrival", "When twelve mysterious spacecraft appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien visitors. ", r"https://upload.wikimedia.org/wikipedia/en/archive/d/df/20161020171048!Arrival,_Movie_Poster.jpg", r"https://www.youtube.com/watch?v=tFMo3UJ4B4g", "PG-13", "1h 56min", "Sci-Fi", "8.0")

the_butterfly_effect = media.Movie("The butterfly effect", "Evan Treborn suffers blackouts during significant events of his life. As he grows up, he finds a way to remember these lost memories and a supernatural way to alter his life by reading his journal. ", r"https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg", r"https://www.youtube.com/watch?v=1YMs41xh52c", "R", "1h 53min", "Sci-Fi", "7.7")

the_godfather = media.Movie("The godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son. ", r"https://upload.wikimedia.org/wikipedia/en/a/af/The_Godfather,_The_Game.jpg", r"https://www.youtube.com/watch?v=sY1S34973zA", "R", "2h 55min", "Crime", "9.2")

the_lion_king = media.Movie("The lion king", "Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble. ", r"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", r"https://www.youtube.com/watch?v=4sj1MT05lAA", "G", "1h 28min", "Animation", "8.5")

game_of_thrones = media.Series("Game of Thrones","Nine noble families fight for control over the mythical lands of Westeros; A forgotten race returns after being dormant for thousands of years.", r"https://upload.wikimedia.org/wikipedia/en/d/d8/Game_of_Thrones_title_card.jpg", r"https://www.youtube.com/watch?v=Qq0B0NVKghA","R", "56 min", "Adventure", "9.5","7", "73" )

westworld = media.Series("Westworld", "Set at the intersection of the near future and the reimagined past, explore a world in which every human appetite can be indulged. ",r"https://static.independent.co.uk/s3fs-public/thumbnails/image/2016/11/19/12/westworld-hbo-1.jpg", r"https://www.youtube.com/watch?v=IuS5huqOND4", "TV-MA","1h","Sci-Fi","9.1","2","20" )

naruto = media.Series("Naruto: Shippuden", "Naruto Uzumaki, is a loud, hyperactive, adolescent ninja who constantly searches for approval and recognition, as well as to become Hokage, who is acknowledged as the leader and strongest of all ninja in the village. ",r"http://vignette4.wikia.nocookie.net/toonami/images/0/08/Shipuden.jpg/revision/latest/scale-to-width-down/300?cb=20131107012205",r"https://www.youtube.com/watch?v=1WLO0Owi5-A","TV-14","24 min", "Animation", "8.5","24","500" )

movies = [les_miserables, the_godfather ,the_lion_king, interstellar, arrival, game_of_thrones, the_butterfly_effect, westworld, naruto]
fresh_tomatoes.open_movies_page(movies)

