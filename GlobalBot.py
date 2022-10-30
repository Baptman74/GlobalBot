"""
Coucou mon chou !
Deux choses à installer :
    pip install selenium
    pip install webdriver_manager

Il faut également posseder Chrome
puis met ton EMAIL, MDP, temps d'entrainement en minutes, et ton pourcentage de bonnes réponses ci-dessous et paf !
"""

EMAIL = ""
USERNAME = ""
MDP = ""
MINUTES = 60
pourcentage = 80

import random
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager# Initiate the browser
from selenium.webdriver.common.action_chains import ActionChains

browser  = webdriver.Chrome(ChromeDriverManager().install())

#connexion moodlol
browser.get('https://moodle.univ-smb.fr/login/index.php?authCAS=CAS')
browser.find_element_by_id('username').send_keys(USERNAME)
browser.find_element_by_id('password').send_keys(MDP)
sleep(1)
a = browser.find_element_by_xpath('/html/body/div/div[4]/form/div[2]/section/input[4]')
ActionChains(browser).move_to_element(a).click(a).perform()
browser.get('https://moodle.univ-smb.fr/course/view.php?id=14675')

browser.get('https://moodle.univ-smb.fr/course/view.php?id=14675#section-2')
#sleep(1000)
browser.get('https://moodle.univ-smb.fr/mod/lti/view.php?id=169537')

def justeOuFaux():

    rand = random.randint(1,100)

    if rand >= pourcentage :
        return True
    else :
        return False

minu = MINUTES

while minu >= 0:
    temps_passe = 0
    browser.get("https://exam.global-exam.com/")
    browser.get("https://exam.global-exam.com/library/trainings")
    browser.get("https://exam.global-exam.com/library/trainings/sections/487/exercises")
    browser.get("https://exam.global-exam.com/library/trainings/exercises/669/activities")
    
    
    #clique sur l'exercice
    browser.find_element_by_xpath("/html/body/div[1]/main[2]/div/div[2]/div/div[" + str(random.randint(1,6)) + "]/div/div[2]/button").click()
    
    sleep(4)
    temps_passe = temps_passe + 4
    try:
        #clique sur démarrer 
        browser.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div[2]/button").click()
    except:
        #si il n'y a pas le bouton démarrer
        print("noice \n")
    
    
    a = 1
    for i in range(16): 
        
        if a >= 5:
            a = 1
        
        timerrand = random.randint(10,45)
        sleep(timerrand)
        temps_passe = temps_passe + timerrand
        
        browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/button[1]").click()
            
        randomizer = justeOuFaux()
        
        if randomizer == True:
            browser.find_element_by_xpath( "/html/body/div[1]/div/div[2]/div/div[2]/div[" + str(a) + "]/div[2]/div/div/label[" + str(random.randint(1,4)) + "]/div" ).click()
        elif randomizer == False:
            tabl=browser.find_elements_by_class_name("bg-success-05")
            tabl[len(tabl)-1].click()        
        sleep(2)
        temps_passe = temps_passe + 2
        browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/button[2]").click()
        a = a + 1
    sleep(5)
    temps_passe = temps_passe + 5
    minu = minu - (temps_passe/60)
    print (minu)
    
browser.close()