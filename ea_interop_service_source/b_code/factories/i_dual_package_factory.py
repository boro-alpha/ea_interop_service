from ea_interop_service_source.b_code.common_knowledge.package_view_types import PackageViewTypes
from ea_interop_service_source.b_code.i_dual_objects.packages.i_dual_package import IDualPackage


def create_i_dual_package(
        containing_package: IDualPackage,
        name: str,
        package_view_type: PackageViewTypes = PackageViewTypes.NOT_SET) \
        -> IDualPackage:
    i_dual_package = \
        IDualPackage(
            containing_package.packages.add_new(
                ea_object_name=name,
                ea_object_type='Package'))

    if package_view_type != PackageViewTypes.NOT_SET:
        i_dual_package.flags = \
            package_view_type.flags

    i_dual_package.update()

    containing_package.packages.refresh()

    return \
        i_dual_package
