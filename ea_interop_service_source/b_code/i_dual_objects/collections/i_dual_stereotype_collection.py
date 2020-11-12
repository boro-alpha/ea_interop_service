from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_collection import IDualCollection
from ea_interop_service_source.b_code.i_dual_objects.stereotypes.i_dual_stereotype import IDualStereotype


class IDualStereotypeCollection(
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
            -> IDualStereotype:
        collection_item = \
            self.ea_collection.GetAt(
                index)

        stereotype = \
            IDualStereotype(
                stereotype=collection_item)

        return \
            stereotype
