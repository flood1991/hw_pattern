from time import sleep
from multiprocessing import Queue,Process,Value,Array,Pool,TimeoutError,Semaphore
import os
# my_queue = Queue()
# def action(n,a):
# 	number = int(n.value)
# 	for i in range(len(a)):
# 		a[i] = -a[i] * number
# 		print(a[i])
# 	n.value = 3.1415927
	
	

		



# if __name__ == '__main__':
# 	num = Value('d',10)
# 	arr = Array('i',[1,2,3,4,5,6,7])
# 	p = Process(target=action,args=[num,arr])
# 	p2.start()
# 	p.start()
	
# def action(arr):
# 	sleep(3)
# 	for i in range(len(arr)):
# 		arr[i] = str(arr[i])
# def action2(arr):
# 	for i in range(len(arr)):
# 		arr[i] *= 10



# if __name__ == '__main__':
# 	data = Array('i',[1,2,3,4,5,6,7])
# 	p = Process(target=action,args=[data])
# 	p2 = Process(target=action2,args=[data])
# 	p.start()
# 	p2.start()
# 	p.join()
# 	p2.join()
# 	print(data[:])

# def f(sem,x):
# 	sem.acquire()
# 	print(f'action {x}')
# 	sleep(5)
# 	sem.release()



# if __name__ == '__main__':
# 	sem=Semaphore(1)
# 	processes=[]
# 	for i in range(10):
# 		p = Process(target=f,args=[sem,i])
# 		p.start()
# 		processes.append(p)

# end_typing = Event()
# def f(e):
# 	sleep(5)
# 	end_typing.set()
	



# if __name__ == '__main__':
# 	end_typing = Event()
# 	processes=[]
# 	p = Process(target=f,args[end_typing])
# 	p.start()
# 	end_typing.wait()
# 	print('process 1 finished')

if 1<0 and int('a') or 2>1:
	print(15)