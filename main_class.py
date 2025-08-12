
class Auto_parts_website:
    def __init__(self, name, mainfunc):
        self.__name=name
        self.__mainfunc=mainfunc
        return None


    def main_calculation(self, arg1, arg2)->list|str|bool:
        res=self.__mainfunc(arg1, arg2)
        keys=list(res.keys())
        for key in keys:
            if len(res[key])!=0:
                break
        else:
            return [keys, False, self.__name]
        minprice=float("inf")
        link=None
        for key in keys:
            element=res[key]
            if len(element)>0 and (mn:=min(element))<minprice:
                minprice=mn
                link=key
        return [link, minprice, self.__name]



class Auto_parts_notparsing:
    def __init__(self, name, generlink):
        self.__name=name
        self.__generlink=generlink
        return None
    
    def get_name(self):
        return self.__name


    def get_link(self, get):
        return self.__generlink(get)