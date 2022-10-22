import time

from selenium import webdriver


class BotInstagram():

    def __init__(self):
        self.drive = webdriver.Chrome(executable_path="chromedriver.exe")

    def entrar_link(self, link):
        self.drive.get(link)

    def pegar_link_das_fotos(self):
        os_links = self.drive.find_elements_by_tag_name('_aa_c')
        
        todos_os_links = []
        for os_link in os_links:
            href = os_link.get_attribute("href")
            print(href)
            # if
            todos_os_links.append(href)

    def dar_like(self):
        pass

    def comentar(self, comentario):
        pass

bot = BotInstagram()
bot.entrar_link("https://www.instagram.com/")
time.sleep(15)
bot.entrar_link("https://www.instagram.com/_babioliveiraaa/")
time.sleep(2)
bot.pegar_link_das_fotos()