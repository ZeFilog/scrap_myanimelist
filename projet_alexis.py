import ssl
import requests
import re

from bs4 import BeautifulSoup as soup
from bs4 import Tag
#from urllib.request import urlopen as uReq
import urllib.request
import certifi
from flask import Flask, request
import os
from pymessenger import Bot
app = Flask(__name__)

liens_annonce_a_decortique = []

def get_liens(recherche): # Making a GET request to the specified URL with the user's search query included
    response = requests.get("https://myanimelist.net/search/all?q="+recherche+"&cat=all") # Setting the regular expressions to find the links of the products and the unique ids of the products
    #https://myanimelist.net/search/all?q=akira&cat=all

    id_liens = '<a href="(.+?)" class="hoverinfo_trigger fw-b fl-l" id=".+?" rel=".+?"'
    bb = '<a href="/" class="Text__SCText-sc-kgt5u3-0 Breadcrumb__Text-sc-1b8swsh-1 gbkHxu lhWiOf">(.+?)</a>'

    with open ('page_de_recherche_alexis', 'w') as file: # Writing the response to a file named "code_ao"
        file.write(response.text)
    with open('page_de_recherche_alexis', 'r') as file:  # Reading the file again
        main = file.read()
        #print(id_liens)
        liens_ads = re.findall(id_liens,main)
        scrap(liens_ads[0])


    return


def scrap(liens):
    url = liens
    #print(url)
    #urllib.request.urlopen(url, cafile=certifi.where(), verify=True)
    #print(liens)
    context = ssl.create_default_context(cafile=certifi.where())
    page_html = urllib.request.urlopen(url, context=context).read()

    #uClient = uReq(url)
    #page_html = uClient.read()
    page_soup = soup(page_html, features='html.parser')

    titre = page_soup.find('h1').text
    synopsis = page_soup.find('h2',string = 'Synopsis').find_next('p').text
    rank = page_soup.find("span","numbers popularity").text
    score = page_soup.find("div", "score").text
    members = page_soup.find('span','numbers members').text

    type = page_soup.find("h2", string="Information").find_next('div').text
    date_sortie = page_soup.find("span", string="Status:").find_next('div').text

    studio = page_soup.find("span", string="Studios:").find_next('a').text
    source = page_soup.find("span", string="Studios:").find_next('div').text



    popularite = ''




    return print(titre,rank,score,members,type,date_sortie,studio,source,synopsis)

#get_liens("Akira")

bot = Bot("82e30ada6b2d86f929cd89b3235dfb40")




