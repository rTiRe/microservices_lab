from fastapi import HTTPException, status

from src.api.v1.router import router
from src.schemas import Group


groups_db = {}


@router.post(
    '/group',
    response_model=Group,
    status_code=status.HTTP_201_CREATED,
)
def create_group(group: Group):
    if group.id in groups_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Group with same id already exists',
        )
    groups_db[group.id] = group
    return group


@router.get(
    '/group/{group_id}',
    response_model=Group,
)
def read_group(group_id: int):
    if group_id not in groups_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return groups_db[group_id]


@router.put(
    '/group/{group_id}',
    response_model=Group,
)
def update_group(group_id: int, group: Group):
    if group_id not in groups_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    groups_db[group_id] = group
    return group


@router.delete(
    '/group/{group_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_group(group_id: int):
    if group_id not in groups_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    del groups_db[group_id]
    return None
