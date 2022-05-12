
from ast import pattern
import tkinter as tk
import scrapping as sc
import re

data = []

def seach(text):
    for i in data:
        ch = 0
        for key,value in i.items():
            tem = value + " "
            if ch == 1:
                t1.insert(tk.END,tem)
                t1.insert(tk.END,"฿\n")
            elif re.search(text,value):
                t1.insert(tk.END,tem)
                ch = 1
            

def buttonCLicked():
    global state
    if state == 0:
        label.configure(text="scrapping")
        global data
        data = sc.scrap()
        label.configure(text="done scrapping")
        b1.configure(text="seach")
        tem = ""
        #print(data)
        for i in data:
            for key,value in i.items():
                tem = value + " "
                t1.insert(tk.END,tem)
            t1.insert(tk.END,"฿\n")
        state = 1

    elif state == 1:
        texts = e1.get()
        t1.delete('1.0', tk.END)
        seach(texts)
        b1.configure(text="Back")
        state = 2

    elif state == 2:
        b1.configure(text="seachx")
        t1.delete('1.0', tk.END)
        tem = ""
        for i in data:
            for key,value in i.items():
                tem = value + " "
                t1.insert(tk.END,tem)
            t1.insert(tk.END,"฿\n")
        state = 1

 
    
    

state = 0
app = tk.Tk()
app.geometry("800x600")
app.title('scrapper')
label = tk.Label(text="wait click to begin")
e1 = tk.Entry()
b1 = tk.Button(text="Click me!", command=buttonCLicked)
t1 = tk.Text()

label.pack()
b1.pack()
e1.pack()
t1.pack()

app.mainloop()

#legacy
"""
#find max page
max = soup.find('div', attrs = {'class': 'pagenav'})
pagenumber = max.find_all('a')
maxpage = int(pagenumber[-2].text)
#print(maxpage)

for i in range(1,maxpage):
    url = "https://shop.dexclub.com/products/cats/1/?&page=" + str(i)
    res = reg.get(url)
    res.encoding = "utf-8"
    c = res.content
    soup = BeautifulSoup(c,"html.parser")
    main = soup.find('div', attrs = {'class': 'pboxes'})
    content = main.find_all('div', attrs = {'class': 'pbox'})

    for book in content:
        name = book.find('h2', attrs = {'class': 'name'})
        price = book.find('span', attrs = {'class': 'price'})
        print(name.text)
        print(price.text)
"""
