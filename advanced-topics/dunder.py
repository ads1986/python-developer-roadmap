#Font: https://www.section.io/engineering-education/dunder-methods-python

print("#Dunder")

class Software: 
    names = []
    versions = {}

    def __init__(self, names):
        if names:
            self.names = names.copy()
            for name in names:
                self.versions[name] = 1
        else:
            raise Exception("Please Enter the names")
            
    def __str__(self):
        s = "The current softwares and their versions are listed below: \n"
        for key,value in self.versions.items():
            s+= f"{key} : v{value} \n"
        return s

    def __setitem__(self,name,version):
        if name in self.versions:
            self.versions[name] = version
        else:
            raise Exception("Software Name doesn't exist")
            
    def __getitem__(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception("Software Name doesn't exist")
            
    def __delitem__(self,name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception("Software Name doent exist")
            
    def __len__(self):
        return len(self.names)
        
    def __contains__(self,name):
        if name in self.versions:
            return True
        else:
            return False
    
p = Software(['S1', 'S2', 'S3'])
p['S2'] = 2
del p['S1']
#p['2'] = 2 Will raise an exception
print(p['S2'])
print(len(p))

if 'S2' in p:
    print("Software Exists")
else:
    print("Software DOESN'T exist")

print(p)
#p1 = Software([]) Will raise an exception

print()
