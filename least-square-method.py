import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
import random
from operator import add


graph_range = 1001
big_grid = np.arange(0,graph_range)
#sin_amp = np.sin(big_grid)
fs = graph_range # sample rate 
f = 4 # the frequency of the signal
sin_amp = 0.2 * (np.sin(2*np.pi*f * (big_grid/fs)))


w_desired_list = [0, 0.3, 0.4, 0.5, 0.6]
# u_list = np.zeros((5, 5))
u_list = [0, 0, 0 , 0, 0]
tmp_list = [0.2, 0.3, 0.4, 0.5, 0.6]
w_actual_list = [0, 0, 0, 0, 0]
noise = 0.03				#AKA noise
que = 0.9

char_function_a = []
char_function_b = []
char_function_c = []
char_function_d = []
char_function_e = []

alpha = 10**6
matrix_k_ai = np.matrix(np.identity(5), copy=False)
matrix_k_ai = matrix_k_ai * alpha

for x in range(graph_range):
	w_desired_list[0] = sin_amp[x]
	char_function_a.append(w_actual_list[0])
	char_function_b.append(w_actual_list[1])
	char_function_c.append(w_actual_list[2])
	char_function_d.append(w_actual_list[3])
	char_function_e.append(w_actual_list[4])
	
	###START FOR ALL K
	##START UPPER K
	#INITIALIZE 5 RANDOM VECTORS u(m) IN A VECTOR
	for j in range(5):
		xsi = ((random.uniform(0,1)) - 0.5) * 2
		u_list[j] = xsi
	
	temp1 = []
	for i in range(5):
		row1 = []
		for j in range(5):
			row1.append(u_list[i]*u_list[j])
		temp1.append(row1)
		
	matrix_u = np.matrix(temp1)

	matrix_right = ((matrix_u) * (matrix_k_ai))
	matrix_left = ((matrix_k_ai) * (matrix_right))
	##END UPPER K
	
	##START LOWER K
	vector_right_list = ((matrix_k_ai) * (np.matrix(u_list).T))
	vector_right_list = np.squeeze(np.asarray(vector_right_list))
	vector_right_list = vector_right_list.tolist()
	
	scalar_left_temp = np.multiply(u_list, vector_right_list)
	scalar_left = sum(scalar_left_temp)
	#scalar_left = 1 + scalar_left
	scalar_left = que + scalar_left
	##END LOWER K
	
	matrix_beta = matrix_left / scalar_left
	
	matrix_k_ai = matrix_k_ai - matrix_beta
	matrix_k_ai = matrix_k_ai * (que**(-1))
	###END FOR ALL K
	
	###START FOR ALL W
	##START FOR Y STAR
	y_star_temp_1 = np.multiply(w_desired_list, u_list)
	y_star_n_1 = sum(y_star_temp_1)
	y_star_n_1 = y_star_n_1 + noise
	##END FOR Y STAR
	
	temp_a_1_t = np.multiply(w_actual_list, u_list)
	temp_a_1 = sum(temp_a_1_t)
	
	temp_b_1 = y_star_n_1 - temp_a_1
	
	temp_c_1 = [k * (temp_b_1) for k in u_list]
	
	gamma = ((matrix_k_ai) * (np.matrix(temp_c_1).T))
	gamma = np.squeeze(np.asarray(gamma))
	gamma = gamma.tolist()
	
	w_actual_list = list(map(add, w_actual_list, gamma))


	

plt.plot(big_grid,char_function_a, label='w1*(n) = 0.2')
plt.plot(big_grid,char_function_b, label='w2*(n) = 0.3')
plt.plot(big_grid,char_function_c, label='w3*(n) = 0.4')
plt.plot(big_grid,char_function_d, label='w4*(n) = 0.5')
plt.plot(big_grid,char_function_e, label='w5*(n) = 0.6')
plt.plot(big_grid, sin_amp)
tmp_string = "noise = {0}".format(noise)
plt.plot([],[], ' ', label=tmp_string)
#tmp_string = "alpha = 10^3"
#plt.plot([],[], ' ', label=tmp_string)
tmp_string = "q = {0}".format(que)
plt.plot([],[], ' ', label=tmp_string)
plt.legend(loc='lower right'), plt.suptitle('Simulation Results of Least Square Method (Recursive)')
# Customize the major grid
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.minorticks_on()
plt.show()