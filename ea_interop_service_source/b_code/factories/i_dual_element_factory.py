from ea_interop_service_source.b_code.i_dual_objects.elements.i_dual_element import IDualElement


def create_i_dual_element(
        container,
        element_name: str,
        element_type: str,
        element_notes=str(),
        stereotype_ex=str()) \
        -> IDualElement:
    i_dual_element = \
        IDualElement(
            container.elements.add_new(
                ea_object_name=element_name,
                ea_object_type=element_type))

    if element_notes:
        i_dual_element.notes = \
            element_notes

    if stereotype_ex:
        i_dual_element.stereotype_ex = \
            stereotype_ex

    i_dual_element.update()

    container.elements.refresh()

    return \
        i_dual_element
