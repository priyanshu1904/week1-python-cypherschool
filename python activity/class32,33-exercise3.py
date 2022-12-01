# take two comma seperated inputs from user
# 1) user name  , ex- 'priyanshu'
# 2) a single character , 'i'

#oputput - 2 print lines 
# 1) user's name length
# 2) count the character that user inputed 


name,char=input('enter comma seperated name and character : ').split(',')
print('length of your name is {} '.format(len(name)))
print(f'count character : {name.lower().count(char.lower())}') #case sensitive hatane ke liye name ko lower kara , fir char ko lower kara, aab hume name me se count karna hai lower char
