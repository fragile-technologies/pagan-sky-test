import pytest

from src.Rating import Rating


@pytest.mark.parametrize("ratingStr,expectedRating", [("U", Rating.UNRATED),
                                                       ("PG", Rating.PARENTAL_GUIDANCE),
                                                       ("12", Rating.TWELVE),
                                                       ("15", Rating.FIFTEEN),
                                                       ("18", Rating.EIGHTEEN)
                                                       ]
                          )
def test_it_should_map_all_movie_ratings_from_string(ratingStr, expectedRating):
    assert Rating.fromMovieRatingString(ratingStr) == expectedRating

def test_it_should_raise_exception_when_passed_unknown_movie_rating():
    unknownRating = "Nonexistent"
    with pytest.raises(RuntimeError):
        Rating.fromMovieRatingString(unknownRating)
