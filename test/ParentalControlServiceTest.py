import pytest

from src.ParentalControlService import ParentalControlService, Rating
from src.TitleNotFoundException import TitleNotFoundException
from src.TechnicalFailureExeption import TechnicalFailureExeption


@pytest.mark.parametrize("preference", [Rating.UNRATED, Rating.PARENTAL_GUIDANCE, Rating.TWELVE, Rating.FIFTEEN])
def test_films_disallowed_by_preference(mocker, preference):
    movieId = "movieId"
    movieService = mocker.Mock()
    movieService.getParentalControlLevel.return_value = "18"

    parentalControlService = ParentalControlService(movieService)

    canWatch = parentalControlService.canWatchFilmWithIdAndPreference(
        movieId, preference)

    assert canWatch == False


def test_preference_equal_to_parental_control_level(mocker):
    movieId = "movieId"
    movieService = mocker.Mock()
    movieService.getParentalControlLevel.return_value = "12"
    preference = Rating.TWELVE

    parentalControlService = ParentalControlService(movieService)

    canWatch = parentalControlService.canWatchFilmWithIdAndPreference(
        movieId, preference)

    assert canWatch == True


@pytest.mark.parametrize("preference", [Rating.PARENTAL_GUIDANCE, Rating.TWELVE, Rating.FIFTEEN, Rating.EIGHTEEN])
def test_preference_higher_than_parental_control_level(mocker, preference):
    movieId = "movieId"
    movieService = mocker.Mock()
    movieService.getParentalControlLevel.return_value = "U"

    parentalControlService = ParentalControlService(movieService)

    canWatch = parentalControlService.canWatchFilmWithIdAndPreference(
        movieId, preference)

    assert canWatch == True


def test_it_should_return_false_when_rating_is_unknown(mocker):
    movieId = "movieId"
    movieService = mocker.Mock()
    movieService.getParentalControlLevel.side_effect = RuntimeError(
        'Unknown rating unknown')

    parentalControlService = ParentalControlService(movieService)

    canWatch = parentalControlService.canWatchFilmWithIdAndPreference(
        movieId, Rating.EIGHTEEN)

    assert canWatch == False


def test_it_should_return_false_if_title_cannot_be_found(mocker):
    movieId = "movieId"
    movieService = mocker.Mock()
    movieService.getParentalControlLevel.side_effect = TitleNotFoundException()

    parentalControlService = ParentalControlService(movieService)

    canWatch = parentalControlService.canWatchFilmWithIdAndPreference(
        movieId, Rating.EIGHTEEN)

    assert canWatch == False


def test_it_should_return_false_if_Technical_failure(mocker):
    movieId = "movieId"
    movieService = mocker.Mock()
    movieService.getParentalControlLevel.side_effect = TechnicalFailureExeption()

    parentalControlService = ParentalControlService(movieService)

    canWatch = parentalControlService.canWatchFilmWithIdAndPreference(
        movieId, Rating.EIGHTEEN)

    assert canWatch == False
