from redis import asyncio as aioredis
import logging

logger = logging.getLogger(__name__)


class PhoneAddressRepository:
    def __init__(self, url: str):
        logger.info(f"call params: url={url}")
        self.redis_db = aioredis.from_url(url, db=1)

    async def get(self, key: str) -> bytes:
        """
        Get value from redis by key.
        :param key: key
        :type key: str
        :return: value
        :rtype: bytes
        """
        logger.info(f"call params: key={key}")
        return await self.redis_db.get(key)

    async def add(self, key: str, value: str):
        """
        Set key value in redis.
        :param key: key
        :type key: str
        :param value: value
        :type value: str
        :return: None
        :rtype: None
        """
        logger.info(f"call params: key={key}, value={value}")
        await self.redis_db.set(key, value)
