from ea_interop_service_source.b_code.i_dual_objects.projects.i_project import IProject


class IDualProject(
    IProject):

    def __init__(
            self,
            project):
        IProject.__init__(
            self)

        self.project = \
            project

    def import_package_xmi(
            self,
            package_guid: str,
            filename: str,
            import_diagrams: int,
            strip_guid: int):
        self.project.ImportPackageXMI(
            package_guid,
            filename,
            import_diagrams,
            strip_guid)
