# Script to ping the list of IPs' in parallel and to list the Online and Offline IPs.   

# linux commands to ping the list of IPs parallely.
'''
fping -u -g 192.168.0.1 192.168.0.9 -r 1
fping -a -g 192.168.0.1 192.168.0.9 -r 1
'''


import subprocess  
import random
import pdb


def online_offline_ips():
	'''
	   Function to list down all the online and offline IPs in the given network. 
	'''

	online_IPs = []
	offline_IPs = []

	initial_ip = '192.168.43.171'
	target_ip  = '192.168.43.180'

	p = subprocess.Popen(['fping','-a','-g', initial_ip, target_ip], stdout=subprocess.PIPE)   # linux command to check online IPs
	pass
	p1 = subprocess.Popen(['fping','-u','-g', initial_ip, target_ip], stdout=subprocess.PIPE)  # linux command to check offline IPs

	output,err = p.communicate()                        # writing the data to output
	output1,err = p1.communicate()						# writing the data to output1	

	online_IPs  = output.split()						# list creation
	offline_IPs = output1.split()

	print "Online IPs:::::", online_IPs
	print('---'*20)
	print "Offline IPs::::", offline_IPs
	return random.choice(offline_IPs)					# Generate the random IP from the list of offline_IPs



if __name__ == '__main__':
	o = online_offline_ips()
	print o
