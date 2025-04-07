from fastapi import HTTPException, status

from src.api.v1.router import router
from src.schemas import Contact


contacts_db = {}


@router.post(
    '/contact',
    response_model=Contact,
    status_code=status.HTTP_201_CREATED,
)
def create_contact(contact: Contact):
    if contact.id in contacts_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Contact with same id already exists',
        )
    contacts_db[contact.id] = contact
    return contact


@router.get(
    '/contact/{contact_id}',
    response_model=Contact,
)
def read_contact(contact_id: int):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return contacts_db[contact_id]


@router.put(
    '/contact/{contact_id}',
    response_model=Contact,
)
def update_contact(contact_id: int, group: Contact):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    contacts_db[contact_id] = group
    return group


@router.delete(
    '/contact/{contact_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_contact(contact_id: int):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    del contacts_db[contact_id]
    return None
