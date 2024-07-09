import pyautogui
from time import sleep
import webbrowser
import pandas 

webbrowser.open('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
sleep(2)
pyautogui.press('tab')
pyautogui.write('qualquercoisa')
sleep(2)
pyautogui.press('tab')
pyautogui.write('qualquercoisa')
pyautogui.press('tab')
pyautogui.press('enter')

sleep(3)
tabela = pandas.read_csv('meuprojeto/produtos.csv')

for linha in tabela.index:
    pyautogui.click(740,273, duration=2)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    sleep(2)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    sleep(2)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    sleep(2)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    sleep(2)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    sleep(2)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    sleep(2)
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
      pyautogui.write(obs)
   
    sleep(2)
    pyautogui.press('tab')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.scroll(5000)
    sleep(3)        