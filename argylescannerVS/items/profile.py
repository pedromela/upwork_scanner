from pydantic import BaseModel

class Profile(BaseModel):
    first_name = ''
    last_name = ''
    full_name = ''
    email = ''
    picture_url = ''
    phone_number = ''
    line1 = ''
    line2 = ''
    city = ''
    state = ''
    postal_code = '' 
    country = ''