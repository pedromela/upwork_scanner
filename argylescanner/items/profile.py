"""
Profile module
"""
from items.base_item import BaseItem

NOT_AVAILABLE = 'Not Available'

class Profile(BaseItem):
    """
    Profile class
    """
    id = NOT_AVAILABLE
    account = NOT_AVAILABLE
    employer = NOT_AVAILABLE
    created_at = NOT_AVAILABLE
    updated_at = NOT_AVAILABLE
    first_name = NOT_AVAILABLE
    last_name = NOT_AVAILABLE
    full_name = NOT_AVAILABLE
    email = NOT_AVAILABLE
    picture_url = NOT_AVAILABLE
    phone_number = NOT_AVAILABLE
    address = {
            'line1' : NOT_AVAILABLE,
            'line2' : NOT_AVAILABLE,
            'city' : NOT_AVAILABLE,
            'state': NOT_AVAILABLE,
            'postal_code' : NOT_AVAILABLE,
            'country' : NOT_AVAILABLE
        }
    employment_status = NOT_AVAILABLE
    employment_type = NOT_AVAILABLE
    job_title = NOT_AVAILABLE
    ssn = NOT_AVAILABLE
    platform_user_id = NOT_AVAILABLE
    hire_dates = [NOT_AVAILABLE]
    terminations = [{NOT_AVAILABLE}]
    marital_status = NOT_AVAILABLE

    def serialize(self):
        """
        serialize object and store in pickle file
        """
        super().serialize(self.full_name)
