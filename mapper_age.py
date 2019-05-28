#!/usr/bin/env python

import sys
import json
import re

black_list = ['whowouldwin', 'wouldyourather', 'scenesfromahat', 'AskOuija', 'cosplay', 'cosplaygirls', 'DnD', 'DnDGreentext', 'DnDBehindTheScreen', 'dndnext', 'dungeonsanddragons', 'criticalrole', 'DMAcademy', 'magicTCG', 'modernmagic', 'zombies', 'cyberpunk', 'fantasy', 'scifi', 'starwars', 'startrek', 'asksciencefiction', 'prequelmemes', 'empiredidnothingwrong', 'SequelMemes', 'sciencefiction', 'DarkMatter', 'DefianceTV', 'DoctorWho', 'KilljoysTV', 'OtherSpaceTV', 'RedDwarf', 'StarWarsRebels', 'ThunderbirdsAreGo', 'Andromeda', 'Babylon5', 'Caprica', 'Farscape', 'Firefly', 'Futurama', 'LostInSpace', 'Lexx', 'Space1999', 'SpaceAboveandBeyond', 'SGA', 'DeepSpaceNine', 'StarTrekEnterprise', 'TNG', 'TheAnimatedSeries', 'TOS', 'Voyager', 'TheCloneWars', 'TheThunderbirds', 'LV426', 'BSG', 'Defiance', 'Dune', 'GalaxyQuest', 'DontPanic', 'Spaceballs', 'Stargate', 'Treknobabble', 'StarWars', 'themartian', 'Thunderbirds', 'printSF', 'ScienceFiction', 'SciFi', 'AskScienceFiction', 'movies', 'Television', 'SpaceGameJunkie', 'EliteDangerous', 'StarCitizen', 'AttackWing', 'startrekgames', 'sto', 'gaming', 'Games', 'outside', 'truegaming', 'gamernews', 'gamephysics', 'webgames', 'IndieGaming', 'patientgamers', 'AndroidGaming', 'randomactsofgaming', 'speedrun', 'gamemusic', 'emulation', 'MMORPG', 'gamecollecting', 'hitboxporn', 'gamingcirclejerk', 'gamersriseup', 'gamingdetails', 'gaming4gamers', 'retrogaming', 'GameDeals', 'steamdeals', 'PS4Deals', 'freegamesonsteam', 'shouldibuythisgame', 'nintendoswitchdeals', 'freegamefindings', 'xboxone', 'oculus', 'vive', 'paradoxplaza', 'pcmasterrace', 'pcgaming', 'gamingpc', 'steam', 'linux_gaming', 'nintendo', '3DS', 'wiiu', 'nintendoswitch', '3dshacks', 'amiibo', 'sony', 'PS3', 'playstation', 'vita', 'PSVR', 'playstationplus', 'PS4', 'PS4Deals', 'DotA2', 'starcraft', 'smashbros', 'dayz', 'civ', 'KerbalSpaceProgram', 'masseffect', 'clashofclans', 'starbound', 'heroesofthestorm', 'terraria', 'dragonage', 'citiesskylines', 'smite', 'bindingofisaac', 'eve', 'starcitizen', 'animalcrossing', 'metalgearsolid', 'elitedangerous', 'bloodborne', 'monsterhunter', 'warframe', 'undertale', 'thedivision', 'stardewvalley', 'nomansskythegame', 'totalwar', 'pathofexile', 'ClashRoyale', 'crusaderkings', 'dwarffortress', 'eu4', 'thesims', 'assassinscreed', 'playrust', 'forhonor', 'stellaris', 'kingdomhearts', 'blackdesertonline', 'factorio', 'Warhammer', 'splatoon', 'rimworld', 'Xcom', 'streetfighter', 'paydaytheheist', 'MonsterHunterWorld', 'Seaofthieves', 'cyberpunkgame', 'warhammer40k', 'paladins', 'osugame', 'spidermanps4', 'persona5', 'horizion', 'reddeadredemption', 'mountandblade', 'deadbydaylight', 'farcry', 'hoi4', 'warthunder', 'grandorder', 'divinityoriginalsin', 'escapefromtarkov', 'theexpanse', 'darkestdungeon', 'forza', 'godofwar', 'ark', 'bioshock', 'edh', 'summonerswar', 'duellinks', 'arma', 'pathfinderrpg', 'footballmanagergames', 'kingdomcome', 'subnautica', 'thelastofus', 'doom', 'jrpg', 'borderlands', 'borderlands2', 'DarkSouls', 'DarkSouls2', 'DarkSouls3', 'diablo', 'diablo3', 'elderscrollsonline', 'ElderScrolls', 'teslore', 'Skyrim', 'skyrimmods', 'fallout', 'fo4', 'fo76', 'fireemblem', 'FireEmblemHeroes', 'FortniteBR', 'Fortnite', 'FortniteBattleRoyale', 'Fortnitecompetitive', 'FortniteLeaks', 'GrandTheftAutoV', 'gtav', 'gtaonline', 'hearthstone', 'CompetitiveHS', 'customhearthstone', 'minecraft', 'feedthebeast', 'overwatch', 'competitiveoverwatch', 'overwatchuniversity', 'Overwatch_Memes', 'Overwatch_Porn', 'PUBATTLEGROUNDS', 'PUBG', 'pubgxboxone', 'pubgmobile', 'rocketleague', 'rocketleagueexchange', 'witcher', 'gwent', 'tf2', 'starwarsbattlefront', 'rainbow6', 'titanfall', 'shittyrainbow6', 'battlefield_4', 'battlefield', 'battlefield_one', 'blackops3', 'CODZombies', 'callofduty', 'WWII', 'blackops4', 'codcompetitive', 'GlobalOffensive', 'globaloffensivetrade (private)', 'csgo', 'halo', 'haloonline', 'fifa', 'nba2k', 'DestinyTheGame', 'fireteams', 'destiny2', 'leagueoflegends', 'summonerschool', 'LoLeventVODs', 'wow', 'guildwars2', 'swtor', 'ffxiv', 'FinalFantasy', 'ffxv', 'Pokemon', 'friendsafari', 'pokemontrades', 'pokemongo', 'TheSilphRoad', 'Runescape', '2007scape', 'zelda', 'breath_of_the_wild']

