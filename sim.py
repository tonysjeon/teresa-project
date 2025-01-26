import pybullet as p
import pybullet_data
import time
from sensors.servo import SimServo


dt = 0.01


class Joint:
    YAW = 0
    PITCH = 1
    camera = 2


p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, 0)
p.setRealTimeSimulation(1)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.resetDebugVisualizerCamera(
    cameraDistance=0.15,
    cameraYaw=135,
    cameraPitch=-40,
    cameraTargetPosition=[0, 0, 0.09],
)

robot_id = p.loadURDF("simulation/robot.urdf", [0.0, 0.0, 0.09], useFixedBase=True)

yaw_servo = SimServo("yaw")
pitch_servo = SimServo("pitch")
while True:
    yaw_servo.update()
    pitch_servo.update()
    p.resetJointState(robot_id, Joint.YAW, targetValue=yaw_servo.get_position())
    p.resetJointState(robot_id, Joint.PITCH, targetValue=pitch_servo.get_position())
    time.sleep(dt)
