import numpy as np
from numpy.linalg import inv
import math
from math import sin, cos, pi 
import time

#input velocity each wheel
v1 = 0		#wheel 1
v2 = 0		#wheel 2
v3 = 0.1	#wheel 3
d = 0.3 	#distance center robot to wheel

#initial start position robot
D_robot_x = 0
D_robot_y = 0
D_robot_th = 0
d_D_robot_x = 0
d_D_robot_y = 0

# matrix 3x1
v_wheel_robot = np.matrix([[v1],[v2],[v3]])
 
# T matrix transltion velocity robot to velocity wheel,matrix 3x3
T_matrix = [ [-sin(math.radians(30)) , cos(math.radians(30)) , d], 
			 [-cos(math.radians(60)) , -sin(math.radians(60)) , d],
			 [1 , 0 , d ] ]
T_matrix = np.matrix(T_matrix)

# invest matrix
T_matrix_inv = inv(T_matrix)

# dot matrix ( T matrix and velocity wheel ) to find velocity of robot
v_at_robot = np.dot(T_matrix_inv,v_wheel_robot)

v_r_x,v_r_y,v_th = v_at_robot


timer_a = time.time() # startr time


while True:
	if time.time() - timer_a > 0.1: #sampling time 0.1 second
		timer_a = time.time()
	
		d_D_robot_x = v_r_x * 0.1
		D_robot_x =  D_robot_x + d_D_robot_x
		

		d_D_robot_y = v_r_y * 0.1
		D_robot_y = D_robot_y + d_D_robot_y

		d_D_robot_th = v_th * 0.1
		D_robot_th = D_robot_th + d_D_robot_th  

		print D_robot_x
		print D_robot_y
		print D_robot_th
		print "............"



# print 	T_matrix
# print "................."
# print T_matrix_inv

