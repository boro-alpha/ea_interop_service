from ea_interop_service_source.b_code.i_dual_objects.diagrams.i_dual_diagram import IDualDiagram


def create_i_dual_diagram(
        container,
        diagram_name: str,
        diagram_type: str) \
        -> IDualDiagram:
    i_dual_diagram = \
        IDualDiagram(
            container.diagrams.add_new(
                ea_object_name=diagram_name,
                ea_object_type=diagram_type))

    i_dual_diagram.update()

    container.diagrams.refresh()

    return \
        i_dual_diagram
