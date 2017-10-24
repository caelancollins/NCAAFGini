import numpy as np
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup, SoupStrainer
import requests
import time
import matplotlib.pyplot as plt


def gini(data):
    array = np.sort(data)
    # plt.plot(array)
    # plt.ylabel('Rating Score')
    # plt.plot([0,99],[array[0],array[-1]], color = 'yellow')
    # plt.axis([0,99,array[0],array[-1]], color = 'black')
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()
    index = np.arange(1,array.shape[0]+1)
    n = array.shape[0]
    coef = ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))
    return coef

def getYear(year):
    ratings_url = 'http://247sports.com/Season/' + year + '-Football/CompositeTeamRankings?Conference='
    years_Ratings = []
    division_list = ['AAC', 'ACC', 'Big-12','Big-Ten','C-USA','IND','MAC', 'M-West', 'Pac-12', 'SBC', 'SEC']
    for division in division_list:
        division_url = ratings_url + division
        driver = webdriver.Chrome()
        driver.get(division_url)
        #driver.find_element_by_css_selector('#page-content > div.main-div.clearfix > section > section > section > ul > li.showmore_blk > a').click()
        #time.sleep(3)
        rating = driver.find_element_by_css_selector('#page-content > div.main-div.clearfix > section > section > section > ul')
        ratings = str(rating.text).split('\n')
        ratings = ratings[11:]
        i=0
        while i<len(ratings):
            #print ratings[i], ratings[i+6]
            years_Ratings.append(float(ratings[i+6]))
            i = i+9
        driver.quit()
    data = np.asarray(years_Ratings)
    return data

def main():
    for year in range(2008,2018):
        data = getYear(str(year))
        print year, gini(data)






if __name__ == '__main__':
    main()
