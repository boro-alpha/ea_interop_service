from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_collection import IDualCollection
from ea_interop_service_source.b_code.i_dual_objects.packages.i_dual_package import IDualPackage


class IDualPackageCollection(
    IDualCollection):

    def __init__(
            self,
            ea_collection):
        IDualCollection.__init__(
            self,
            ea_collection=ea_collection)

    def get_at(
            self,
            index: int) \
            -> IDualPackage:
        collection_item = \
            self.ea_collection.GetAt(
                index)

        package = \
            IDualPackage(
                package=collection_item)

        return \
            package
