import os
import time
from pathlib import Path

import rospy

from src.publisher import ImagePublisher
from src.subscriber import ImageSubscriber


def change_image(path):
    pub.publish_image(path)
    rospy.sleep(2)


if __name__ == '__main__':
    rospy.init_node('image_handling', anonymous=True)
    picture_directory = str(Path.home()) + '/workspaces/Work/playground/test_images/'
    default_picture = os.path.join(picture_directory, 'default_logo.png')
    doing_picture = os.path.join(picture_directory, 'detecting.png')

    # Ensure subscriber started on hsrb
    # sub = ImageSubscriber()
    # time.sleep(3)

    pub = ImagePublisher()
    pub.publish_image(default_picture)

    time.sleep(3)

    pub.publish_image(doing_picture)

    time.sleep(3)

    pub.publish_image(default_picture)

    print("done")
