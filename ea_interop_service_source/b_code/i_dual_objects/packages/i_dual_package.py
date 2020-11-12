from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_element_collection import IDualElementCollection
from ea_interop_service_source.b_code.i_dual_objects.packages.i_package import IPackage


class IDualPackage(
    IPackage):

    def __init__(
            self,
            package):
        IPackage.__init__(
            self)

        self.package = \
            package

    def __get_name(
            self) \
            -> str:
        element_name = \
            self.package.Name

        return \
            element_name

    def __set_name(
            self,
            name: str):
        self.package.Name = \
            name

    def __get_package_guid(
            self) \
            -> str:
        package_guid = \
            self.package.PackageGUID

        return \
            package_guid

    def __get_packages(
            self):
        from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_package_collection import \
            IDualPackageCollection

        packages = \
            IDualPackageCollection(
                ea_collection=self.package.Packages)

        return \
            packages

    def __get_elements(
            self) \
            -> IDualElementCollection:
        elements = \
            IDualElementCollection(
                ea_collection=self.package.Elements)

        return \
            elements

    def update(
            self):
        self.package.Update()

    def refresh(
            self):
        self.package.Refresh()

    package_guid = \
        property(
            fget=__get_package_guid)

    packages = \
        property(
            fget=__get_packages)

    elements = \
        property(
            fget=__get_elements)

    name = \
        property(
            fget=__get_name,
            fset=__set_name)
