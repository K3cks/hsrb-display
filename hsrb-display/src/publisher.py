#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImagePublisher:

    def __init__(self, topic="/head_display/reveiver"):
        self.bridge = CvBridge()

        # Create a publisher for the image
        self.publisher = rospy.Publisher(topic, Image, queue_size=10)
        print("publisher started")

    def publish_image(self, path):
        image = cv2.imread(path)

        print(image)

        if image is not None:
            # Convert the OpenCV image to a ROS image message
            ros_image = self.bridge.cv2_to_imgmsg(image, "bgr8")

            # Publish the ROS image message
            rospy.sleep(1)
            self.publisher.publish(ros_image)
            print("published image")
        else:
            rospy.logerr("Failed to load image: %s", path)
