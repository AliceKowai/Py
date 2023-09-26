import pyautogui
import time
import pandas as pandas
import pyperclip
pyautogui.PAUSE=1

pyautogui.hotkey("ctrl","t")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=983, y=441)
pyautogui.write("meu login")

pyautogui.click(x=983, y=628)
pyautogui.wite("minha senha")

pyautogui.click(x=1036, y=609)

time.sleep(5)

pyautogui.click(x=504, y=440)
pyautogui.click(x=872, y=212)
pyautogui.click(x=990, y=628)

tabela = pandas.read_csv(r"D:\Dungeons e Dragons - Honra Entre Rebeldes 2023 1080p WEB-DL DUAL 5.1\Dungeons e Dragons - Honra Entre Rebeldes 2023 1080p WEB-DL DUAL 5.1.mkv")
print(tabela)

total_gasto = tabela["VlorFinal"].sum()
quantidade = tabela["Quantidade"]. sum()
preco_medio = total_gasto / quantidade

pyautogui.hotkey("ctrl","t")
pyautogui.write("magalichan.com")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=135,y=224)
pyautogui.write("devalice117@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.write("Relatorio de compras")

pyautogui.press("tab")
texto = """Ai ai você pode escrever o tanto de texto que quiser
ui ui ui"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")





