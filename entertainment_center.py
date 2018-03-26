import media
import fresh_tomatoes

cold_war = media.Movie("Cold War", 
                       "https://img.char.tw/uploads/2017/08/1502983441-ae9a662bcafd635a2595e7892dc792c3.jpg", 
                       "https://www.youtube.com/watch?v=6_SAdcvKbaY");

cold_war_two = media.Movie("Cold War II", 
                           "https://chingszechuen01.files.wordpress.com/2016/07/coldwar.jpg",
                           "https://www.youtube.com/watch?v=LzcOQhHYzgw");

star_wars_fa = media.Movie("Star Wars:<br>The Force Awakens", 
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcT6nGxj1D4P-9EiVSY32sb6Ql-XQrbeK5FgM37UI6QxcZwfcfVw", # NOQA
                           "https://www.youtube.com/watch?v=UitsQDWSlUg");

star_wars_lj = media.Movie("Star Wars:<br>The Last Jedi", 
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcRgcIU4MKHZkZNeDt_tAewyfwX7PAmSdj_7wdg_FInkZw8Um9F_", # NOQA
                           "https://www.youtube.com/watch?v=Q0CbN8sfihY");

eva_alone = media.Movie("Eva:<br>You Are (Not) Alone", 
                        "https://image.tmdb.org/t/p/w1280/12hS3pC0dG31JteNj56NscKDX9A.jpg", 
                        "https://www.youtube.com/watch?v=k3FYymwS4RM");

eva_advance = media.Movie("Eva:<br>You Can (Not) Advance", 
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcSx2EVXG44dnybJe7j3gifGcuEuDVO2cmYPyiOVcqT3aYNEj2y4", # NOQA
                          "https://www.youtube.com/watch?v=0qil1D3KcqE");

movies = [cold_war, cold_war_two, star_wars_fa, star_wars_lj, eva_alone, eva_advance]

fresh_tomatoes.open_movies_page(movies);
