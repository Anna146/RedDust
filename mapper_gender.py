#!/usr/bin/env python

import sys
import json
import re

male_list = ["man", "male", "boy", "husband", "father", "brother"]
female_list = ["woman", "female", "girl", "lady", "wife", "mother", "sister"]
black_list = ['whowouldwin', 'wouldyourather', 'scenesfromahat', 'AskOuija', 'cosplay', 'cosplaygirls', 'DnD', 'DnDGreentext', 'DnDBehindTheScreen', 'dndnext', 'dungeonsanddragons', 'criticalrole', 'DMAcademy', 'magicTCG', 'modernmagic', 'zombies', 'cyberpunk', 'fantasy', 'scifi', 'starwars', 'startrek', 'asksciencefiction', 'prequelmemes', 'empiredidnothingwrong', 'SequelMemes', 'sciencefiction', 'DarkMatter', 'DefianceTV', 'DoctorWho', 'KilljoysTV', 'OtherSpaceTV', 'RedDwarf', 'StarWarsRebels', 'ThunderbirdsAreGo', 'Andromeda', 'Babylon5', 'Caprica', 'Farscape', 'Firefly', 'Futurama', 'LostInSpace', 'Lexx', 'Space1999', 'SpaceAboveandBeyond', 'SGA', 'DeepSpaceNine', 'StarTrekEnterprise', 'TNG', 'TheAnimatedSeries', 'TOS', 'Voyager', 'TheCloneWars', 'TheThunderbirds', 'LV426', 'BSG', 'Defiance', 'Dune', 'GalaxyQuest', 'DontPanic', 'Spaceballs', 'Stargate', 'Treknobabble', 'StarWars', 'themartian', 'Thunderbirds', 'printSF', 'ScienceFiction', 'SciFi', 'AskScienceFiction', 'movies', 'Television', 'SpaceGameJunkie', 'EliteDangerous', 'StarCitizen', 'AttackWing', 'startrekgames', 'sto', 'gaming', 'Games', 'outside', 'truegaming', 'gamernews', 'gamephysics', 'webgames', 'IndieGaming', 'patientgamers', 'AndroidGaming', 'randomactsofgaming', 'speedrun', 'gamemusic', 'emulation', 'MMORPG', 'gamecollecting', 'hitboxporn', 'gamingcirclejerk', 'gamersriseup', 'gamingdetails', 'gaming4gamers', 'retrogaming', 'GameDeals', 'steamdeals', 'PS4Deals', 'freegamesonsteam', 'shouldibuythisgame', 'nintendoswitchdeals', 'freegamefindings', 'xboxone', 'oculus', 'vive', 'paradoxplaza', 'pcmasterrace', 'pcgaming', 'gamingpc', 'steam', 'linux_gaming', 'nintendo', '3DS', 'wiiu', 'nintendoswitch', '3dshacks', 'amiibo', 'sony', 'PS3', 'playstation', 'vita', 'PSVR', 'playstationplus', 'PS4', 'PS4Deals', 'DotA2', 'starcraft', 'smashbros', 'dayz', 'civ', 'KerbalSpaceProgram', 'masseffect', 'clashofclans', 'starbound', 'heroesofthestorm', 'terraria', 'dragonage', 'citiesskylines', 'smite', 'bindingofisaac', 'eve', 'starcitizen', 'animalcrossing', 'metalgearsolid', 'elitedangerous', 'bloodborne', 'monsterhunter', 'warframe', 'undertale', 'thedivision', 'stardewvalley', 'nomansskythegame', 'totalwar', 'pathofexile', 'ClashRoyale', 'crusaderkings', 'dwarffortress', 'eu4', 'thesims', 'assassinscreed', 'playrust', 'forhonor', 'stellaris', 'kingdomhearts', 'blackdesertonline', 'factorio', 'Warhammer', 'splatoon', 'rimworld', 'Xcom', 'streetfighter', 'paydaytheheist', 'MonsterHunterWorld', 'Seaofthieves', 'cyberpunkgame', 'warhammer40k', 'paladins', 'osugame', 'spidermanps4', 'persona5', 'horizion', 'reddeadredemption', 'mountandblade', 'deadbydaylight', 'farcry', 'hoi4', 'warthunder', 'grandorder', 'divinityoriginalsin', 'escapefromtarkov', 'theexpanse', 'darkestdungeon', 'forza', 'godofwar', 'ark', 'bioshock', 'edh', 'summonerswar', 'duellinks', 'arma', 'pathfinderrpg', 'footballmanagergames', 'kingdomcome', 'subnautica', 'thelastofus', 'doom', 'jrpg', 'borderlands', 'borderlands2', 'DarkSouls', 'DarkSouls2', 'DarkSouls3', 'diablo', 'diablo3', 'elderscrollsonline', 'ElderScrolls', 'teslore', 'Skyrim', 'skyrimmods', 'fallout', 'fo4', 'fo76', 'fireemblem', 'FireEmblemHeroes', 'FortniteBR', 'Fortnite', 'FortniteBattleRoyale', 'Fortnitecompetitive', 'FortniteLeaks', 'GrandTheftAutoV', 'gtav', 'gtaonline', 'hearthstone', 'CompetitiveHS', 'customhearthstone', 'minecraft', 'feedthebeast', 'overwatch', 'competitiveoverwatch', 'overwatchuniversity', 'Overwatch_Memes', 'Overwatch_Porn', 'PUBATTLEGROUNDS', 'PUBG', 'pubgxboxone', 'pubgmobile', 'rocketleague', 'rocketleagueexchange', 'witcher', 'gwent', 'tf2', 'starwarsbattlefront', 'rainbow6', 'titanfall', 'shittyrainbow6', 'battlefield_4', 'battlefield', 'battlefield_one', 'blackops3', 'CODZombies', 'callofduty', 'WWII', 'blackops4', 'codcompetitive', 'GlobalOffensive', 'globaloffensivetrade (private)', 'csgo', 'halo', 'haloonline', 'fifa', 'nba2k', 'DestinyTheGame', 'fireteams', 'destiny2', 'leagueoflegends', 'summonerschool', 'LoLeventVODs', 'wow', 'guildwars2', 'swtor', 'ffxiv', 'FinalFantasy', 'ffxv', 'Pokemon', 'friendsafari', 'pokemontrades', 'pokemongo', 'TheSilphRoad', 'Runescape', '2007scape', 'zelda', 'breath_of_the_wild']

