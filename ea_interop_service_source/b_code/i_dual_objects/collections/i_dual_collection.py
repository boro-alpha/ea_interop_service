from ea_interop_service_source.b_code.i_dual_objects.collections.i_collection import ICollection


class IDualCollection(
    ICollection):

    def __init__(
            self,
            ea_collection):
        ICollection.__init__(
            self)

        self.ea_collection = \
            ea_collection

    def delete(
            self,
            index: int) \
            -> int:
        ea_attribute_parent_id = \
            self.ea_collection.Delete(
                index)

        return \
            ea_attribute_parent_id

    def add_new(
            self,
            ea_object_name: str,
            ea_object_type: str):
        ea_object = \
            self.ea_collection.AddNew(
                ea_object_name,
                ea_object_type)

        return \
            ea_object

    def __get_count(
            self) \
            -> int:
        ea_collection_count = \
            self.ea_collection.Count

        return \
            ea_collection_count

    count = \
        property(
            fget=__get_count)

    def refresh(
            self):
        self.ea_collection.Refresh()
