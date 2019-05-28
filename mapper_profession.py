#!/usr/bin/env python

import sys
import json
import re

prof_dict = {'movie director': ['movie director', 'film maker'], 'editor': ['editor', 'editor-in-chief', 'publisher', 'journalist'], 'lawyer': ['lawyer', 'advocate', 'attorney', 'barrister', 'solicitor', 'counsel'], 'airplane pilot': ['airplane pilot', 'pilot', 'airline pilot'], 'writer': ['writer', 'novelist', 'screenwriter'], 'salesperson': ['salesperson', 'salesman', 'vendor', 'dealer'], 'actor': ['actor', 'actress', 'comedian'], 'teacher': ['teacher', 'school teacher'], 'student': ['student', 'pupil'], 'waiter': ['waiter', 'waitress', 'bartender', 'server', 'barista'], 'housewife': ['housewife', 'homemaker'], 'psychologist': ['psychologist', 'therapist', 'psychoanalyst'], 'businessperson': ['businessperson', 'businessman', 'entrepeneur', 'merchant', 'tycoon', 'trader', 'businesswoman'], 'engineer': ['engineer', 'mechanic', 'technician', 'architect', 'plumber', 'electrician'], 'detective': ['detective'], 'journalist': ['journalist', 'reporter', 'newsman'], 'scientist': ['scientist', 'researcher'], 'policeman': ['policeman', 'cop', 'police', 'constable', 'gendarme', 'FBI agent', 'police officer'], 'clerk': ['clerk', 'secretary'], 'stewardess': ['stewardess', 'flight attendant', 'cabin attendant', 'cabin crew', 'purser'], 'doctor': ['doctor', 'physician'], 'musician': ['musician', 'pianist', 'violinist', 'singer', 'guitarist', 'drummer', 'vocalist', 'composer', 'saxophonist'], 'professor': ['professor', 'lecturer', 'academic'], 'tv presenter': ['tv presenter', 'presenter', 'radio presenter', 'announcer'], 'sportsman': ['sportsman', 'athlete', 'swimmer', 'football player', 'soccer player', 'hockey player', 'basketball player', 'baseball player', 'tennis player'], 'driver': ['driver', 'chauffeur'], 'photographer': ['photographer', 'cameraman', 'cinematographer'], 'banker': ['banker', 'stockbroker', 'broker', 'stock trader', 'daytrader'], 'painter': ['painter'], 'manager': ['manager', 'administrator', 'superintendent'], 'military personnel': ['military personnel', 'soldier', 'military officer', 'sergeant', 'trooper', 'lieutenant', 'enlisted man'], 'politician': ['politician', 'statesman', 'policy maker'], 'assistant': ['assistant'], 'priest': ['priest', 'pastor', 'preacher', 'clergyman', 'vicar'], 'unemployed': ['unemployed'], 'activist': ['activist', 'campaigner', 'militant']}

