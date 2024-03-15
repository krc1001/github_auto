from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service('C:\\Users\\LabInfo\\Documents\\KAUÃ R. CORDEIRO\\TesteSelenium_heroku-main\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://github.com/")

    def enviarDados( palavra ):
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"user_email"))
        )
        email_login.clear
        print(1)
        email_login.send_keys(palavra)
        print(2)
        driver.implicitly_wait(5)  
        print(3)
        alert = driver.find_element(By.ID, 'result').text
        return alert
    
    alert = enviarDados('cskrc02122@gmail.com')
    print(4)
    if 'You entered: A' in alert :
     alert = enviarDados(Keys.DELETE)
    if 'You entered: DELETE' in alert :
     alert = enviarDados(Keys.SPACE)
    if 'You entered: SPACE' in alert :
        print(4)
        print("A ultima letra foi encotrada")
        
    else:
        print("Usuário incorreto não reconhecido, teste falhou")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()