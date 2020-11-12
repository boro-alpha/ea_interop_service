from ea_interop_service_source.b_code.i_dual_objects.stereotypes.i_stereotype import IStereotype


class IDualStereotype(
    IStereotype):

    def __init__(
            self,
            stereotype):
        IStereotype.__init__(
            self)

        self.stereotype = \
            stereotype

    def __get_name(
            self) \
            -> str:
        stereotype_name = \
            self.stereotype.Name

        return \
            stereotype_name

    def __set_name(
            self,
            name: str):
        self.stereotype.Name = \
            name

    def __get_notes(
            self) \
            -> str:
        stereotype_notes = \
            self.stereotype.Notes

        return \
            stereotype_notes

    def __set_notes(
            self,
            notes: str):
        self.stereotype.Notes = \
            notes

    def __get_stereotype_guid(
            self) \
            -> str:
        stereotype_guid = \
            self.stereotype.StereotypeGUID

        return \
            stereotype_guid

    def update(
            self):
        self.stereotype.Update()

    stereotype_guid = \
        property(
            fget=__get_stereotype_guid)

    name = \
        property(
            fget=__get_name,
            fset=__set_name)

    notes = \
        property(
            fget=__get_notes,
            fset=__set_notes)
