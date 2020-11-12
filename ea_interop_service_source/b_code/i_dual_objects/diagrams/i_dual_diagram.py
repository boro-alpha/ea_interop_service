from ea_interop_service_source.b_code.i_dual_objects.diagrams.i_diagram import IDiagram


class IDualDiagram(
    IDiagram):

    def __init__(
            self,
            diagram):
        IDiagram.__init__(
            self)

        self.diagram = \
            diagram

    def __get_name(
            self) \
            -> str:
        diagram_name = \
            self.diagram.Name

        return \
            diagram_name

    def __set_name(
            self,
            name: str):
        self.diagram.Name = \
            name

    def update(
            self):
        self.diagram.Update()

    name = \
        property(
            fget=__get_name,
            fset=__set_name)
