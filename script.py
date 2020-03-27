import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

start_time = time.time()

def stocks_fucn(url, size):
    req = requests.get(url)
    bigboy = BeautifulSoup(req.content, "lxml")
    price_box = bigboy.find("div", attrs={"class": "company-secondary-data"})
    name_box = bigboy.find("div", attrs={"class": "company-title"})
    print(name_box.text.strip()[0:size])  # Company name
    print("Preço Atual Descida Descida(%)")
    print(price_box.text.strip())  # Company value
    opening_box = bigboy.find("table", attrs={"class": "table table-other-indexes"})

    def tableDataText(table):
        def rowgetDataText(tr, coltag='td'):  # td (data) or th (header)
            return [td.get_text(strip=True) for td in tr.find_all(coltag)]

        rows = []
        trs = table.find_all('tr')
        headerow = rowgetDataText(trs[0], 'th')
        if headerow:
            rows.append(headerow)
            trs = trs[1:]
        for tr in trs:
            rows.append(rowgetDataText(tr, 'td'))
        return rows

    table = tableDataText(opening_box)
    print(pd.DataFrame(table, columns=[name_box.text.strip()[0:size], "     Valor em Euros €"]), end="\n\n\n")


company_url = [("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTALT0AE0002&sectorid=240", 16),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTBCP0AM0015&sectorid=810", 25),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTCOR0AE0006&sectorid=416", 23),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTCTT0AM0001&sectorid=000", 30),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTEDP0AM0009&sectorid=720", 43),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=ES0127797019&sectorid=720", 15),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTFRV0AE0004&sectorid=188", 29),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTGAL0AM0009&sectorid=078", 21),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTIBS0AM0008&sectorid=539", 7),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTJMT0AE0001&sectorid=630", 22),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTMEN0AE0005&sectorid=137", 20),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTPTI0AM0006&sectorid=156", 21),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTZON0AM0006&sectorid=543", 6),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTPTC0AM0009&sectorid=673", 11),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTREL0AM0008&sectorid=720", 33),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTSEM0AM0004&sectorid=132", 31),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTSNP0AE0008&sectorid=879", 13),
               ("https://www.bancomontepio.pt/mercados/empresa-cotada?bolsa=LS&lista=6&isin=PTSON0AM0001&sectorid=630", 24)]


#size = [16, 25, 23, 30, 43, 15, 29, 21, 7, 22, 20, 21, 6, 11, 33, 31, 13, 24]

#for i in range(len(size)):
    #stocks_fucn(company_url[i],size[i])

#[stocks_fucn(company_url[i],size[i]) for i in range(len(size))]

[stocks_fucn(tup[0],tup[1]) for tup in company_url]

print("How long it took to execute {0}".format
