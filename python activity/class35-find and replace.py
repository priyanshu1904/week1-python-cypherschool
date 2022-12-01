#replace() method
#find() method

#string='is she is beautiful and she is a good dancer'
#print(string.replace('is','was', 1))  #sirf ek aur opehla hi she replace karna hai was se
  
  
  
#find() method  : jis position se is start hora hai vo num. print kardega

#print(string.find('is'))

#print(string.find('is',1)) #isme hume 2nd vale she ki position jaani thi to 1st se start kiya taaki 0 pe jo she hai usse na counr=t kare

string='she is beautiful and she is a good dancer'

# Q: find the position of second she and we dont know the value of 1st she

pos1=string.find('is') # pos1--->number
pos2=string.find('is', pos1 + 1)
print(pos2)

