from pydantic import BaseModel, constr


class Phone(BaseModel):
    phone: constr(pattern=r"^\d{11,11}$")


class Address(BaseModel):
    address: constr(max_length=256)


class Data(Phone, Address):
    ...
