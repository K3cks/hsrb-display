#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImageSubscriber:
    def __init__(self, topic="/head_display/reveiver"):
        self.image = None

        self.subscriber = rospy.Subscriber(topic, Image, self.image_callback)

        self.bridge = CvBridge()

        print("subscriber started")

    def image_callback(self, msg):

        try:
            image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

            if image is not None:
                self._display_image(image)

        except Exception as e:
            rospy.logerr("Error processing image: %s", e)

    def _display_image(self, image):
        # cv2.CAP_IMAGES: Fixed frame. Rescale images to frame
        # cv2.WINDOW_GUI_NORMAL: Fixed frame. Fixed image
        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

        desired_width = 800  # Example width
        desired_height = 600  # Example height
        cv2.resizeWindow("Image", desired_width, desired_height)

        cv2.imshow("Image", image)
        cv2.waitKey(50)  # Display image for 1 second
        print("changed image")



