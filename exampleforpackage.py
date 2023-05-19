import examplepackagedirectory.example1
examplepackagedirectory.example1.calc_shipping()
# above is one way of importing it is legthy so we use second method
from examplepackagedirectory.example1 import calc_shipping
calc_shipping()

# another way

from examplepackagedirectory import example1
example1.calc_shipping()
