from ea_interop_service_source.b_code.i_dual_objects.projects.i_project import IProject


class INullProject(
    IProject):

    def __init__(
            self):
        IProject.__init__(
            self)
        pass