for line in sys.stdin:
    try:
        line = line

        # 0 load json
        try:
            js = json.loads(line)
        except:
            continue
        if not isinstance(js, dict):
            continue
        if 'author' not in js or 'subreddit' not in js or js['author'] == '[deleted]' or js['author'] == "":
            continue
        if 'selftext' not in js and 'body' not in js:
            continue
        if len((js.get('selftext', '') + js.get('body', '')).strip()) == 0:
            continue
        if 'subreddit' not in js:
            continue
        if js['subreddit'].lower() in black_list:
            continue
        if "\"" in js.get('selftext', '') or "\"" in js.get('body', ''):
            continue

        # 1 extract text
        txt = (js.get('selftext', '') + ' ' + js.get('body', '') + ' ' + js.get('title', ''))

        original_txt = txt
        txt = txt.lower()

        pattern = re.compile('#[\w]*')
        txt = pattern.sub(' ', txt)
        pattern = re.compile('[\w]*@[\w]*')
        txt = pattern.sub(' ', txt)
        txt = re.sub(r'https?:\/\/.*[\r\n]*', '', txt)

        pattern = re.compile('([^\s\w\']|_)+|\d|\t|\n')
        txt = pattern.sub(' ', txt)
        pattern = re.compile('\s+')
        txt = pattern.sub(" ", txt)
        pattern = re.compile('\.+')
        txt = pattern.sub(".", txt)

        # 3 check post len
        post_len = len([x for x in txt.split(" ") if len(x.strip().strip(".")) > 1])
        if post_len > 100 or post_len < 10:
            continue
        line = line.lower()
        gender_name = "-1"

        # 4 check pattern
        iam_pos = min([line.find(p) for p in ["i am a", "i'm a"] if p in line] + [sys.maxsize])
        iam_found = (iam_pos != sys.maxsize)
        gender_name = "-1"

        if iam_found:
            for itm in male_list:
                if line.find(" " + itm + " ", iam_pos + 3, iam_pos + len(itm) + 12) != -1:
                    gender_name = "m"
                    break
            for itm in female_list:
                if line.find(" " + itm + " ", iam_pos + 3, iam_pos + len(itm) + 12) != -1:
                    if gender_name == "m":
                        gender_name = "-2"
                    else:
                        gender_name = "f"

        pattern = re.compile(r"(?:i|i'm|me)\s*\(\s*(\d+)\s*(m|f)\s*\)")  # for round brackets
        pattern1 = re.compile(r"(?:i|i'm|me)\s*\[\s*(\d+)\s*(m|f)\s*\]")  # for square brackets
        lst = pattern.findall(line)
        lst1 = pattern1.findall(line)
        right_after = ""
        for it in lst:
            if gender_name != "-1":
                gender_name = it[1] if it[1] == gender_name else "-2"
            else:
                gender_name = it[1]
        for it in lst1:
            if gender_name != "-1":
                gender_name = it[1] if it[1] == gender_name else "-2"
            else:
                gender_name = it[1]

        # 5 and finally
        print(u'%s\t%s___%s' % (js["author"], gender_name, js["id"]))
    except:
        continue
