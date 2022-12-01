name='        har       shit      '
dots='...............'
# lstrip()method :removes left side space
print(name+dots)

print(name.lstrip() + dots)

# rstrip()method :removes right space
print(name.rstrip()+dots)

# strip()method : removes space from both side
print(name.strip()+dots)

#to remove all spaces : name.replace(' ','whth ehatever you want to remove space')
print(name.replace(' ','')+dots)


# take two comma seperated inputs from user
# 1) user name  , ex- 'Aman'
# 2) a single character , 'a'

#output - 2 print lines 
# 1) user's name length
# 2) count the character that user inputed 


name, char=input('enter comma seperated name and character : ').split(',')
print('length of your name is {} '.format(len(name)))
print(f'count character : {name.strip().lower().count(char.strip().lower())}') #case sensitive hatane ke liye name ko lower kara , fir char ko lower kara, aab hume name me se count karna hai lower char


#AMan --> aman
#'  AMan  ' -->  'AMan' -->  'aman'
#'  A  ' -->  'A' --> 'a'

#name.strip().lower().count(char.strip().lower())
#char.strip().lower()