black_list = ['whowouldwin', 'wouldyourather', 'scenesfromahat', 'AskOuija', 'cosplay', 'cosplaygirls', 'DnD', 'DnDGreentext', 'DnDBehindTheScreen', 'dndnext', 'dungeonsanddragons', 'criticalrole', 'DMAcademy', 'magicTCG', 'modernmagic', 'zombies', 'cyberpunk', 'fantasy', 'scifi', 'starwars', 'startrek', 'asksciencefiction', 'prequelmemes', 'empiredidnothingwrong', 'SequelMemes', 'sciencefiction', 'DarkMatter', 'DefianceTV', 'DoctorWho', 'KilljoysTV', 'OtherSpaceTV', 'RedDwarf', 'StarWarsRebels', 'ThunderbirdsAreGo', 'Andromeda', 'Babylon5', 'Caprica', 'Farscape', 'Firefly', 'Futurama', 'LostInSpace', 'Lexx', 'Space1999', 'SpaceAboveandBeyond', 'SGA', 'DeepSpaceNine', 'StarTrekEnterprise', 'TNG', 'TheAnimatedSeries', 'TOS', 'Voyager', 'TheCloneWars', 'TheThunderbirds', 'LV426', 'BSG', 'Defiance', 'Dune', 'GalaxyQuest', 'DontPanic', 'Spaceballs', 'Stargate', 'Treknobabble', 'StarWars', 'themartian', 'Thunderbirds', 'printSF', 'ScienceFiction', 'SciFi', 'AskScienceFiction', 'movies', 'Television', 'SpaceGameJunkie', 'EliteDangerous', 'StarCitizen', 'AttackWing', 'startrekgames', 'sto', 'gaming', 'Games', 'outside', 'truegaming', 'gamernews', 'gamephysics', 'webgames', 'IndieGaming', 'patientgamers', 'AndroidGaming', 'randomactsofgaming', 'speedrun', 'gamemusic', 'emulation', 'MMORPG', 'gamecollecting', 'hitboxporn', 'gamingcirclejerk', 'gamersriseup', 'gamingdetails', 'gaming4gamers', 'retrogaming', 'GameDeals', 'steamdeals', 'PS4Deals', 'freegamesonsteam', 'shouldibuythisgame', 'nintendoswitchdeals', 'freegamefindings', 'xboxone', 'oculus', 'vive', 'paradoxplaza', 'pcmasterrace', 'pcgaming', 'gamingpc', 'steam', 'linux_gaming', 'nintendo', '3DS', 'wiiu', 'nintendoswitch', '3dshacks', 'amiibo', 'sony', 'PS3', 'playstation', 'vita', 'PSVR', 'playstationplus', 'PS4', 'PS4Deals', 'DotA2', 'starcraft', 'smashbros', 'dayz', 'civ', 'KerbalSpaceProgram', 'masseffect', 'clashofclans', 'starbound', 'heroesofthestorm', 'terraria', 'dragonage', 'citiesskylines', 'smite', 'bindingofisaac', 'eve', 'starcitizen', 'animalcrossing', 'metalgearsolid', 'elitedangerous', 'bloodborne', 'monsterhunter', 'warframe', 'undertale', 'thedivision', 'stardewvalley', 'nomansskythegame', 'totalwar', 'pathofexile', 'ClashRoyale', 'crusaderkings', 'dwarffortress', 'eu4', 'thesims', 'assassinscreed', 'playrust', 'forhonor', 'stellaris', 'kingdomhearts', 'blackdesertonline', 'factorio', 'Warhammer', 'splatoon', 'rimworld', 'Xcom', 'streetfighter', 'paydaytheheist', 'MonsterHunterWorld', 'Seaofthieves', 'cyberpunkgame', 'warhammer40k', 'paladins', 'osugame', 'spidermanps4', 'persona5', 'horizion', 'reddeadredemption', 'mountandblade', 'deadbydaylight', 'farcry', 'hoi4', 'warthunder', 'grandorder', 'divinityoriginalsin', 'escapefromtarkov', 'theexpanse', 'darkestdungeon', 'forza', 'godofwar', 'ark', 'bioshock', 'edh', 'summonerswar', 'duellinks', 'arma', 'pathfinderrpg', 'footballmanagergames', 'kingdomcome', 'subnautica', 'thelastofus', 'doom', 'jrpg', 'borderlands', 'borderlands2', 'DarkSouls', 'DarkSouls2', 'DarkSouls3', 'diablo', 'diablo3', 'elderscrollsonline', 'ElderScrolls', 'teslore', 'Skyrim', 'skyrimmods', 'fallout', 'fo4', 'fo76', 'fireemblem', 'FireEmblemHeroes', 'FortniteBR', 'Fortnite', 'FortniteBattleRoyale', 'Fortnitecompetitive', 'FortniteLeaks', 'GrandTheftAutoV', 'gtav', 'gtaonline', 'hearthstone', 'CompetitiveHS', 'customhearthstone', 'minecraft', 'feedthebeast', 'overwatch', 'competitiveoverwatch', 'overwatchuniversity', 'Overwatch_Memes', 'Overwatch_Porn', 'PUBATTLEGROUNDS', 'PUBG', 'pubgxboxone', 'pubgmobile', 'rocketleague', 'rocketleagueexchange', 'witcher', 'gwent', 'tf2', 'starwarsbattlefront', 'rainbow6', 'titanfall', 'shittyrainbow6', 'battlefield_4', 'battlefield', 'battlefield_one', 'blackops3', 'CODZombies', 'callofduty', 'WWII', 'blackops4', 'codcompetitive', 'GlobalOffensive', 'globaloffensivetrade (private)', 'csgo', 'halo', 'haloonline', 'fifa', 'nba2k', 'DestinyTheGame', 'fireteams', 'destiny2', 'leagueoflegends', 'summonerschool', 'LoLeventVODs', 'wow', 'guildwars2', 'swtor', 'ffxiv', 'FinalFantasy', 'ffxv', 'Pokemon', 'friendsafari', 'pokemontrades', 'pokemongo', 'TheSilphRoad', 'Runescape', '2007scape', 'zelda', 'breath_of_the_wild']


for line in sys.stdin:
    try:
        line = line.lower()

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
        if js['subreddit'] in black_list:
            continue
        if "\"" in js.get('selftext', '') or "\"" in js.get('body', ''):
            continue

        # 1 extract text
        txt = (js.get('selftext', '') + ' ' + js.get('body', '') + ' ' + js.get('title', '')).lower()  #
        otxt = txt

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
        line = txt


        # 3 check post len
        post_len = len([x for x in txt.split(" ") if len(x.strip().strip(".")) > 1])
        if post_len > 100 or post_len < 10:
            continue

        # 4 check pattern
        iam_pos = min([line.find(p) for p in ["i am", "i'm"] if p in line] + [sys.maxsize])
        iam_found = (iam_pos != sys.maxsize)
        prof_name = "-1"
        found_count = 0
        proof = ""
        if iam_found:
            for cat, syns in prof_dict.items():
                for prof in syns:
                    cur_pos = line.find(" " + prof + " ", iam_pos + 4, iam_pos + len(prof) + 8)
                    if cur_pos != -1 and cur_pos < sys.maxsize and line.find(" no ", iam_pos, cur_pos + 1) == -1 and line.find(" not ", iam_pos, cur_pos + 1) == -1:
                        prof_name = cat
                        found_count += 1
                        proof = line[max(0, iam_pos - 40):min(iam_pos + 60, len(line))]
        if found_count > 1:
            prof_name = "-2"

        # 5 and finally
        print(u'%s\t%s___%s' % (js["author"], prof_name, js["id"]))

    except:
        continue
