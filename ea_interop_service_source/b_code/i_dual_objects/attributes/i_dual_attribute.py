from ea_interop_service_source.b_code.i_dual_objects.attributes.i_attribute import IAttribute


class IDualAttribute(
    IAttribute):

    def __init__(
            self,
            attribute):
        IAttribute.__init__(
            self)

        self.attribute = \
            attribute

    def __get_attribute_guid(
            self) \
            -> str:
        attribute_guid = \
            self.attribute.AttributeGUID

        return \
            attribute_guid

    def __get_classifier_id(
            self) \
            -> int:
        classifier_id = \
            self.attribute.ClassifierID

        return \
            classifier_id

    def __set_classifier_id(
            self,
            classifier_id: int):
        self.attribute.ClassifierID = \
            classifier_id

    def __get_default(
            self) \
            -> str:
        default = \
            self.attribute.Default

        return \
            default

    def __set_default(
            self,
            default: str):
        self.attribute.Default = \
            default

    def __get_is_ordered(
            self) \
            -> bool:
        is_ordered = \
            self.attribute.IsOrdered

        return \
            is_ordered

    def __set_is_ordered(
            self,
            is_ordered: bool):
        self.attribute.IsOrdered = \
            is_ordered

    def __get_name(
            self) \
            -> str:
        attribute_name = \
            self.attribute.Name

        return \
            attribute_name

    def __set_name(
            self,
            name: str):
        self.attribute.Name = \
            name

    def __get_parent_id(
            self) \
            -> int:
        parent_id = \
            self.attribute.ParentID

        return \
            parent_id

    def __get_pos(
            self) \
            -> int:
        pos = \
            self.attribute.Pos

        return \
            pos

    def __set_pos(
            self,
            pos: int):
        self.attribute.Pos = \
            pos

    def __get_type(
            self) -> str:
        attribute_type = \
            self.attribute.Type

        return \
            attribute_type

    def __set_type(
            self,
            attribute_type: str):
        self.attribute.Type = \
            attribute_type

    def __get_visibility(
            self) -> str:
        visibility = \
            self.attribute.Visibility

        return \
            visibility

    def __set_visibility(
            self,
            visibility: str):
        self.attribute.Visibility = \
            visibility

    def update(
            self):
        self.attribute.Update()

    attribute_guid = \
        property(
            fget=__get_attribute_guid)

    classifier_id = \
        property(
            fget=__get_classifier_id,
            fset=__set_classifier_id)

    default = \
        property(
            fget=__get_default,
            fset=__set_default)

    is_ordered = \
        property(
            fget=__get_is_ordered,
            fset=__set_is_ordered)

    name = \
        property(
            fget=__get_name,
            fset=__set_name)

    parent_id = \
        property(
            fget=__get_parent_id)

    pos = \
        property(
            fget=__get_pos,
            fset=__set_pos)

    type = \
        property(
            fget=__get_type,
            fset=__set_type)

    visibility = \
        property(
            fget=__get_visibility,
            fset=__set_visibility)
