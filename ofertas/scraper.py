import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .models import Produto

def scroll_to_bottom(driver):
    """Scroll to the bottom of the page to load all products."""
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.body.scrollHeight") > last_height
        )
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape():
    url = "https://www.mercadolivre.com.br"
    busca = "Computador gamer i7 16gb ssd 1tb"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "as_word"))
        )
        
        search_box.send_keys(busca)
        search_box.send_keys(Keys.RETURN)

        scroll_to_bottom(driver)

        produtos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ui-search-result"))
        )

        produtos_processados = set()

        for produto in produtos:
            try:
                nome = produto.find_element(By.CSS_SELECTOR, "h3.poly-component__title-wrapper a").text
                imagem_url = produto.find_element(By.CLASS_NAME, "poly-component__picture").get_attribute("src")
                preco = produto.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
                
                try:
                    link = produto.find_element(By.XPATH, ".//a[contains(@class, 'ui-search-link')]").get_attribute("href")
                except Exception as e:
                    print(f"Link não encontrado para o produto {nome}: {e}")
                    link = None

                if link in produtos_processados:
                    print(f"Produto {nome} já foi processado.")
                    continue

                produtos_processados.add(link)

                tipo_entrega = produto.find_element(By.CLASS_NAME, "poly-component__shipped-from").text
                frete_gratis = "Frete grátis" in produto.text


                try:
                    preco_sem_desconto = produto.find_element(By.CLASS_NAME, "andes-money-amount--previous .andes-money-amount__fraction").text
                except Exception:
                    preco_sem_desconto = None
                
                try:
                    percentual_desconto_str = produto.find_element(By.CLASS_NAME, "andes-money-amount__discount").text
                    percentual_desconto = int(re.search(r'\d+', percentual_desconto_str).group())
                except Exception:
                    percentual_desconto = None

                try:
                    parcelamento = produto.find_element(By.CLASS_NAME, "poly-price__installments").text
                except Exception:
                    parcelamento = None

                if link:
                    Produto.objects.create(
                        nome=nome,
                        imagem_url=imagem_url,
                        preco=preco,
                        preco_sem_desconto=preco_sem_desconto,
                        percentual_desconto=percentual_desconto,
                        parcelamento=parcelamento,
                        link=link,
                        tipo_entrega=tipo_entrega,
                        frete_gratis=frete_gratis
                    )
                    print(f"Produto {nome} processado com sucesso!")
                else:
                    print(f"Produto {nome} ignorado devido à falta de link.")
            except Exception as e:
                print(f"Erro ao processar produto: {e}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        driver.quit()
