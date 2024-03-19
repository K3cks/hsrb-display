import os
import time
from pathlib import Path

import rospy

from src.publisher import ImagePublisher
from src.subscriber import ImageSubscriber

sub = ImageSubscriber()
print("Subscribed to head display visualizer")
rospy.spin()
