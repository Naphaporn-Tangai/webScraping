import re

import requests as reg
from bs4 import BeautifulSoup
def scrap():
    data = []
    page_pattern = re.compile(r'<div.*class=.pagenav.*>+[\S\s]+?</div>')
    pagemax_pattern = re.compile(r'(?<=page=)\d+')

    url = "https://shop.dexclub.com/products/cats/1/"
    res = reg.get(url)
    res.encoding = "utf-8"
    c = res.content
    soup = BeautifulSoup(c,"html.parser")
    #print(soup.prettify())

    pagenum = page_pattern.findall(soup.prettify())
    #print(pagenum)
    pagemax = pagemax_pattern.findall(BeautifulSoup(pagenum[0],features="lxml").prettify())
    #print(max(pagemax))

    pbox_pattern = re.compile(r'<div.*class=.pbox.*>+[\S\s]+?</div>')
    name_pattern = re.compile(r'(?<=title=")\[.+\].+(?="/>)')
    price_pattern = re.compile(r'(?<=<span class="price">\s          )\d*')


    for i in range(1,int(max(pagemax))+1):
        url = "https://shop.dexclub.com/products/cats/1/?&page=" + str(i)
        res = reg.get(url)
        res.encoding = "utf-8"
        c = res.content
        soup = BeautifulSoup(c,"html.parser")

        pboxes = pbox_pattern.findall(soup.prettify())
        for j in pboxes:
            pbox = j
            names = name_pattern.findall(pbox)
            if names:
                price = price_pattern.findall(pbox)
                content = {"name":names[0],"price":price[0]}
                data.append(content)
    #print(data)
    return data
    