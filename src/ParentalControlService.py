from src.Rating import Rating
from src.TitleNotFoundException import TitleNotFoundException
from src.TechnicalFailureExeption import TechnicalFailureExeption


class ParentalControlService():
    def __init__(self, movieService):
        self.movieService = movieService

    def canWatchFilmWithIdAndPreference(self, movieId: str, preference: Rating):
        try:
            return self.__getMovieRatingAndCompareToPreference(movieId, preference)
        except (RuntimeError, TitleNotFoundException, TechnicalFailureExeption):
            return False

    def __getMovieRatingAndCompareToPreference(self, movieId: str, preference: Rating) -> bool:
        movieRatingString = self.movieService.getParentalControlLevel(movieId)
        movieRating = Rating.fromMovieRatingString(movieRatingString)

        return preference >= movieRating
