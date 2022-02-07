from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import time
from time import sleep



navegador = webdriver.Chrome(r'C:\Users\USER\Desktop\arquivo\chromedriver.exe')

navegador.get('https://web.whatsapp.com/')

sleep(15)
contato = ('O Mais Gost')
def chat(contato):
    campo_pesquisa = navegador.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
    sleep(3)
    #//*[@id="main"]/div[3]/div/div[2]/div[3]/div[6]/div/div/div/div[1]/div[2]
    #//*[@id="main"]/div[3]/div/div[2]/div[3]/div[12]/div/div/div/div[1]/div[2]
    #//*[@id="main"]/div[3]/div/div[2]/div[3]/div[12]/div/div/div/div[1]/div[2]/span[1]/span
def pegando_msg():#//*[@id="main"]/div[3]/div/div[2]/div[3]/div[26]/div/div/div/div[1]/div
    mensagem = navegador.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[17]/div/div/div/div[1]/div')
    mensagem_v = mensagem.text
    horario = navegador.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[3]/div[8]/div/div/div/div[2]/div/span')
    horario_msg = horario.text
    
    print(f'Esse é o horario da msg {horario_msg}')
    print(f'Essa é a msg! {mensagem_v}')
    return mensagem_v
    
def envia_msg():
    mensagem_a_enviar = 'Olá roberto'
    while True:
        msg = pegando_msg()
        
        if msg == 'Roberto':
            campo_mensagem = navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]') 
            campo_mensagem.click()
            sleep(3)
            campo_mensagem.send_keys(mensagem_a_enviar)
            campo_mensagem.send_keys(Keys.ENTER)
            break
        else:
            sleep(10)
            print('ainda n encontrado')
            
    
    
chat(contato)
pegando_msg()
envia_msg()