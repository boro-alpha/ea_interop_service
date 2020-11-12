from ea_interop_service_source.b_code.i_dual_objects.i_repository import IRepository


class INullRepository(
    IRepository):

    def __init__(
            self):
        IRepository.__init__(
            self)
        pass
