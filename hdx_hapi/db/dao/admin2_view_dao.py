from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_admin2_view import Admin2View
from hdx_hapi.db.dao.util.util import apply_pagination

from datetime import datetime

async def admin2_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    is_unspecified: bool = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):

    query = select(Admin2View)
    if code:
        query = query.where(Admin2View.code == code)
    if name:
        query = query.where(Admin2View.name.icontains(name))
    if is_unspecified:
        query = query.where(Admin2View.is_unspecified == is_unspecified)
    if reference_period_start:
        query = query.where(Admin2View.reference_period_start >= reference_period_start)
    if reference_period_end:
        query = query.where(Admin2View.reference_period_end <= reference_period_end)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    locations = result.scalars().all()
    return locations