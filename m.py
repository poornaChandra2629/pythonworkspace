dic = {'. _':'A' , '_ . . .':'B', '_ . _ .':'C','_ . .':'D', '.':'E',
     '. . _ .':'F','_ _ .':'G','. . . .':'H','. .':'I','. _ _ _':'J', 
     '_ . _':'K', '. _ . .':'L','_ _':'M', '_ .':'N', '_ _ _':'O', 
     '. _ _ .':'P', '_ _ . _':'Q', '. _ .':'R', '. . .':'S', '_':'T',
     '. . _':'U', '. . . _':'V','. _ _':'W','_ . ._':'X', '_ . _ _':'Y',
     '_ _ . .':'Z','. _ _ _ _':1,'. . _ _ _':2, '. . . _ _':3,
     '. . . . _':4,'. . . . .':5, '_ . . . .':6, '_ _ . . .':7,'_ _ _ . .':8,
     '_ _ _ _ .':9, '_ _ _ _ _':0}


stng = input()


lis = stng.split('       ')


for i in lis:

   inlis = i.split('   ')
 
   for j in inlis:

      print(dic[j],end='')
    
print(end=' ')