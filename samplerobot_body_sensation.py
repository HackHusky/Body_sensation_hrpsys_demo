#!/usr/bin/env python

try:
    from hrpsys.hrpsys_config import *
    import OpenHRP
except:
    print "import without hrpsys"
    import rtm
    from rtm import *
    from OpenHRP import *
    import waitInput
    from waitInput import *
    import socket
    import time

def init ():
    global hcf,orientation_sensor,force_sensor,initial_pose, hrpsys_version
    hcf = HrpsysConfigurator()
    hcf.getRTCList = hcf.getRTCListUnstable
    hcf.init ("SampleRobot(Robot)0", "$(PROJECT_DIR)/../model/sample1.wrl")
    hcf.connectLoggerPort(hcf.kf, 'baseRpyCurrent')
    # initialize poses
    initial_pose = [-7.779e-005,  -0.378613,  -0.000209793,  0.832038,  -0.452564,  0.000244781,  0.31129,  -0.159481,  -0.115399,  -0.636277,  0,  0,  0,  -7.77902e-005,  -0.378613,  -0.000209794,  0.832038,  -0.452564,  0.000244781,  0.31129,  0.159481,  0.115399,  -0.636277,  0,  0,  0,  0,  0,  0]
    # simulate value for gyroscope/acclerometer when standing
    orientation_sensor = [0,90,0];
    # simulate value for force sensor 0 = no force, 1 = force applied
    force_sensor = 0;
    #write initial pose
    hcf.seq_svc.setJointAngles(initial_pose, 1)
    hcf.seq_svc.waitInterpolation()
    hrpsys_version = hcf.seq.ref.get_component_profile().version
    print("hrpsys_version = %s"%hrpsys_version)

def test_walk ():
    hcf.abc_svc.goPos(.6,0,0)
    hcf.abc_svc.waitFootSteps()


def fall():
    #simulate the robot falling forward 
    fall_pose = [-7.779e-005,  -1.2,  -0.000209793,  1,  -0.8,  0.000244781,  0.31129,  -0.159481,  -0.115399,  -0.636277,  0,  0,  0,  -7.77902e-005,  -1.2,  -0.000209794,  1,  -0.8,  0.000244781,  0.31129,  0.159481,  0.115399,  -0.636277,  0,  0,  0,  0,  0,  0]
    hcf.seq_svc.setJointAngles(fall_pose, 1)
    hcf.seq_svc.waitInterpolation()
    print(fall_pose[1])

    #simulate sensor value when robot on the ground
    if fall_pose[1] == -1.2 and fall_pose[3] == 1 :
        force_sensor = 1
        orientation_sensor[0] = 90
        orientation_sensor[1] = 0
        orientation_sensor[2] = 90
       
    initial_pose = [-7.779e-005,  -0.378613,  -0.000209793,  0.832038,  -0.452564,  0.000244781,  0.31129,  -0.159481,  -0.115399,  -0.636277,  0,  0,  0,  -7.77902e-005,  -0.378613,  -0.000209794,  0.832038,  -0.452564,  0.000244781,  0.31129,  0.159481,  0.115399,  -0.636277,  0,  0,  0,  0,  0,  0]
    hcf.seq_svc.setJointAngles(initial_pose, 1)
    hcf.seq_svc.waitInterpolation()

def stand():
    pose1 = [-7.779e-005,  -1.5,  -0.000209793,  1.4,  -0.452564,  0.000244781,  .31129,  -0.159481,  -0.115399,  -1.636277,  0,  0,  0,  -7.77902e-005,  -1.5,  -0.000209794,  1.4,  -0.452564,  0.000244781,  .31129,  0.159481,  0.115399,  -1.636277,  0,  0,  0,  0,  0,  0]
    pose2 = [-7.779e-005,  -1.5,  -0.000209793,  1.4,  -0.452564,  0.000244781,  .31129,  -0.159481,  -0.115399,  -1.936277,  0,  0,  0,  -7.77902e-005,  -1.5,  -0.000209794,  1.4,  -0.452564,  0.000244781,  .31129,  0.159481,  0.115399,  -1.936277,  0,  0,  0,  0,  0,  0]
    pose3 = [-7.779e-005,  -1.5,  -0.000209793,  1.4,  -0.452564,  0.000244781,  -.31129,  -0.159481,  -0.115399,  -1.936277,  0,  0,  0,  -7.77902e-005,  -1.5,  -0.000209794,  1.4,  -0.452564,  0.000244781,  -.31129,  0.159481,  0.115399,  -1.936277,  0,  0,  0,  0,  0,  0]
    pose4 = [-7.779e-005,  -2.5,  -0.000209793,  1.4,  -0.452564,  0.000244781,  -.31129,  -0.159481,  -0.115399,  -1.936277,  0,  0,  0,  -7.77902e-005,  -1.5,  -0.000209794,  1.4,  -0.452564,  0.000244781,  -.31129,  0.159481,  0.115399,  -1.936277,  0,  0,  0,  0,  0,  0]
    pose5 = [-7.779e-005,  -2.5,  -0.000209793,  1.4,  -0.452564,  0.000244781,  -.31129,  -0.159481,  -0.115399,  -1.936277,  0,  0,  0,  -7.77902e-005,  -2.5,  -0.000209794,  1.4,  -0.452564,  0.000244781,  -.31129,  0.159481,  0.115399,  -1.936277,  0,  0,  0,  0,  0,  0]
    pose6 = [-7.779e-005,  -2.7, -0.000209793,  1.4,  -0.452564,  0.000244781,  -.61129,  -0.159481,  -0.115399,  -1.936277,  0,  0,  0,  -7.77902e-005,  -2.7,  -0.000209794,  1.4,  -0.452564,  0.000244781,  -.61129,  0.159481,  0.115399,  -1.936277,  0,  0,  0,  0,  0,  0]
    pose7 = [-7.779e-005,  -1.378613,  -0.000209793,  0.832038,  -0.452564,  0.000244781,  0.31129,  -0.159481,  -0.115399,  -0.636277,  0,  0,  0,  -7.77902e-005,  -1.378613,  -0.000209794,  0.832038,  -0.452564,  0.000244781,  0.31129,  0.159481,  0.115399,  -0.636277,  0,  0,  0,  0,  0,  0]  
    pose8 = [-7.779e-005,  -0.378613,  -0.000209793,  0.832038,  -0.452564,  0.000244781,  0.31129,  -0.159481,  -0.115399,  -0.636277,  0,  0,  0,  -7.77902e-005,  -0.378613,  -0.000209794,  0.832038,  -0.452564,  0.000244781,  0.31129,  0.159481,  0.115399,  -0.636277,  0,  0,  0,  0,  0,  0]
    standup_pose = [pose1,pose2,pose3,pose4,pose5,pose6,pose7,pose8] 
    timer = 2;
    for x in range(0, 8):
         hcf.seq_svc.setJointAngles(standup_pose[x], timer)
         hcf.seq_svc.waitInterpolation()
         if x == 5 :
            timer = 5
            
    #simulate sensor value wen robot is upright
    force_sensor = 0 
    orientation_sensor[0] = 0
    orientation_sensor[1] = 90
    orientation_sensor[2] = 0

def demo():
    init()
    test_walk()  
    fall()
    
    if orientation_sensor[0] != 0 and orientation_sensor[1] != 90 and orientation_sensor[2] != 0 :
        stand();
    
    test_walk()  

if __name__ == '__main__':
    demo()
