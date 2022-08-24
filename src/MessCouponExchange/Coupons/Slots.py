import enum


class Slots(str, enum.Enum):
    """
    Enum for the slots of mess
    """

    BREAKFAST = "1"
    LUNCH = "2"
    SNACK = "3"
    DINNER = "4"
