import os
import items.profile
from items.base_item import BaseItem
from items.job import Job
from items.profile import Profile


for file_name in os.listdir("./pickles"):
    file = open("./pickles/" + file_name, 'rb')
    item = items.base_item.deserialize(file)
    print(item)
