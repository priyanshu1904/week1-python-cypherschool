#Q: ask user to input 3 no. and you have to print avg. of three numbers using string formating
a,b,c=input('enter three numbers comma seperated: ').split(',')
#avg=(int(a) + int(b) +int(c))/3 
print('average of three number {}'.format((int(a) + int(b) +int(c))/3))