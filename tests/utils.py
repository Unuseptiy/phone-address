from .conftest import fake


def get_phone_number() -> str:
    return fake.country_calling_code() + fake.msisdn()[3:]
