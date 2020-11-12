from enum import Enum
from enum import auto
from enum import unique


@unique
class IDualRepositoryCreationResultTypes(
    Enum):
    SUCCEEDED = \
        auto()

    FAILED_TO_OPEN_EA = \
        auto()

    FAILED_TO_OPEN_EA_PROJECT = \
        auto()
