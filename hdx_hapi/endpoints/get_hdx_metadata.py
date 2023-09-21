from datetime import datetime, date
from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.dataset_view import DatasetViewPydantic
from hdx_hapi.endpoints.models.resource_view import ResourceViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.dataset_logic import get_datasets_srv
from hdx_hapi.services.resource_logic import get_resources_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['hdx-metadata'],
)


@router.get('/api/dataset', response_model=List[DatasetViewPydantic])
async def get_datasets(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    hdx_id: Annotated[str, Query(max_length=36, description='HDX Dataset ID')] = None,
    hdx_stub: Annotated[str, Query(max_length=128, description='HDX Dataset name')] = None,
    title: Annotated[str, Query(max_length=128, description='HDX Dataset title or display name')] = None,
    provider_code: Annotated[str, Query(max_length=10, description='Dataset ID given by provider')] = None,
    provider_name: Annotated[str, Query(max_length=128, description='Dataset name given by provider')] = None,
):
    """
    Return the list of datasets
    """
    result = await get_datasets_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        hdx_id=hdx_id,
        hdx_stub=hdx_stub,
        title=title,
        provider_code=provider_code,
        provider_name=provider_name,
    )
    return result


@router.get('/api/resource', response_model=List[ResourceViewPydantic])
async def get_resources(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    hdx_id: Annotated[str, Query(max_length=36, description='HDX Resource ID')] = None,
    format: Annotated[str, Query(max_length=10, description='HDX Resource format')] = None,
    is_hxl: Annotated[bool, Query(description='Is Resource HXL')] = None,
    dataset_hdx_id: Annotated[str, Query(max_length=128, description='HDX Dataset ID')] = None,
    dataset_hdx_stub: Annotated[str, Query(max_length=128, description='HDX Dataset name')] = None,
    dataset_title: Annotated[str, Query(max_length=10, description='HDX Dataset title')] = None,
    dataset_provider_code: Annotated[str, Query(max_length=10, description='Dataset ID given by provider')] = None,
    dataset_provider_name: Annotated[str, Query(max_length=10, description='Dataset name given by provider')] = None,
):
    """
    Return the list of datasets
    """
    result = await get_resources_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        hdx_id=hdx_id,
        format=format,
        is_hxl=is_hxl,
        dataset_hdx_id=dataset_hdx_id,
        dataset_hdx_stub=dataset_hdx_stub,
        dataset_title=dataset_title,
        dataset_provider_code=dataset_provider_code,
        dataset_provider_name=dataset_provider_name,
    )
    return result