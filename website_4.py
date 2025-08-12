from main_fuctions import *



def strinint2(string:str)->int:
    string=string.replace('\t', '')
    string=string.replace('\n', '')
    return strinint(string)



def func_request(user, req=None, link=None):
    header={"user-agent":user}
    if req==None:
        return BeautifulSoup(requests.get(link, headers=header).text, "lxml")
    return BeautifulSoup(requests.get(f"https://b2b.autorus.ru/search/?pcode={req}&whCode=", headers=header).text, "lxml")


def search_in_html_link(html:BeautifulSoup)->list[str]:
    arr=list(html.find_all("a", class_="startSearching"))
    ln=len(arr)
    if ln==0:
        return None
    for i in range(ln):
        arr[i]="https://b2b.autorus.ru/"+arr[i].get("href")
    return arr


def search_price(html:BeautifulSoup)->list[int]:
    main_arr=list(html.find_all("td", class_="resultPrice"))
    main_arr=[strinint2(i.text) for i in main_arr if len(i.get("class"))==1]
    return main_arr


def website_4(req, user):
    html=func_request(user, req=req)
    arr_link=search_in_html_link(html)
    if arr_link==None:
        return {f"https://b2b.autorus.ru/search/?pcode={req}&whCode=":search_price(html)}
    main_dt=dict()
    for i in arr_link:
        main_dt[i]=search_price(func_request(user, link=i))
    return main_dt