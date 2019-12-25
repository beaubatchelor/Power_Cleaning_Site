import datetime as dt
import math

def thank_you_message(first_name):
    message = { 'message' : f'Thank you for your interest {first_name}! Someone from our team will contact you shortly.'}
    return message
def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

today = dt.date.today()

olivia_age = today - dt.date(2005, 4, 1)
bennett_age = today -  dt.date(2009, 5, 19)
declan_age = today -  dt.date(2019, 5, 18)
experiance_age = today - dt.date(1998, 6, 18)

olivia_age_clean = str(int(round_down(olivia_age.days / 365, 0))) + ' years old'
bennett_age_clean = str(int(round_down(bennett_age.days / 365, 0))) + ' years old'
declan_age_clean = int(round_down(declan_age.days / 365, 0))
experiance_age_clean = str(int(round_down(experiance_age.days / 365, 0)))

if declan_age_clean == 0:
    declan_age_clean = str(int(round_down((declan_age.days / 365) * 12, 0))) + ' months old'
else:
    declan_age_clean = str(int(round_down(declan_age.days / 365, 0))) + ' years old'

blank_message = { 'message' : ''}

bio_message = {'busi_bio' : f'I have had a connection to the hood cleaning business my entire life. It started with my father who passed down not only his knowledge but the great sense of pride in completing even the smallest tasks perfectly. I have carried on that same attention to detail for {experiance_age_clean} years now and am grateful that I learned a skill early that has helped me provide for my family. Our company has intentionally stayed small in order to keep the quality of our work consistent, and I feel fortunate that I get to know and work with the caliber of people that I do.',\
'fish_bio' : 'I have a second career as a fishing guide for all of the southwest rivers in Montana. I have a strong bond with the state I call home and am reminded of it every day I am out on the water.',\
'fam_bio' : f'When I am not working I spend most of my free time with my beautiful wife Ashley and my 3 amazing children Olivia ({olivia_age_clean}), Bennett ({bennett_age_clean}), and Declan ({declan_age_clean}). Olivia raised her second hog for 4-h this year and is planning her third, Bennett is currently interested in all manner of sports and is dynamite on the soccer field, and Baby Declan’s stoicism continues to teach us how the world is meant to be experienced, lessons I pay for in diaper changes and lack of sleep. My wife has her bachelors in health and human performance and is a runner, hiker, yogi, and an everlasting support system for the entire family.'}