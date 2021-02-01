from pydantic import BaseModel

class Job(BaseModel):
    jobtitle = ''
    jobdescription =''
    hourlypay = ''
    proposals = ''
    country = ''