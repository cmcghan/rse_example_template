# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/AS4SR/rse_example_template
# Additional copyright may be held by others, as reflected in the commit history.

# reference files used:
# https://raw.githubusercontent.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
# https://raw.githubusercontent.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
# License for ref. files: BSD 3-clause, Copyright (c) 2008, Willow Garage, Inc., All rights reserved.

#
# code below is new code, using the upper two codesets as a function-reference only
#

import rospy
from std_msgs.msg import String
import sys

def default_callback(data):
    # *** WIP ***

class RosPubSubClass(object):

    def __init__(self,typestr,publistodict=None,sublistodict=None):
        """
        classtype = 0 (not set), 1 (pub), 2 (sub), 3 (pubsub)
                    "3" in this context means "mixed" / both occur, but this is not recommended!
        publistodict format is list of dictionaries = 
                           [{ topicname: string_as_name_of_topic ,
                              datatype: ros_imported_datatype ,
                              queue_size: int_queue_size (default=0) ,
                              rate: int_Rate (default=10 (Hertz))
                            }, ...]
        sublistodict format is list of dictionaries = 
                           [{ topicname: string_as_name_of_topic ,
                              datatype: ros_imported_datatype ,
                              callbackfn: function_callback (default=default_callback())
                            }, ...]
        """
        #
        # checking and copying over inputs
        #
        
        # make sure you have a class "type" for this before proceeding
        self.classtype = 0
        dictflag = 0
        if (typestr == "pub"):
            self.typestr = typestr
            self.classtype = 1
            # make sure you have actual channel info (topics) before proceeding
            if (publistodict is not None): # pub       
                self.publistodict = publistodict
            else:
                dictflag = 1
        elif (typestr == "sub"):
            self.typestr = typestr
            self.classtype = 2
            # make sure you have actual channel info (topics) before proceeding
            if (sublistodict is not None): # pub       
                self.sublistodict = sublistodict
            else:
                dictflag = 1
        elif (typestr == "pubsub"):
            self.typestr = typestr
            self.classtype = 3
            # make sure you have actual channel info (topics) before proceeding
            if (publistodict is not None): # pub       
                self.publistodict = publistodict
            else:
                dictflag = 1
            if (sublistodict is not None): # pub       
                self.sublistodict = sublistodict
            else:
                dictflag = 1
        else:
            print("Error: RosPubSubClass not given typestr")
            print("acceptable options are: 'pub', 'sub', 'pubsub'")
            sys.exit(1)
        
        # error message corresponding to "actual channel info (topics)" checks above:
        if (dictflag == 1): # and (self.classtype < 1) <-- should be >=1 if got this far
            print("Error: RosPubSubClass not given pubdict and/or subdict")
            print("You must give at least one dictionary of information,")
            print("in the proper format, and corresponding to the typestr selected.")
            sys.exit(1)
        
        #
        # setting up channels / topics for messaging
        #
        
        # dealing with setting up publisher channels:
        pubtopicsdict = {}
        pubtopicsnames = [] # dictionaries don't have order, need
                            # list of lists for linking/correspondence
        for i in range(self.pubdict):
            topicname = self.publistodict[i].topicname
            datatype = self.publistodict[i].datatype
            queue_size = self.publistodict[i].queue_size
            if queue_size is None:
                queue_size = 0
            rate = self.publistodict[i].rate
            if rate is None:
                rate = 10
            holdtopic = rospy.Publisher(topicname, datatype, queue_size, rate)
            #pubtopicsdict.update({topicname: holdtopic})
            pubtopicslist.append([topicname, holdtopic])
        
        # dealing with setting up subscription channels:
        #subtopicsdict = {}
        subtopicslist = [] # dictionaries don't have order, need
                           # list of lists for linking/correspondence
        for i in range(self.sublistodict):
            topicname = self.sublistodict[i].topicname
            datatype = self.sublistodict[i].datatype
            callbackfn = self.sublistodict[i].callbackfn
            if callbackfn is None:
                callbackfn = default_callback
            # class that can be pinged for data via .receive() or .receive_and_clear()
            holdtopic = RosSingleSubClass(topicname, datatype, callbackfn)
            #subtopicsdict.update({topicname: holdtopic})
            subtopicslist.append([topicname, holdtopic])


    def send(data): # single-send vs. multisend
        
        pub = 
        # *** WIP ***
        pub.publish(data)
    



    #def callback(data):
    #    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

    #def listener(): # subscribe call
    #    rospy.Subscriber('chatter', String, callback)
    #    # spin() simply keeps python from exiting until this node is stopped
    #    rospy.spin()




class RosSingleSubClass(object):

    def __init__(self,topicname,datatype,callbackfn):
        """
        topicname: string_as_name_of_topic ,
        datatype: ros_imported_datatype ,
        callbackfn: function_callback (default=default_callback())
        """
        
        from multiprocessing import Lock # .acquire(block={true,false},timeout={None,int})
        self.thelock = Lock()
        
        #
        # setting up channel / topic for messaging
        #
        self.topicname = topicname
        self.datatype = datatype
        self.callbackfn_local = callbackfn
        if callbackfn is None:
            self.callbackfn_local = default_callback
        holdtopic = rospy.Subscriber(topicname, datatype, self.toplevelcallbackfn)
        return holdtopic

    def toplevelcallbackfn(data):
        # use mutex stuff -- lock, save data, unlock -- this will overwrite anything
        self.thelock.acquire(True)
        self.returneddata = self.callbackfn_local(data)
        self.thelock.release()
        return

    def received():
        self.thelock.acquire(True)
        thedata = self.returneddata
        #self.returneddata = None # not clearing data that was received
                                  # only know if received new data if value changes
        self.thelock.release()
        return thedata
        
    def received_and_clearreceived():
        self.thelock.acquire(True)
        thedata = self.returneddata
        self.returneddata = None # cleared data that was stored locally,
                                 # know if received new data if not "None"
        self.thelock.release()
        return thedata


if __name__ == '__main__':
    
    
    
    try:
        rospy.init_node('talker', anonymous=True)
        talker()
    except rospy.ROSInterruptException:
        pass
    # -versus-
    rospy.init_node('listener', anonymous=True)
    listener()

    sys.exit(0)

# -- eof --
