from fastapi import APIRouter, Query, HTTPException, status, Response

from app.api.v1 import schemas as sch
from app.core.repositories import PhoneAddressRepository
from app.core import service
from app.core import exceptions as exc
from app.core.config import get_config

router = APIRouter(prefix="/data")


config = get_config()


@router.get("", response_model=sch.Address)
async def check_data(phone: str = Query(..., pattern=r"^\d{11,11}$")):
    """
        Get data by phone.

        - params:
            - phone: phone

        - return:
            - Address
        """
    phone_address_repository = PhoneAddressRepository(config.redis_url, config.phone_address_db)
    try:
        address_b = await service.get_data(phone, phone_address_repository)
    except exc.NoEntityError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"The address by the phone {phone} not found."
        )
    return sch.Address(address=address_b)


@router.post("", status_code=status.HTTP_204_NO_CONTENT)
async def create_update_data(data: sch.Data):
    """
    Create or update data.
    - params:
        - phone: phone
        - address: address

    -return:
        - None
    """
    phone_address_repository = PhoneAddressRepository(config.redis_url, config.phone_address_db)
    await service.create_update_data(data.phone, data.address, phone_address_repository)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
