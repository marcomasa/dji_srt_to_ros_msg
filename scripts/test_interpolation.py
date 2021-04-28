# Python test file

import numpy as np
from scipy import interpolate

#def interpolate_values(raw_data, steps):
    #interpolated_data = []
    #for index, elem in enumerate(raw_data):
        #interpolated_data.append(elem)
        #if( (index+1) < len(raw_data) ):
        #    interpolated_vals = np.interp(elem, raw_data[index+1], steps)
        #    for iv in interpolated_vals:
        #        interpolated_data.append(interpolated_vals)

    #return interpolated_data



test_array = [0, 1, 2]
steps_list = list(range(0, 29))

#result = interpolate_values(test_array, steps)

result = sp.interpolate.interp1d(test_array, )

for index, elem in result:
    print('elem' + (index+1) + '=' + elem)
                

