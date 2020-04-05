# composition represents a situation where we have two different classes that are related to each other 
# but one class is not inherited from the other and one class makes use of code contained in another class 

# example: imagine we have a Package class which represents a software package. It contains attributes about the software 
# package, like name, version, and size. We also have a Repository class which represents all the packages available for 
# installation. While there’s no inheritance relationship between the two classes, they are related. The Repository class 
# will contain a dictionary or list of Packages that are contained in the repository.

class Repository:
    def __init__(self):
        self.packages = {}
        
    def add_package(self, package):
        self.packages[package.name] = package
    
    def total_size(self):
        result = 0
        for package in self.packages.values():
            result += package.size
        return result    