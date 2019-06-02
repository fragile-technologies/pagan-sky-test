from enum import IntEnum


class Rating(IntEnum):
    UNRATED = 1
    PARENTAL_GUIDANCE = 2
    TWELVE = 3
    FIFTEEN = 4
    EIGHTEEN = 5

    @staticmethod
    def fromMovieRatingString(rating: str) -> "Rating":
        if rating == "18":
            return Rating.EIGHTEEN
        elif rating == "15":
            return Rating.FIFTEEN
        elif rating == "12":
            return Rating.TWELVE
        elif rating == "PG":
            return Rating.PARENTAL_GUIDANCE
        elif rating == "U":
            return Rating.UNRATED

        raise RuntimeError(f"Unknown movie rating {rating}")
