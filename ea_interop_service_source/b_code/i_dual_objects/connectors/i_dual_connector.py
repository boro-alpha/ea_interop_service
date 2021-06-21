from ea_interop_service_source.b_code.i_dual_objects.connectors.i_connector import IConnector


class IDualConnector(
    IConnector):

    def __init__(
            self,
            connector):
        IConnector.__init__(
            self)

        self.connector = \
            connector

    def __get_client_id(
            self) \
            -> int:
        client_id = \
            self.connector.ClientID

        return \
            client_id

    def __set_client_id(
            self,
            client_id: int):
        self.connector.ClientID = \
            client_id

    def __get_color(
            self) \
            -> int:
        color = \
            self.connector.Color

        return \
            color

    def __set_color(
            self,
            color: int):
        self.connector.Color = \
            color

    def __get_connector_guid(
            self) \
            -> str:
        connector_guid = \
            self.connector.ConnectorGUID

        return \
            connector_guid

    def __get_connector_id(
            self) \
            -> int:
        connector_id = \
            self.connector.ConnectorID

        return \
            connector_id

    def __get_direction(
            self) \
            -> str:
        direction = \
            self.connector.Direction

        return \
            direction

    def __set_direction(
            self,
            direction: str):
        self.connector.Direction = \
            direction

    def __get_stereotype(
            self) \
            -> str:
        stereotype = \
            self.connector.Stereotype

        return \
            stereotype

    def __set_stereotype(
            self,
            stereotype: str):
        self.connector.Stereotype = \
            stereotype

    def __get_stereotype_ex(
            self) \
            -> str:
        stereotype_ex = \
            self.connector.StereotypeEx

        return \
            stereotype_ex

    def __set_stereotype_ex(
            self,
            stereotype_ex: str):
        self.connector.StereotypeEx = \
            stereotype_ex

    def __get_supplier_id(
            self) \
            -> int:
        supplier_id = \
            self.connector.SupplierID

        return \
            supplier_id

    def __set_supplier_id(
            self,
            supplier_id: int):
        self.connector.SupplierID = \
            supplier_id

    def __get_width(
            self) \
            -> int:
        width = \
            self.connector.Width

        return \
            width

    def __set_width(
            self,
            width: int):
        self.connector.Width = \
            width

    def __get_notes(
            self) \
            -> str:
        element_notes = \
            self.connector.Notes

        return \
            element_notes

    def __set_notes(
            self,
            notes: str):
        self.connector.Notes = \
            notes

    def update(
            self):
        self.connector.Update()

    client_id = \
        property(
            fget=__get_client_id,
            fset=__set_client_id)

    color = \
        property(
            fget=__get_color,
            fset=__set_color)

    connector_guid = \
        property(
            fget=__get_connector_guid)

    connector_id = \
        property(
            fget=__get_connector_id)

    direction = \
        property(
            fget=__get_direction,
            fset=__set_direction)

    stereotype = \
        property(
            fget=__get_stereotype,
            fset=__set_stereotype)

    stereotype_ex = \
        property(
            fget=__get_stereotype_ex,
            fset=__set_stereotype_ex)

    supplier_id = \
        property(
            fget=__get_supplier_id,
            fset=__set_supplier_id)

    width = \
        property(
            fget=__get_width,
            fset=__set_width)

    notes = \
        property(
            fget=__get_notes,
            fset=__set_notes)
