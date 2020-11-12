from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_attribute_collection import \
    IDualAttributeCollection
from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_connector_collection import \
    IDualConnectorCollection
from ea_interop_service_source.b_code.i_dual_objects.elements.i_element import IElement


class IDualElement(
    IElement):

    def __init__(
            self,
            element):
        IElement.__init__(
            self)

        self.element = \
            element

    def __get_attributes(
            self) \
            -> IDualAttributeCollection:
        attribute_collection = \
            IDualAttributeCollection(
                ea_collection=self.element.Attributes)

        return \
            attribute_collection

    def __get_classifier_id(
            self) \
            -> int:
        classifier_id = \
            self.element.ClassifierID

        return \
            classifier_id

    def __set_classifier_id(
            self,
            classifier_id: int):
        self.element.ClassifierID = \
            classifier_id

        self.element.Update()

    def __get_connectors(
            self) \
            -> IDualConnectorCollection:
        connector_collection = \
            IDualConnectorCollection(
                ea_collection=self.element.Connectors)

        return \
            connector_collection

    def __get_element_guid(
            self) \
            -> str:
        element_guid = \
            self.element.ElementGUID

        return \
            element_guid

    def __get_element_id(
            self) \
            -> int:
        element_id = \
            self.element.ElementID

        return \
            element_id

    def __get_elements(
            self):
        from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_element_collection import \
            IDualElementCollection

        element_collection = \
            IDualElementCollection(
                ea_collection=self.element.Elements)

        return \
            element_collection

    def __get_name(
            self) \
            -> str:
        element_name = \
            self.element.Name

        return \
            element_name

    def __set_name(
            self,
            name: str):
        self.element.Name = \
            name

    def __get_package_id(
            self) \
            -> int:
        package_id = \
            self.element.PackageID

        return \
            package_id

    def __set_package_id(
            self,
            package_id: int):
        self.element.PackageID = \
            package_id

    def update(
            self):
        self.element.Update()

    def refresh(
            self):
        self.element.Refresh()

    attributes = \
        property(
            fget=__get_attributes)

    classifier_id = \
        property(
            fget=__get_classifier_id,
            fset=__set_classifier_id)

    connectors = \
        property(
            fget=__get_connectors)

    element_guid = \
        property(
            fget=__get_element_guid)

    element_id = \
        property(
            fget=__get_element_id)

    elements = \
        property(
            fget=__get_elements)

    name = \
        property(
            fget=__get_name,
            fset=__set_name)

    package_id = \
        property(
            fget=__get_package_id,
            fset=__set_package_id)
