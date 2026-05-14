import time

import pyautogui


#ABRIR NAVEGADOR:
pyautogui.PAUSE = 0.7
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#FAZER UMA PAUSA MAIOR PARA O SITE CARREGAR
time.sleep(3)

pyautogui.click(1234, y=374)
pyautogui.write("ch0892160@gmail.com")
pyautogui.click(x=1227, y=476)
pyautogui.write("12345678")
pyautogui.click(x=956, y=534)

#FAZER UMA PAUSA MAIOR PARA O SITE CARREGAR
time.sleep(3)

#IMPORTAR ARQUIVOS

import pandas

tabela = pandas.read_csv("ProjectPy01/produtos.csv")
print(tabela)

for linha in tabela.index:
    time.sleep(1)
    #codigo = str(tabela.loc[linha, "codigo"])

    pyautogui.click(x=932, y=264)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #MARCA
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #TIPO
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #CATEGORIA
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #PRECO
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #CUSTO
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan": 
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)