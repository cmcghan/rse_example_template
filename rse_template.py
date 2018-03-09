# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/AS4SR/rse_example_template
# Additional copyright may be held by others, as reflected in the commit history.

class RSE_basics(object):


    def __init__(self):
        
        
        
        self.comms_initialization()
        
        return
        
    def comms_initialization(self): # separating this out b/c comms is a beast unto itself
        
        
        
        return
        
    def state_machine(self): # "main block" of the class, handles wahat-is-done-when
        # basically, everything you're doing here is "a way" to encode
        # and then enact an action policy (there are several ways to do this :)
        
        #
        # the "stupid, can't-stop-in-the-middle" way
        #
        #while (1):
            #holdarb = self.arbitration.check()
            #if holdarbi == ...:
                
            #elif holdarbi == ...:
                
            #else:
                
            #holdtact = self.tactics.check()
            #if holdtact == ...
                
            #elif holdtact == ...:
                
            #else:
                
            #holdctrl = self.control.check()
            #if holdctrl == ...
                
            #elif holdctrl == ...:
                
            #else:
                
            #holdactv = self.activity_manager.check()
            #if holdactv == ...
                
            #elif holdactv == ...:
                
            #else:
           
        #
        # the less-stupid way to do it -- more "state-machine-like"
        #
        state = "start"
        while (1):
            # "interrupt-level state machine" part
            # ... comms polling from arbitration side to see if new
            # commands or interrupt commands came in
            # if a new "interrupt" command came in (e.g., cancel" or similar),
            # then a priority flag gets set as a part of the states looked at below
            
            # "state machine" part
            if state == "start":
                state = "arbitration-1"
                runpiece = "arbitration"
            elif state == "arbitration-1": # step 1 or arbitration process
            #alt.: "arb1_ctl0_tac0_act0" as "just started, nothing else running/active"
            #      or [1, 0, 0, 0] , or arbflag=arbstatus=1 ...
                # checking status of arbitration process if non-blocking
                # (parallel, not going to run this until completes, vs.
                #  blocking / serial, runs until complete and only then returns)
                holdcheck = self.arbitration.check()
                if holdcheck == ???: #in-progress
                    ???
                elif holdcheck == ???: # completed
                    ???

                    if holdvalue == ???:
                        state = ???
                    elif holdvalue == ???:
                        state = ???
                    else:
                        state = ???

                else: # nothing / hasn't started yet / not currently computing(?)
                    ???
                    
            elif state == ???:
                if holdvalue == ???:
                    state = ???
                elif holdvalue == ???:
                    state = ???
                else:
                    state = ???
            ...
            
            # "actually run things that need to be run" part
            #if state == "arbitration-1":
            if runpiece == "arbitration":
                holdvalue = self.arbitration.run()
                
            elif holdactv == ...:
                
            else:
                
            #
            # alternative #3 -- "action policy"-like / "activity diagram"-like
            # for this one, it's easier to follow the flow of what's going on,
            # and there is no "required" breakdown of all "sub"states of each node
            # that you may not want to interrupt (so, no "artificial",
            # "externally-imposed by the code strcture" stops)
            # 
            # for this, the actions are the "state" and the "state" is the transition
            # that determines the next action that needs to be done
            # (so, basically backwards from a state machine's usual instantiation)
            #
            
            
            
        state = "start"
        
        return
        
    def arbitration(self):
        
        
        
        
        
    def control(self):
        
        
        
        
        
    def tactics(self):
        
        
        
        
        
    def activity_manager(self):
        
        
        
        
        


if __name__ == '__main__':
       
    rse_node = RSE_basics()
    try:
        rospy.init_node('rse_node_1', anonymous=True)
        RSE_basics.start_state_machine()
    except rospy.ROSInterruptException:
        pass

    sys.exit(0)

# -- eof --
