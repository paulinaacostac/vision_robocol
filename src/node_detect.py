#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import String

### NODO PRINCIPAL ###
def node_main():
    # Creacion del nodo
    rospy.init_node('node_detect',anonymous=True)
    # Subscrirse al topico ...
    rospy.Subscriber ('topic_name',String, callback)
    # Publica en el tópico ...
    pub = rospy.Publisher('topic_name',String,queue_size=10)
    # Crea el servicio ...
    #service = rospy.Service('service_name',service_type_msg,handle)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep ()

def callback(param):
    pass

def handle(param):
    pass

if __name__ == '__main__':
    try:
        node_main()
    except rospy.ROSInterruptException:
        pass