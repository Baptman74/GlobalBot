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
from selenium.webdriver.common.by import By
import sys
from tqdm import trange

browser  = webdriver.Chrome(ChromeDriverManager().install())

print("demarrage du bot")
for i in trange (0,5):
    sleep(0.5)

print("\nconnexion a moodle")
for i in trange (0,5):
    sleep(0.5)

#connexion moodlol
browser.get('https://moodle.univ-smb.fr/login/index.php?authCAS=CAS')
browser.find_element('id','username').send_keys(USERNAME)
browser.find_element('id','password').send_keys(MDP)
print("\nconnexion reussie")

a = browser.find_element('xpath','/html/body/div/div[4]/form/div[2]/section/input[4]')
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

print("\nacces a Globalexam")
for i in trange (0,5):
    sleep(0.5)

while minu >= 0:
    temps_passe = 0
    browser.get("https://exam.global-exam.com/")
    browser.get("https://exam.global-exam.com/library/trainings")
    browser.get("https://exam.global-exam.com/library/trainings/sections/487/exercises")
    browser.get("https://exam.global-exam.com/library/trainings/exercises/669/activities")

    sleep(5)
    #clique sur l'exercice
    random_int = random.randint(1,6)

    for i in range(0,5):
        try:
            browser.find_element('xpath',"/html/body/div[1]/main[2]/div/div[2]/div/div[" + str(random_int) + "]/div/div[2]/button").click()
        except:
            print("error n° " + str(i))
            sleep(4)
            temps_passe = temps_passe + 4
            if i >= 5:
                browser.close()
        else :
            break

    print("\nlancement de l'exercice " + str(random_int) + "\n" )

    """
    /html/body/div[1]/main[2]/div/div[2]/div/div[1]/div/div[2]/button
    /html/body/div[1]/main[2]/div/div[2]/div/div[2]/div/div[2]/button
    /html/body/div[1]/main[2]/div/div[2]/div/div[3]/div/div[2]/button
    /html/body/div[1]/main[2]/div/div[2]/div/div[4]/div/div[2]/button
    /html/body/div[1]/main[2]/div/div[2]/div/div[5]/div/div[2]/button
    /html/body/div[1]/main[2]/div/div[2]/div/div[6]/div/div[2]/button
    """

    sleep(5)
    temps_passe = temps_passe + 5

    for i in range(0,5):

        try:
            #clique sur démarrer
            browser.find_element('xpath',"/html/body/div[1]/div[1]/main/div/div/div[2]/button").click()
        except:
            #si il n'y a pas le bouton démarrer
            print("error \n")
            sleep(4)
            temps_passe = temps_passe + 4
            if i >= 5:
                browser.close()
        else:
            print("demarrage de l'exercice\n")
            break


    a = 1
    for i in range(16):

        if a >= 5:
            a = 1

        print("question n°"+ str(i)+ "\n")
        timerrand = random.randint(10,45)
        print("attente pendant "+str(timerrand)+" secondes\n")
        for i in trange(timerrand):
            sleep(1)
        temps_passe = temps_passe + timerrand

        browser.find_element('xpath',"/html/body/div[1]/div/div[3]/div/button[1]").click()

        randomizer = justeOuFaux()

        if randomizer == True:
            browser.find_element('xpath',"/html/body/div[1]/div/div[2]/div/div[2]/div[" + str(a) + "]/div[2]/div/div/label[" + str(random.randint(1,4)) + "]/div" ).click()
        elif randomizer == False:
            tabl=browser.find_elements(By.CLASS_NAME,"bg-success-05")
            tabl[len(tabl)-1].click()
        sleep(2)
        temps_passe = temps_passe + 2
        browser.find_element('xpath',"/html/body/div[1]/div/div[3]/div/button[2]").click()
        a = a + 1
    sleep(5)
    temps_passe = temps_passe + 5
    minu = minu - (temps_passe/60)
    print ("temps restant " + str(int(minu)) + " minutes\n")

browser.close()
print("fin du programme, vous avez travaillé au moins " +str(int(MINUTES))+ " minutes. Bravo :) \n")
print("merci d'avoir utilisé Globalbot, hesitez pas a donner votre avis: ")
print("https://docs.google.com/forms/d/e/1FAIpQLScs4OjK0zu0L6H0ahSwu0qLlHYpxSm76MHpKrUN_bUaq2pa5w/viewform?usp=sf_link")
