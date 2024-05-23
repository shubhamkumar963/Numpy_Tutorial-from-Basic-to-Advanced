#5 ways to rounding of decimals: truncation(), fix(),rounding(),floor(),ceil()

#return value of trunc() will be a float value

import numpy as np
x= np.trunc([-5.4551,9.999])
print(x)

#rounding - using around() function

import numpy as np
x= np.around([-5.5551,9.999])
print(x)

#rounding - using floor() function-round off to lower integer

import numpy as np
x= np.floor([-5.5551,9.999])
print(x)

#ceil(): round off decimal to upper integer
import numpy as np
x= np.ceil([-5.5551,9.999])
print(x)
