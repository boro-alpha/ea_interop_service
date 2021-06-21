from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_connector_collection import \
    IDualConnectorCollection
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

    def __get_elements(
            self) \
            -> IDualElementCollection:
        elements = \
            IDualElementCollection(
                ea_collection=self.package.Elements)

        return \
            elements

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

    def __get_flags(
            self) \
            -> str:
        flags = \
            self.package.Flags

        return \
            flags

    def __set_flags(
            self,
            flags: str):
        self.package.Flags = \
            flags

    def __get_package_guid(
            self) \
            -> str:
        package_guid = \
            self.package.PackageGUID

        return \
            package_guid

    def __get_package_id(
            self) \
            -> int:
        package_id = \
            self.package.PackageID

        return \
            package_id

    def __get_packages(
            self):
        from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_package_collection import \
            IDualPackageCollection

        packages = \
            IDualPackageCollection(
                ea_collection=self.package.Packages)

        return \
            packages

    def __get_connectors(
            self) \
            -> IDualConnectorCollection:
        connector_collection = \
            IDualConnectorCollection(
                ea_collection=self.package.Connectors)

        return \
            connector_collection

    def __get_stereotype_ex(
            self) \
            -> str:
        stereotype_ex = \
            self.package.StereotypeEx

        return \
            stereotype_ex

    def __set_stereotype_ex(
            self,
            stereotype_ex: str):
        self.package.StereotypeEx = \
            stereotype_ex

    def update(
            self):
        self.package.Update()

    def refresh(
            self):
        self.package.Refresh()

    elements = \
        property(
            fget=__get_elements)

    flags = \
        property(
            fget=__get_flags,
            fset=__set_flags)

    name = \
        property(
            fget=__get_name,
            fset=__set_name)

    package_guid = \
        property(
            fget=__get_package_guid)

    package_id = \
        property(
            fget=__get_package_id)

    packages = \
        property(
            fget=__get_packages)

    connectors = \
        property(
            fget=__get_connectors)

    stereotype_ex = \
        property(
            fget=__get_stereotype_ex,
            fset=__set_stereotype_ex)
