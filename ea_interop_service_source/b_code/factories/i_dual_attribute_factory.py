from ea_interop_service_source.b_code.i_dual_objects.attributes.i_dual_attribute import IDualAttribute
from ea_interop_service_source.b_code.i_dual_objects.elements.i_dual_element import IDualElement


def create_i_dual_attribute(
        attributed_object: IDualElement,
        attribute_name: str,
        attribute_type: IDualElement,
        attribute_visibility: str,
        ea_attribute_type_name: str,
        ea_attribute_initial_value: str) \
        -> IDualAttribute:
    if attribute_type is not None:
        attribute_type_name = \
            attribute_type.name

    else:
        attribute_type_name = \
            ea_attribute_type_name

    i_dual_attribute = \
        IDualAttribute(
            attributed_object.attributes.add_new(
                ea_object_name=attribute_name,
                ea_object_type=attribute_type_name))

    if attribute_type is not None:
        i_dual_attribute.classifier_id = \
            attribute_type.element_id

    if ea_attribute_initial_value is not None:
        i_dual_attribute.default = \
            ea_attribute_initial_value

    i_dual_attribute.visibility = \
        attribute_visibility

    i_dual_attribute.update()

    return \
        i_dual_attribute
