# dji_srt_to_ros_msg
This package contains python scripts to convert the telemetry of a DJI Drone (e.g. Mavic Mini) to ROS messages that may be used for robotic applications.
As the telemetry belongs to a video file and is pre-recorded, it is advised to record a bagfile of the messages for multiple use.

## Pre-requisites

1.  You will need to enable the telemetry recording in your DJI Fly App.
    Please refer to https://djitelemetryoverlay.com/ for instructions.

2. Fly and record a video.

3. Use the [subtitle extractor](https://djitelemetryoverlay.com/subtitle-extractor/#) to get the raw text file containing the telemetry information.
   You should have a file called NAME_OF_YOUR_VIDEO.srt now.

## Video conversion

You can use the [movie publisher](https://github.com/peci1/movie_publisher) package to convert the video stream to a ROS message.

### Dependencies

Install the [rosbash_params](https://github.com/peci1/rosbash_params) package

``` sudo apt install ros-melodic-rosbash-params ```

Also, install the dependencies required from the movie publisher package 

``` sudo apt install ffmjpeg ```

(please refer to [movie publisher](https://github.com/peci1/movie_publisher) for specific dependencies)

### Necessary Adjustments

In line 313 of the [movie_publisher_node](https://github.com/peci1/movie_publisher/blob/indigo-devel/nodes/movie_publisher_node) the image encoding needs to be changed from "bgr8" to "rgb8" to work correctly (atleast for Mavic Mini .mp4 videos):

``` msg = self.bridge.cv2_to_imgmsg(frame, "bgr8") ```

Change to:

``` msg = self.bridge.cv2_to_imgmsg(frame, "rgb8") ```

