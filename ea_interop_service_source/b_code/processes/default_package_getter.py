from ea_interop_service_source.b_code.i_dual_objects.i_dual_repository import IDualRepository
from ea_interop_service_source.b_code.i_dual_objects.packages.i_dual_package import IDualPackage


def get_default_i_dual_package(
        i_dual_repository: IDualRepository) \
        -> IDualPackage:
    default_i_dual_model = \
        i_dual_repository.models.get_at(
            index=0)

    default_i_dual_view = \
        default_i_dual_model.packages.get_at(
            index=0)

    default_i_dual_package = \
        default_i_dual_view.packages.get_at(
            index=0)

    return \
        default_i_dual_package
