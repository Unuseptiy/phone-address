import logging

from app.core.repositories import PhoneAddressRepository
from app.core import exceptions as exc


logger = logging.getLogger(__name__)


async def create_update_data(
        phone: str,
        address: str,
        phone_address_repository: PhoneAddressRepository,
) -> None:
    """
    Create or update data.

    :param phone: phone
    :type phone: str
    :param address: address
    :type address: str
    :param phone_address_repository: phone address repository
    :type phone_address_repository: PhoneAddressRepository
    :return: None
    :rtype: Coroutine[None, None, None]
    """
    logger.info(f"call params: phone={phone} address={address}")
    await phone_address_repository.add(phone, address)


async def get_data(
        phone: str,
        phone_address_repository: PhoneAddressRepository,
) -> bytes:
    """
    Get data by phone.

    :param phone: phone
    :type phone: str
    :param phone_address_repository: phone address repository
    :type phone_address_repository: PhoneAddressRepository
    :return: corresponding address
    :rtype: Coroutine[None, None, bytes]
    """
    logger.info(f"call params: phone={phone}")
    address = await phone_address_repository.get(phone)
    if address:
        logger.info(f"return: address={address}")
        return address
    logger.info("error: NoEntityError")
    raise exc.NoEntityError(f"There is no entity with phone {phone}")
