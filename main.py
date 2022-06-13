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


def selection():
    print("\n" + Fore.CYAN + "-===  " + "Welcome to Effective Guacamole!  ===-")
    print("This script will help you choose what to cook based on what's in your fridge.\n" + Fore.RESET)

    print("Please choose a meal type :")
    for i in range(len(available_meal_types)):
        print(" [" + str(i) + "] " + ''.join(available_meal_types[i]))
    meal_type = input("Your choice : ")

    print("\nPlease choose a cuisine type :")
    for i in range(len(available_cuisine_types)):
        print(" [" + str(i) + "] " + ''.join(available_cuisine_types[i]))
    cuisine_type = input("Your choice : ")

    print("\nPlease choose a dish type :")
    for i in range(len(available_dish_types)):
        print(" [" + str(i) + "] " + ''.join(available_dish_types[i]))
    dish_type = input("Your choice : ")
    print("\nYou have chosen : " + Fore.CYAN + available_meal_types[int(meal_type)] + " - " + available_cuisine_types[int(cuisine_type)] + " - " + available_dish_types[int(dish_type)] + Fore.RESET)
    choice = input("\nConfirm your choice ? (y/n) : ")

    if choice == "y":
        print("\n" + Fore.CYAN + "Searching..." + Fore.RESET)
    else:
        print("\n" + Fore.RED + "Aborting..." + Fore.RESET)
        exit()


def start():
    selection()


start()


# ingredient = input("What's in your fridge?")

# response = requests.get(
#     "https://api.edamam.com/api/recipes/v2?type=public&beta=false&q=" + ingredient + "&app_id=bec4ba3b&app_key=93e2d9babbfc42a6d936ae7b5a057471&cuisineType=Central%20Europe&mealType=Dinner")

# print(response.json())
