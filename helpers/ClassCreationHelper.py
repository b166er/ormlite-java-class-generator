def getJavaType(sqliteType): 
    for case in switch(sqliteType):
        if case ("INTEGER"):
            return "int"
            break
        if case ("smallint"):
            return "int"
            break
        if case ("mediumint"):
            return "int"
            break
        if case ("bigint"):
            return "int"
            break
        if case ("tinyint"):
            return "int"
            break
        if case ("int"):
            return "int"
            break
        if case ("decimal"):
            return "float"
            break
        if case ("REAL"):
            return "float"
            break
        if case ("TEXT"):
            return "String"
            break
        if case ("varchar"):
            return "String"
            break
        if case ("char"):
            return "String"
            break
        if case ("BLOG"):
            return "Object"
            break;
        if case ("time"):
            return "time"
            break;
        if case ("timestamp"):
            return "datetime"
            break;
        if case ("datetime"):
            return "datetime"
            break;
        if case ("date"):
            return "date"
            break;
        if case ("enum"):
            return "string"
            break;
        raise Exception('SQL-Type not found: ' + sqliteType)


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
