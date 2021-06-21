from enum import Enum
from enum import auto
from enum import unique


@unique
class PackageViewTypes(
    Enum):
    NOT_SET = \
        auto()

    SIMPLE = \
        auto()

    USE_CASE = \
        auto()

    DYNAMIC = \
        auto()

    CLASS_VIEW = \
        auto()

    COMPONENT = \
        auto()

    DEPLOYMENT = \
        auto()

    def __get_flags(
            self) \
            -> str:
        return \
            package_view_type_to_flags_mapping[self]

    flags = \
        property(
            fget=__get_flags)


package_view_type_to_flags_mapping = \
    {
        PackageViewTypes.SIMPLE: 'VICON=6;',
        PackageViewTypes.USE_CASE: 'VICON=1;',
        PackageViewTypes.DYNAMIC: 'VICON=2;',
        PackageViewTypes.CLASS_VIEW: 'VICON=3;',
        PackageViewTypes.COMPONENT: 'VICON=4;',
        PackageViewTypes.DEPLOYMENT: 'VICON=5;'
    }
