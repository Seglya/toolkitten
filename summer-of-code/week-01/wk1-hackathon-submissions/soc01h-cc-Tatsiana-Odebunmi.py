
import time
import numpy as np
import math
import random
class Error(Exception):
	"""docstring for Error"""
	pass
class WaterValueError(Error):
	"""docstring for ClassName"""
	pass
x_cur_list=[] #array of curent continet points(x)
y_cur_list=[] #array of curent continet points(y)
x_list=[] #array of checked points(x)
y_list=[] #array of checked points(y)
#checking if curent point of land is in the list of lands, if not will add it to the list
def check_availability(x,y):
	if len(x_cur_list)>0:
		for i in range(len(x_cur_list)):
			if x_cur_list[i]==x:
				if y_cur_list[i]==y:#This point alreadey in the list
					return 
		else:#adding point to the list
		 	x_cur_list.append(x)
		 	y_cur_list.append(y)
		 	return 
	else:#adding point to the list
		x_cur_list.append(x)
		y_cur_list.append(y)
		return 
#checking if curent point was checked before, if not will add it to the list
def checked_coordinates(x,y):
	#print("check_availability %s & %s" %(x,y))
	if len(x_list)>0:
		for i in range(len(x_list)):
			if x_list[i]==x:
				if y_list[i]==y:
					return 1
		else:
		 	x_list.append(x)
		 	y_list.append(y)
		 	return 0
	else:
		x_list.append(x)
		y_list.append(y)
		return 0
#def find_next_continent
#recursion to check each point of the grid
def if_those_land_conected(x,y,index,world):
	check=int(checked_coordinates(x,y))
	if check==0:
		if world[x][y]==1:
			check_availability(x,y)
			if (y+1)<index:
				if_those_land_conected(x,(y+1),index,world)
				if (x+1)<index:
					if_those_land_conected((x+1),(y+1),index,world)
				if(x-1)>=0:
					if_those_land_conected((x-1),(y+1),index,world)
			if (x+1)<index:
				if_those_land_conected((x+1),y,index,world)
				if (y-1)>=0:
					if_those_land_conected((x+1),(y-1),index,world)
			if (x-1)>=0:
				if_those_land_conected((x-1), y,index,world)
				if (y-1)>=0:
					if_those_land_conected((x-1),(y-1),index,world)
			if(y-1)>=0:
				if_those_land_conected(x,(y-1),index,world)
		else:
			if (len(x_cur_list)==0):
				if (y+1)<index:
					if_those_land_conected(x,(y+1),index,world)
				else:
					if (x+1)<index:
						if_those_land_conected((x+1), 0,index,world)
# Main function
def main():
	start_time=time.time()
	x_start=0
	y_start=0
	index=11
	num_lands=[] #array of sizes of land
	sq=pow(index,2)
	world=np.arange(sq).reshape(index,index) #index*index world
	while True:
		try:
			index=int(input("Input the size of world x*x (1...100): "))
			if index>100:
				raise ValueError
			if index<1:
				raise ValueError
			break
		except ValueError:
			print("No valid symbol! Please try again...")
	#randomly filling the world with numbers 0 & 1
	for x in range(index):
		for y in range(index):
			world[x,y]=random.randint(0,1)
	print("The world %s*%s was created" %(index,index))	
	#input start point from the user
	while True:
		try:
			x_start=int(input("Input your start x coordinate (0...%s): " %(index-1)))
			y_start=int(input("Input your start y coordinate (0...%s): " %(index-1)))
			if x_start>=index or x_start<0:
				raise ValueError
			if y_start>=index or y_start<0:
				raise ValueError
			if world[x_start][y_start]==0:
				raise WaterValueError()
			if world[x_start][y_start]==1:
				print("Yahoo it is a land!!!")
			break
		except WaterValueError as Er:
			print("Ooops it is water!!! Please try again... \n")
		except ValueError:
			print("No valid symbol! Please try again...")
	for x in range(index):
		for y in range(index): #printing creted word in format x*x
			print (world[x,y], end='')
		print("")
	"""	world=np.arange(25).reshape(5,5) #5x5 world #1
	world=[[0,1,0,0,1],[1,0,0,1,0],[1,0,0,0,0],[1,0,1,1,1],[0,0,1,1,1]]
	index=5"""
	count_time=time.time()
	if_those_land_conected(x_start,y_start,index,world)
	for x in range(index):
		for y in range(index):
			if_those_land_conected(x,y,index,world)
			if len(x_cur_list)>0:
				num_lands.append(len(x_cur_list))
			x_cur_list.clear()
			y_cur_list.clear()
	print("Created world contain %s continents" %len(num_lands))
	for j in range(len(num_lands)):
		print("%s) %s" %((j+1),num_lands[j]))
	print("The size of continent you landed on is %s cells" %num_lands[0])		
	print ("The largest continent contain %s cells" %max(num_lands))
	print("All procces took %s sec, continent counter %s sec" %((time.time()-start_time),(time.time()-count_time)))
#start point of programm
main()
	