from natlparks import NatlParks
from api import api
parks = NatlParks(api)

test = parks.parks()

print(test)