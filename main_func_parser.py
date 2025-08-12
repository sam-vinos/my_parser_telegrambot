from list_website import *
from main_fuctions import *


def maincalculation(req:str)->list[list[str|int|bool]]:
    arr=[website1, website2, website4]
    arr_not_parsing=[website3, website5]
    user=fakeuseragent()
    ln=len(arr)
    res_arr=[None for _ in range(ln)]
    for ind in range(ln):
        res_arr[ind]=arr[ind].main_calculation(req, user)
    ln=len(arr_not_parsing)
    res_arr_not_parsing=[None for _ in range(ln)]
    for ind in range(ln):
        res_arr_not_parsing[ind]=[arr_not_parsing[ind].get_link(req), arr_not_parsing[ind].get_name()]
    return res_arr, res_arr_not_parsing


def final_func_parser(req):
    arr1,arr2=maincalculation(req)
    for ind in range(len(arr1)):
        if arr1[ind][1]==False:
            arr2.append([arr1[ind][0], arr1[ind][2]])
            arr1.pop(ind)
    return arr1, arr2


def main(req):
    main_string=str()
    try:
        arr1,arr2=final_func_parser(req)
    except:
        return "Неизвестная ошибка"
    if len(arr1)==0:
        main_string=f"Ваш запрос: {req}\n\n0 полученых ответов, возможно ошибка в запросе или неполадки на серверaх\nСсылки:"
        for i in arr2:
            main_string+=f"\n {i[1]}"
            if type(i[0])==list and len(i[0])>1:
                main_string+=':'
                for link in i[0]:
                    main_string+=f"\n  {link}"
            else:
                if type(i[0])==list:
                    i[0]=i[0][0]
                main_string+=f" - {i[0]}"
        return main_string
    main_string=f"Ваш запрос: {req}\n{len(arr1)} из 3 сайтов ответили\n\nЦены:"
    string=str()
    for i in arr1:
        string+=f"\n{i[2]} - {i[1]} p\n{i[0]}"
    main_string+=string
    main_string=main_string+"\n\nСсылки:"
    string=str()
    for i in arr2:
        string+=f"\n {i[1]}"
        if type(i[0])==list and len(i[0])>1:
            string+=':'
            for link in i[0]:
                string+=f"\n  {link}"
        else:
            if type(i[0])==list:
                i[0]=i[0][0]
            string+=f" - {i[0]}"
    main_string=main_string+string
    return main_string