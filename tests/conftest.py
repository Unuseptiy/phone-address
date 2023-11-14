import pytest
from asyncio import new_event_loop, set_event_loop

from faker import Faker


from app.core.config import get_config


fake = Faker()


@pytest.fixture(scope="session")
def event_loop():
    loop = new_event_loop()
    set_event_loop(loop)

    yield loop
    loop.close()


@pytest.fixture
async def get_phone_address_db_config():
    config = get_config()
    yield config.redis_url, config.phone_address_db
