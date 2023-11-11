from redis import asyncio as aioredis


class PhoneAddressRepository:
    def __init__(self, url: str, db: int):
        self.redis_db = aioredis.from_url(url, db=db)

    async def get(self, key: str) -> bytes:
        """
        Get value from redis by key.
        :param key: key
        :type key: str
        :return: value
        :rtype: bytes
        """
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
        await self.redis_db.set(key, value)
