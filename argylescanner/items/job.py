"""
Job module
"""
from items.base_item import BaseItem

NOT_AVAILABLE = 'Not Available'

class Job(BaseItem):
    """
    Job class
    """
    jobtitle = NOT_AVAILABLE
    jobdescription = NOT_AVAILABLE
    hourlypay = NOT_AVAILABLE
    proposals = NOT_AVAILABLE
    country = NOT_AVAILABLE

    def serialize(self):
        """
        serialize object and store in pickle file
        """
        super().serialize(self.jobtitle)
