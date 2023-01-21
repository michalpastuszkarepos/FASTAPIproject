from typing import Optional

from pydantic import BaseModel


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    # phone_number: int
    # street: str
    # city: str
    # post_code: int


class CustomerUpdateData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    # phone_number: int
    # street: str
    # city: str
    # post_code: int

