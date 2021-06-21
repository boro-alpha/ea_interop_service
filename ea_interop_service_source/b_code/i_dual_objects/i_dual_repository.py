from ea_interop_service_source.b_code.i_dual_objects.attributes.i_attribute import IAttribute
from ea_interop_service_source.b_code.i_dual_objects.attributes.i_dual_attribute import IDualAttribute
from ea_interop_service_source.b_code.i_dual_objects.attributes.i_null_attribute import INullAttribute
from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_package_collection import IDualPackageCollection
from ea_interop_service_source.b_code.i_dual_objects.collections.i_dual_stereotype_collection import \
    IDualStereotypeCollection
from ea_interop_service_source.b_code.i_dual_objects.connectors.i_connector import IConnector
from ea_interop_service_source.b_code.i_dual_objects.connectors.i_dual_connector import IDualConnector
from ea_interop_service_source.b_code.i_dual_objects.connectors.i_null_connector import INullConnector
from ea_interop_service_source.b_code.i_dual_objects.diagrams.i_diagram import IDiagram
from ea_interop_service_source.b_code.i_dual_objects.diagrams.i_dual_diagram import IDualDiagram
from ea_interop_service_source.b_code.i_dual_objects.diagrams.i_null_diagram import INullDiagram
from ea_interop_service_source.b_code.i_dual_objects.elements.i_dual_element import IDualElement
from ea_interop_service_source.b_code.i_dual_objects.elements.i_element import IElement
from ea_interop_service_source.b_code.i_dual_objects.elements.i_null_element import INullElement
from ea_interop_service_source.b_code.i_dual_objects.i_repository import IRepository
from ea_interop_service_source.b_code.i_dual_objects.packages.i_dual_package import IDualPackage
from ea_interop_service_source.b_code.i_dual_objects.packages.i_null_package import INullPackage
from ea_interop_service_source.b_code.i_dual_objects.packages.i_package import IPackage
from ea_interop_service_source.b_code.i_dual_objects.projects.i_dual_project import IDualProject
from ea_interop_service_source.b_code.i_dual_objects.projects.i_null_project import INullProject
from ea_interop_service_source.b_code.i_dual_objects.projects.i_project import IProject


