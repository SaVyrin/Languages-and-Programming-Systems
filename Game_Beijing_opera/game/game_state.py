from enum import Enum


class GameState(Enum):
    NOT_STARTED = 0,
    PLAYING = 1,
    STOPPED = 2,
    WON = 3,
    LOST = 4
    FINISHED = 5
