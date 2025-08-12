from main_fuctions import *



def func_request(user, req=None, link=None)->BeautifulSoup:
    header={"user-agent":user}
    if req==None:
        return BeautifulSoup(requests.get(link, headers=header).text, "lxml")
    link=f"https://v01.ru/auto/search/?q={req}"
    return BeautifulSoup(requests.post(link, headers=header).text, "lxml")


def strinlink(string):
    string=list(string)
    ln=len(string)
    ind=0
    res=str()
    while ind<ln:
        if string[ind]=="\'":
            while ind<ln:
                ind+=1
                if string[ind]=="\'":
                    return res
                res+=string[ind]
        ind+=1
    return None


def search_in_html_link(html:BeautifulSoup)->list[str]:
    arr_link=list(html.find_all("tr", class_="catalog-table-brand-row js-search-item"))
    ln=len(arr_link)
    if ln==0:
        return None
    for ind in range(ln):
        arr_link[ind]=strinlink(arr_link[ind].get("onclick"))
    return arr_link


def search_price(html:BeautifulSoup)->list[int]:
    arr_price=list(html.find_all("td", class_="price number-cell"))
    for ind in range(len(arr_price)):
        arr_price[ind]=int(arr_price[ind].get("data-price"))
    return arr_price


def website_2(req, user):
    html=func_request(user, req=req)
    arr_link=search_in_html_link(html)
    if arr_link==None:
        return {f"https://v01.ru/auto/search/?q={req}":search_price(html)}
    dt=dict()
    for link in arr_link:
        main_link="https://v01.ru"+link
        dt[main_link]=search_price(func_request(user=user, link=main_link))
    return dt