for line in sys.stdin:
    try:
        # 0 load json
        try:
            js = json.loads(line)
        except:
            continue
        if not isinstance(js, dict):
            continue

        # 0 sanity check
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
        txt = (js.get('selftext', '') + ' ' + js.get('body', '') + ' ' + js.get('title', ''))  #
        original_txt = txt
        txt = txt.lower()

        pattern = re.compile('#[\w]*')
        txt = pattern.sub(' ', txt)
        pattern = re.compile('[\w]*@[\w]*')
        txt = pattern.sub(' ', txt)
        txt = re.sub(r'https?:\/\/.*[\r\n]*', ' ', txt)

        pattern = re.compile('([^\s\w\'/]|_)+|\t|\n')
        txt = pattern.sub(' ', txt)
        pattern = re.compile('\s+')
        txt = pattern.sub(" ", txt)
        pattern = re.compile('\.+')
        txt = pattern.sub(".", txt)
        line = txt


        # 3 check post len
        post_len = len([x for x in txt.split(" ") if len(x.strip().strip(".")) > 1])
        if post_len > 100 or post_len < 10:
            continue

        # 4 check pattern
        ## get current date for age calculation
        import time
        curr_year = 2017
        if "created_utc" in js:
            try:
                curr_year = int(time.gmtime(js["created_utc"]).tm_year)
            except:
                pass
        age = "-1"
        proof = ""

        ## check 4-digit year and "80s"
        born_pos = min([line.find(p) for p in ["i am born in ", "i'm born in", "i was born in "] if p in line] + [sys.maxsize])#line.find("i was born in ")
        if born_pos != sys.maxsize:
            if_pos = line.find("if ", max(0, born_pos - 20), born_pos)
            if if_pos == -1:
                pieces = [x for x in line[born_pos + 7:min(born_pos + 30, len(line))].split(" ")]
                born_year = ""
                for piece in pieces:
                    if piece[-1] == "s":
                        born_year = "".join(x for x in piece if x.isdigit())
                if born_year != "":
                    try:
                        born_year = int(born_year)
                        if len(str(born_year)) == 2:
                            if born_year in [40, 50, 60, 70, 80, 90]:
                                born_year = 1900 + born_year
                            elif born_year in [00, 10]:
                                born_year = 2000 + born_year
                    except:
                        born_year = ""
                if born_year == "":
                    born_year = "".join(x for x in line[born_pos + 7:born_pos + 20].split(" ") if x.isdigit())
                    try:
                        born_year = int(born_year)
                    except:
                        born_year = ""
                if born_year != "" and born_year > 1910 and born_year < 2015:
                    age = str(curr_year - born_year)
                    proof = line[max(0,born_pos - 40):min(born_pos + 60, len(line))]
                else:
                    age = "-1"

        ## check "born on date"
        born_pos = min([line.find(p) for p in ["i am born on ", "i'm born on", "i was born on "] if p in line] + [sys.maxsize])
        if born_pos != sys.maxsize:
            if_pos = line.find("if ", max(0, born_pos - 20), born_pos)
            if if_pos == -1:
                pieces = [x for x in line[born_pos + 7:min(born_pos + 35, len(line))].split(" ") if any(y.isdigit() for y in x)]
                try:
                    born_year = int(pieces[1])
                except:
                    born_year = -1
                if born_year != -1:
                    age = str(curr_year - born_year)
                    proof = line[max(0, born_pos - 40):min(born_pos + 60, len(line))]
                else:
                    age  = "-1"

        if int(age) < 5 or int(age) > 100:
            age = "-1"

        ## check "years old"
        if age == "-1":
            iam_pos = min([line.find(p) for p in ["i am", "i'm"] if p in line] + [sys.maxsize])
            iam_found = (iam_pos != sys.maxsize)
            years_len = 0
            years_pos = 0
            if iam_found:
                if_pos = line.find("if ", max(0, iam_pos - 20), iam_pos + 1)
                before_pos = line.find("before", max(0, iam_pos - 20), iam_pos + 1)
                if if_pos == -1 and before_pos == -1:
                    years_pos_len = min([(line.find(p, iam_pos + 3, iam_pos + 8 + len(p)), len(p)) for p in ["years of age", "yoa", "yo ", "y/o"] if p in line[iam_pos + 3: iam_pos + 8 + len(p)]] + [(sys.maxsize, 0)], key=lambda x: x[0])
                    years_pos = years_pos_len[0]
                    years_len = years_pos_len[1]
                    if years_pos != sys.maxsize:
                        curr_age = "".join(x for x in line[iam_pos:years_pos].split(" ") if x.isdigit())
                        #right_after = line[years_pos+years_len-2:].split(' ')[1]
                        age = str(curr_age)
                        proof = original_txt[max(0, iam_pos - 40):min(iam_pos + 60, len(original_txt))]

                    if age == "-1":
                        exp_num = "".join([x for x in line[iam_pos + 3:iam_pos + 6] if x.isdigit()])
                        try:
                            found_num = original_txt.find(exp_num)
                            if int(exp_num) < 10:
                                found_num = -1
                            if found_num != -1 and (found_num + 3 > len(original_txt) or
                                                    original_txt[found_num + 2] in [".", ",", "\n", ";"] or
                                                    original_txt[found_num:found_num + 8].split(" ")[1] in ["but", "and"]):
                                age = str(exp_num)
                                proof = str(if_pos) + original_txt[max(0, iam_pos - 40):min(iam_pos + 60, len(original_txt))]
                        except:
                            age = "-1"

        if int(age) < 13 or int(age) > 100:
            age = "-1"

        age_name = age

        # brackets

        pattern = re.compile(r"(?:i|i'm|me)\s*\(\s*(\d+)\s*(m|f)\s*\)")  # for round brackets
        pattern1 = re.compile(r"(?:i|i'm|me)\s*\[\s*(\d+)\s*(m|f)\s*\]")  # for square brackets
        lst = pattern.findall(original_txt)
        lst1 = pattern1.findall(original_txt)
        for it in lst:
            try:
                age = int(it[0])
                if age > 5 and age < 100:
                    if int(age_name) < age:
                        age_name = it[0]
            except:
                continue
        for it in lst1:
            try:
                age = int(it[0])
                if age > 5 and age < 100:
                    if int(age_name) < age:
                        age_name = it[0]
            except:
                continue


        age = age_name

        # 5 and finally
        print(u'%s\t%s___%s' % (js["author"], age, js["id"]))
    except:
        continue
