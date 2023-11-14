from .conftest import fake
from .utils import get_phone_number
from app.core.repositories import PhoneAddressRepository
from app.core import service


async def test_create_data(get_phone_address_db_config):
    """
    Test create data in redis.
    """
    phone = get_phone_number()
    address = fake.address()
    p_a_repo = PhoneAddressRepository(*get_phone_address_db_config)
    await service.create_update_data(phone, address, p_a_repo)

    address_from_redis = await p_a_repo.redis_db.get(phone)

    assert address_from_redis.decode() == address

    await p_a_repo.redis_db.delete(phone)


async def test_update_data(get_phone_address_db_config):
    """
    Test update db data.
    """

    phone = get_phone_number()
    address = fake.address()
    p_a_repo = PhoneAddressRepository(*get_phone_address_db_config)

    await service.create_update_data(phone, address, p_a_repo)

    new_address = fake.address()
    await service.create_update_data(phone, new_address, p_a_repo)

    address_from_redis = await p_a_repo.redis_db.get(phone)

    assert address_from_redis.decode() == new_address

    await p_a_repo.redis_db.delete(phone)


async def test_get_data(get_phone_address_db_config):
    """
    Test get data from redis.
    """
    phone = get_phone_number()
    address = fake.address()
    p_a_repo = PhoneAddressRepository(*get_phone_address_db_config)
    await p_a_repo.redis_db.set(phone, address)

    address_from_redis = await service.get_data(phone, p_a_repo)

    assert address_from_redis.decode() == address

    await p_a_repo.redis_db.delete(phone)
