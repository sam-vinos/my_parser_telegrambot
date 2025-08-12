from main_fuctions import *


def func_request(link, user, req=None)->BeautifulSoup:
    header={"user-agent":user}
    if req==None:
        return BeautifulSoup(requests.get(link, headers=header).text, "lxml")
    return BeautifulSoup(requests.get(f"https://shop.autoeuro.ru/main/search?text={req}&whs=&crosses=0&crosses=1", headers=header).text, "lxml")


def search_in_html_link(html:BeautifulSoup)->list[str]:
    arr=list(html.find_all("span", class_="a_button"))
    ln=len(arr)
    if ln==0:
        return None
    for i in range(ln):
        arr[i]=arr[i].get("data-href")
    return arr


def search_price(html:BeautifulSoup)->list[BeautifulSoup]:
    main_arr=list()
    html=html.find("div", id="commoninfo") #<<<
    for best_or_all in ("best", "all"):
        for snk in ("s", "N", "k"):
            ind_1=0
            bl=0
            while True:
                ind_0=0
                while True:
                    price=html.find("div", id=f"stat_{best_or_all}_{snk}_{ind_1}_{ind_0}")
                    if price==None:
                        bl+=1
                        break
                    else:
                        main_arr.append(price)
                    ind_0+=1
                if bl==10:
                    break
                ind_1+=1
    return main_arr



def search_all_price(req, user, main_link, search_link):
    html=func_request(search_link, user, req)
    arr_link=search_in_html_link(html)
    if arr_link==None:
        return {f"https://shop.autoeuro.ru/main/search?text={req}&whs=&crosses=0&crosses=1":search_price(html)}
    main_dt=dict()
    for link in arr_link:
        Link=main_link+link
        main_dt[Link]=search_price(func_request(Link, user))
    return main_dt


def website_1(req, user):
    main_link="https://shop.autoeuro.ru"
    search_link="https://shop.autoeuro.ru/main/search"
    dt=search_all_price(req, user, main_link, search_link)
    for key in dt:
        arr_link=dt[key]
        for ind in range(len(arr_link)):
            arr_link[ind]=strinint(arr_link[ind].text)
    return dt
