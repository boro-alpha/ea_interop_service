from ea_interop_service_source.b_code.i_dual_objects.i_dual_repository import IDualRepository
from ea_interop_service_source.b_code.i_dual_objects.stereotypes.i_dual_stereotype import IDualStereotype


def create_i_dual_stereotype(
        i_dual_repository: IDualRepository,
        stereotype_name: str) \
        -> IDualStereotype:
    # TODO: Include field AppliesTo in source data as Enum
    hard_coded_stereotype_type = \
        '<all>'

    i_dual_stereotype = \
        IDualStereotype(
            i_dual_repository.stereotypes.add_new(
                ea_object_name=stereotype_name,
                ea_object_type=hard_coded_stereotype_type))

    i_dual_stereotype.update()

    i_dual_repository.stereotypes.refresh()

    return \
        i_dual_stereotype
