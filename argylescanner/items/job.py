"""
Job module
"""
from pydantic import BaseModel

NOT_AVAILABLE = 'Not Available'

class Job(BaseModel):
    """
    Job class
    """
    jobtitle = NOT_AVAILABLE
    jobdescription = NOT_AVAILABLE
    hourlypay = NOT_AVAILABLE
    proposals = NOT_AVAILABLE
    country = NOT_AVAILABLE