class IDualRepository(
    IRepository):

    def __init__(
            self,
            repository):
        IRepository.__init__(
            self)

        self.repository = \
            repository

    def __enter__(
            self):
        return \
            self

    def __exit__(
            self,
            exception_type,
            exception_value,
            traceback):
        self.exit()

    def custom_command(
            self,
            *args):
        self.repository.CustomCommand(
            *args)

    def get_attribute_by_guid(
            self,
            attribute_guid: str) \
            -> IAttribute:
        attribute = \
            self.repository.GetAttributeByGuid(
                attribute_guid)

        if not attribute:
            return \
                INullAttribute()

        i_dual_attribute = \
            IDualAttribute(
                attribute=attribute)

        return \
            i_dual_attribute

    def get_connector_by_guid(
            self,
            connector_ea_guid: str) \
            -> IConnector:
        connector = \
            self.repository.GetConnectorByGuid(
                connector_ea_guid)

        if not connector:
            return \
                INullConnector()

        i_dual_connector = \
            IDualConnector(
                connector=connector)

        return \
            i_dual_connector

    def get_connector_by_id(
            self,
            connector_id: int) \
            -> IConnector:
        connector = \
            self.repository.GetConnectorByID(
                connector_id)

        if not connector:
            return \
                INullConnector()

        i_dual_connector = \
            IDualConnector(
                connector=connector)

        return \
            i_dual_connector

    def get_element_by_guid(
            self,
            element_ea_guid: str) \
            -> IElement:
        element = \
            self.repository.GetElementByGuid(
                element_ea_guid)

        if not element:
            return \
                INullElement()

        i_dual_element = \
            IDualElement(
                element=element)

        return \
            i_dual_element

    def get_element_by_id(
            self,
            element_id: int) \
            -> IElement:
        element = \
            self.repository.GetElementByID(
                element_id)

        if not element:
            return \
                INullElement()

        i_dual_element = \
            IDualElement(
                element=element)

        return \
            i_dual_element

    def get_diagram_by_guid(
            self,
            diagram_ea_guid: str) \
            -> IDiagram:
        diagram = \
            self.repository.GetDiagramByGuid(
                diagram_ea_guid)

        if not diagram:
            return \
                INullDiagram()

        i_dual_diagram = \
            IDualDiagram(
                diagram=diagram)

        return \
            i_dual_diagram

    def get_diagram_by_id(
            self,
            diagram_id: int) \
            -> IDiagram:
        diagram = \
            self.repository.GetDiagramByID(
                diagram_id)

        if not diagram:
            return \
                INullDiagram()

        i_dual_diagram = \
            IDualDiagram(
                diagram=diagram)

        return \
            i_dual_diagram

    def get_package_by_guid(
            self,
            package_ea_guid: str) \
            -> IPackage:
        package = \
            self.repository.GetPackageByGuid(
                package_ea_guid)

        if not package:
            return \
                INullPackage()

        i_dual_package = \
            IDualPackage(
                package=package)

        return \
            i_dual_package

    def get_package_by_id(
            self,
            package_id: int) \
            -> IPackage:
        package = \
            self.repository.GetPackageByID(
                package_id)

        if not package:
            return \
                INullPackage()

        i_dual_package = \
            IDualPackage(
                package=package)

        return \
            i_dual_package

    def exit(
            self):
        self.repository.Exit()

    def get_project_interface(
            self) \
            -> IProject:
        project = \
            self.repository.GetProjectInterface()

        if not project:
            return \
                INullProject()

        i_dual_project = \
            IDualProject(
                project=project)

        return \
            i_dual_project

    def refresh_model_view(
            self,
            package_id: int):
        self.repository.RefreshModelView(
            package_id)

    def sql_query(
            self,
            sql: str) \
            -> str:
        xml_string = \
            self.repository.SQLQuery(
                sql)

        return \
            xml_string

    def __get_batch_append(
            self) \
            -> bool:
        batch_append = \
            self.repository.BatchAppend

        return \
            batch_append

    def __set_batch_append(
            self,
            batch_append: bool):
        self.repository.BatchAppend = \
            batch_append

    def __get_enable_ui_updates(
            self) \
            -> bool:
        enable_ui_updates = \
            self.repository.EnableUIUpdates

        return \
            enable_ui_updates

    def __set_enable_ui_updates(
            self,
            enable_ui_updates: bool):
        self.repository.EnableUIUpdates = \
            enable_ui_updates

    def __get_instance_guid(
            self) \
            -> str:
        instance_guid = \
            self.repository.InstanceGUID

        return \
            instance_guid

    def __get_connection_string(
            self) \
            -> str:
        connection_string = \
            self.repository.ConnectionString

        return \
            connection_string

    def __get_library_version(
            self) \
            -> int:
        library_version = \
            self.repository.LibraryVersion

        return \
            library_version

    def __get_models(
            self) \
            -> IDualPackageCollection:
        models = \
            IDualPackageCollection(
                ea_collection=self.repository.Models)

        return \
            models

    def __get_stereotypes(
            self) \
            -> IDualStereotypeCollection:
        stereotypes = \
            IDualStereotypeCollection(
                ea_collection=self.repository.Stereotypes)

        return \
            stereotypes

    batch_append = \
        property(
            fget=__get_batch_append,
            fset=__set_batch_append)

    connection_string = \
        property(
            fget=__get_connection_string)

    enable_ui_updates = \
        property(
            fget=__get_enable_ui_updates,
            fset=__set_enable_ui_updates)

    instance_guid = \
        property(
            fget=__get_instance_guid)

    library_version = \
        property(
            fget=__get_library_version)

    models = \
        property(
            fget=__get_models)

    stereotypes = \
        property(
            fget=__get_stereotypes)
