# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 19:35:45 2022

@author: User01

"""

"""
Example:
Get all cards on the TCG Banlist who are level 4 and order them by name (A-Z)

https://db.ygoprodeck.com/api/v7/cardinfo.php?banlist=tcg&level=4&sort=name
Get all Dark attribute monsters from

Split things into name, archetpye, number available

#ban_json = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php?banlist=TCG")

# of format {"data":[{card1}, {card2}, ...]}
#{card1} has keys ['id', 'name', 'type', 'desc', 'race', 'archetype', 'card_sets', 'card_images', 'card_prices']
#banlist_info is only a field on F&L cards
{'ban_tcg': 'Semi-Limited', 'ban_ocg': 'Limited'}

https://docs.google.com/spreadsheets/d/1nMsM65XH8koKH3_EC7WAjt_Q03eIM3-SrpMkwtPWc1E
"""

import requests
import json
import pandas as pd
import random

random.seed(0)

cards_json = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
data = json.loads(cards_json.text)
df = pd.DataFrame(data["data"])

random_banning = [3*random.randint(0,1) for i in range(df.shape[0])]
df["usable"] = random_banning

#limited_dict = {"Limited":1, "Banned":0, "Semi-Limited":2}

df.loc[df['banlist_info'].notnull(), "usable"] = 0

df_sheet = df[["name", "archetype", "usable"]]

df_sheet.to_csv('ygo_banlist.csv')