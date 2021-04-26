# Python test file

import rospy
from sensor_msgs.msg import NavSatFix

# every 4th line the pattern repeats
# pattern is:
# 1. sequence
# 2. time window
# 3. telemetry data
i_seq, i_timewindow, i_telemetry = 1, 2, 3

i_gps_vals = 4

class GPS_RAW:
    sequence_id = None
    latitude = None
    longitude = None
    altitude = None
    distance = None
    height = None

    def print_this(self):
        print('GPS_RAW(' + self.sequence_id +
              ' | lat=' + self.latitude + 
              ' | long=' + self.longitude + 
              ' | alt=' + self.altitude + 
              ' | dist=' + self.distance + 
              ' | height=' + self.height + ')')

all_gps_data = []

### STEP 1: Read the whole file and save the values

# open the provided file
with open("/media/marco/Shared Memory/Documents/UNI/Promotion/Videos_Park_Waste/DJI_0115.srt",'r') as reader:
    
    # use the helper to recognize the pattern / line type
    array_access_index = 1
    tmp_gps_data = GPS_RAW()

    # read line by line
    for line in reader:
        cur_index = array_access_index % 4
        
        # sequence
        if(cur_index == i_seq):
            tmp_gps_data.sequence_id = line.rstrip('\n')

        # time frame    
        elif(cur_index == i_timewindow):
            None

        # telemetry data
        elif(cur_index == i_telemetry):
            
            # seperate the line elements by commas
            currentline = line.split(',')

            # these are the gps vals, some need more string separation
            tmp_gps_data.latitude = currentline[4].split('(')[1]
            tmp_gps_data.longitude = currentline[5]
            tmp_gps_data.altitude = currentline[6].split(')')[0]
            tmp_gps_data.distance = currentline[7].split('D')[1].split('m')[0]
            tmp_gps_data.height = currentline[8].split('H')[1].split('m')[0]

            # optionally print this
            tmp_gps_data.print_this()

            # we can save the local gps data into the array
            all_gps_data.append(tmp_gps_data)
            tmp_gps_data = GPS_RAW()

        # every fourth line is empty
        else:
            None
    
        # increase the index
        array_access_index += 1

### STEP 2: Create ROS Messages with correct timestamps




