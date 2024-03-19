import rospy

from src.subscriber import ImageSubscriber

sub = ImageSubscriber()
print("Subscribed to head display visualizer")
rospy.spin()
