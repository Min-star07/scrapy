"""
@author: Min Li
@e-mail: limin93@ihep.ac.cn
@file: test.py.py
@time: 2023/12/2 22:30
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

import io
import sys

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'}
    # https: // movie.douban.com / top250
    title_list =[]
    quote_list = []
    response = requests.get(url,headers=headers)
    print(response.status_code)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "title"})
    for title in all_titles:
        info_string = title.string
        if "/" not in info_string:
            title_list.append(info_string)
    all_quotes = soup.findAll("span", attrs={"class": "inq"})
    for quote in all_quotes:
        quote_string = quote.string
        quote_list.append(quote_string)
    # print(title_list, quote_list)
    return zip(title_list, quote_list)

if __name__  == '__main__':
    # https://movie.douban.com/top250?start=25&filter=

    with open("doubantop250.txt", "w") as f:
        # f.write("No")
        # f.write("\t")
        # f.write("film")
        # f.write("\t")
        # f.write("quote")
        # f.write("\n")
        print(f"No-----film-----quote", file=f)
        for i in range(10):
            url = "https://movie.douban.com/top250?start=" + str(i*25) + "&filter="
            infos = get_page(url)
            # print(infos)
            # print(infos)
            for j, info in enumerate(infos):
                # f.write(str(i*25 + j))
                # f.write("\t")
                # f.write(info[0])
                # f.write("\t")
                # f.write(info[1])
                # f.write("\n")
                print(f"{str(i*25 + j)}  {info[0]}  {info[1]}", sep ="\t", file=f)


