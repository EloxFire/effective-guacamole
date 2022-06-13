# Effective Guacamole Script
# Version: 1.0
# Date: 2020-01-01
# Author: @EloxFire
# Description: This script help you choose what to cook based on what's in your fridge.

import requests
import colorama
from colorama import Fore

available_meal_types = ["Breakfast", "Lunch", "Dinner"]
available_cuisine_types = ["American", "Asian", "Bristish", "Caribbean", "Central Europe", "Chinese", "Eastern Europe", "French", "Indian", "Italian", "Japanise", "Kosher", " Mediterranean", "Mexican", "Middle Eastern", "Nordic", "South American", "South East Asian"]
available_dish_types = ["Biscuits and cookies",  "Bread, Cereals",  "Condiments and sauces",  "Dessert", "Drinks", "Main course", "Pancake", "Preps", "Preserve", "Salad", "Sandwiches", "Side dish", "Soups", "Starter", "Sweets"]


def start():
    print("\n" + Fore.CYAN + "-===  " + "Welcome to Effective Guacamole!  ===-")
    print("This script will help you choose what to cook based on what's in your fridge.\n" + Fore.RESET)

    print("Please choose a meal type :")
    for i in range(len(available_meal_types)):
        print(' '.join(available_meal_types))
    # meal_type = input("Your choice : ")

    # print("\nPlease choose a cuisine type :")
    # print("[0] - American, [1] - Asian, [2] - Bristish, [3] - Caribbean, [4] - Central Europe, [5] - Chinese, [6] - Eastern Europe, [7] - French, [8] - Indian, [9] - Italian, [10] - Japanise, [11] - Kosher, [12] - Mediterranean, [13] - Mexican, [14] - Middle Eastern, [15] - Nordic, [16] - South American, [17] - South East Asian")
    # cuisine_type = input("Your choice : ")
    # print("\nPlease choose a dish type :")
    # print("[0] - Biscuits and cookies, [1] - Bread, [2] - Cereals, [3] - Condiments and sauces, [4] - Dessert, [5] - Drinks, [6] - Main course, [7] - Pancake, [8] - Preps, [9] - Preserve, [10] - Salad, [11] - Sandwiches, [12] - Side dish, [13] - Soups, [14] - Starter, [15] - Sweets")
    # dish_type = input("Your choice : ")
    # print("\nYou have chosen : " + Fore.CYAN + meal_type + " " + cuisine_type + " " + dish_type + Fore.RESET)


start()


# ingredient = input("What's in your fridge?")

# response = requests.get(
#     "https://api.edamam.com/api/recipes/v2?type=public&beta=false&q=" + ingredient + "&app_id=bec4ba3b&app_key=93e2d9babbfc42a6d936ae7b5a057471&cuisineType=Central%20Europe&mealType=Dinner")

# print(response.json())
