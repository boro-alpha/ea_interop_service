import win32com.client

from ea_interop_service_source.b_code.i_dual_objects.i_dual_repository import IDualRepository
from ea_interop_service_source.b_code.i_dual_objects.i_null_repository import INullRepository
from ea_interop_service_source.b_code.return_results.i_dual_repository_creation_result_types import \
    IDualRepositoryCreationResultTypes
from ea_interop_service_source.b_code.return_results.i_dual_repository_creation_results import \
    IDualRepositoryCreationResults


def get_i_dual_repository_creation_result(
        ea_project_filename: str) \
        -> IDualRepositoryCreationResults:
    i_dual_repository_creation_result = \
        __get_i_dual_repository_creation_result(
            ea_project_filename=ea_project_filename)

    return \
        i_dual_repository_creation_result


def __get_i_dual_repository_creation_result(
        ea_project_filename: str) \
        -> IDualRepositoryCreationResults:
    com_object_repository = \
        __initialise_com_object_repository()

    if com_object_repository is None:
        return \
            IDualRepositoryCreationResults(
                i_dual_repository=INullRepository(),
                i_dual_repository_creation_result_type=IDualRepositoryCreationResultTypes.FAILED_TO_OPEN_EA)

    com_object_repository = \
        __load_com_object_repository(
            com_object_repository=com_object_repository,
            ea_project_filename=ea_project_filename)

    if com_object_repository is None:
        return \
            IDualRepositoryCreationResults(
                i_dual_repository=INullRepository(),
                i_dual_repository_creation_result_type=IDualRepositoryCreationResultTypes.FAILED_TO_OPEN_EA_PROJECT)

    i_dual_repository_creation_result = \
        __get_successful_i_dual_repository_creation_result(
            com_object_repository=com_object_repository)

    return \
        i_dual_repository_creation_result


def __initialise_com_object_repository():
    try:
        initial_com_object_repository = \
            win32com.client.Dispatch(
                'EA.Repository')

    except Exception:
        initial_com_object_repository = \
            None

    return \
        initial_com_object_repository


def __load_com_object_repository(
        com_object_repository,
        ea_project_filename: str):
    try:
        com_object_repository.OpenFile2(
            ea_project_filename,
            1,
            0)

    except Exception:
        com_object_repository = \
            None

    return \
        com_object_repository


def __get_successful_i_dual_repository_creation_result(
        com_object_repository) \
        -> IDualRepositoryCreationResults:
    i_dual_repository = \
        IDualRepository(
            repository=com_object_repository)

    i_dual_repository_creation_result = \
        IDualRepositoryCreationResults(
            i_dual_repository=i_dual_repository,
            i_dual_repository_creation_result_type=IDualRepositoryCreationResultTypes.SUCCEEDED)

    return \
        i_dual_repository_creation_result
