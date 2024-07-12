import os
def checkdoc(path):
    if os.path.exists(path):
        return True
    else:
        return False
