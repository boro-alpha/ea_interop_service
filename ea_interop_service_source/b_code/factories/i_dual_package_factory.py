from ea_interop_service_source.b_code.i_dual_objects.packages.i_dual_package import IDualPackage


def create_i_dual_package(
        containing_package: IDualPackage,
        name: str) \
        -> IDualPackage:
    i_dual_package = \
        IDualPackage(
            containing_package.packages.add_new(
                ea_object_name=name,
                ea_object_type='Package'))

    i_dual_package.update()

    return \
        i_dual_package
