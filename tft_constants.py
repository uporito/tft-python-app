from Unit import Unit
from Synergy import Synergy

### ALL UNITS ###

# 1-COST #
ASHE             = Unit("Ashe"          , 1, ["LaserCorps", "Recon"])
BLITZCRANK       = Unit("Blitzcrank"    , 1, ["A.D.M.I.N", "Brawler"])
GALIO            = Unit("Galio"         , 1, ["Civilian", "Mascot"])
GANGPLANK        = Unit("Gangplank"     , 1, ["Supers", "Duelist"])
KAYLE            = Unit("Kayle"         , 1, ["Underground", "Duelist"])
LULU             = Unit("Lulu"          , 1, ["Gadgeteen", "Heart"])
LUX              = Unit("Lux"           , 1, ["Star Guardian", "Spellslinger"])
NASUS            = Unit("Nasus"         , 1, ["Anima Squad", "Mascot"])
POPPY            = Unit("Poppy"         , 1, ["Gadgeteen", "Defender"])
RENEKTON         = Unit("Renekton"      , 1, ["LaserCorps", "Brawler"])
SYLAS            = Unit("Sylas"         , 1, ["Renegade", "Anima Squad"])
TALON            = Unit("Talon"         , 1, ["Renegade", "Ox Force"])
WUKONG           = Unit("Wukong"        , 1, ["Mecha: PRIME", "Defender"])

# 2-COST #
ANNIE            = Unit("Annie"         , 2, ["Gadgeteen", "Spellslinger", "Ox Force"])
CAMILLE          = Unit("Camile"        , 2, ["A.D.M.I.N", "Renegade"])
DRAVEN           = Unit("Draven"        , 2, ["Mecha: PRIME", "Ace"])
EZREAL           = Unit("Ezreal"        , 2, ["Underground", "Recon"])
FIORA            = Unit("Fiora"         , 2, ["Ox Force", "Duelist"])
JINX             = Unit("Jinx"          , 2, ["Anima Squad", "Prankster"])
LEE_SIN          = Unit("Lee Sin"       , 2, ["Heart", "Brawler"])
MALPHITE         = Unit("Malphite"      , 2, ["Supers", "Mascot"])
RELL             = Unit("Rell"          , 2, ["Star Guardian", "Defender"])
SIVIR            = Unit("Sivir"         , 2, ["Civilian", "Sureshot"])
VI               = Unit("Vi"            , 2, ["Underground", "Brawler"])
YASUO            = Unit("Yasuo"         , 2, ["LaserCorps", "Duelist"])
YUUMI            = Unit("Yuumi"         , 2, ["Star Guardian", "Heart", "Mascot"])

# 3-COST #
ALISTAR          = Unit("Alistar"       , 3, ["Ox Force", "Aegis", "Mascot"])
CHO_GATH         = Unit("Cho'Gath"      , 3, ["Threat"])
JAX              = Unit("Jax"           , 3, ["Mecha: PRIME", "Brawler"])
KAI_SA           = Unit("Kai'Sa"        , 3, ["Star Guardian", "Recon"])
LEBLANC          = Unit("LeBlanc"       , 3, ["Hacker", "Spellslinger"])
NILAH            = Unit("Nilah"         , 3, ["Star Guardian", "Duelist"])
RAMMUS           = Unit("Rammus"        , 3, ["Threat"])
RIVEN            = Unit("Riven"         , 3, ["Anima Squad", "Brawler", "Defender"])
SENNA            = Unit("Senna"         , 3, ["LaserCorps", "Sureshot"])
SONA             = Unit("Sona"          , 3, ["Underground", "Spellslinger", "Heart"])
VAYNE            = Unit("Vayne"         , 3, ["Anima Squad", "Recon", "Duelist"])
VEL_KOZ          = Unit("Vel'Koz"       , 3, ["Threat"])
ZOE              = Unit("Zoe"           , 3, ["Gadgeteen", "Prankster", "Hacker"])

# 4-COST #
AURELION_SOL     = Unit("Aurelion Sol"  , 4, ["Threat"])
BEL_VETH         = Unit("Bel'Veth"      , 4, ["Threat"])
EKKO             = Unit("Ekko"          , 4, ["Prankster", "Aegis"])
MISS_FORTUNE     = Unit("Miss Fortune"  , 4, ["Anima Squad", "Ace"])
SAMIRA           = Unit("Samira"        , 4, ["Underground", "Sureshot", "Ace"])
SEJUANI          = Unit("Sejuani"       , 4, ["LaserCorps", "Brawler"])
SETT             = Unit("Sett"          , 4, ["Mecha: PRIME", "Defender"])
SORAKA           = Unit("Soraka"        , 4, ["A.D.M.I.N", "Heart"])
TALIYAH          = Unit("Taliyah"       , 4, ["Star Guardian", "Spellslinger"])
VIEGO            = Unit("Viego"         , 4, ["Ox Force", "Renegade"])
ZAC              = Unit("Zac"           , 4, ["Threat"])
ZED              = Unit("Zed"           , 4, ["LaserCorps", "Duelist"])

# 5-COST #
APHELIOS         = Unit("Aphelios"      , 5, ["Arsenal", "Ox Force", "Sureshot"])
FIDDLESTICKS     = Unit("Fiddlesticks"  , 5, ["Threat"])
JANNA            = Unit("Janna"         , 5, ["Forecaster", "Civilian", "Spellslinger"])
LEONA            = Unit("Leona"         , 5, ["Mecha: PRIME", "Aegis"])
MORDEKAISER      = Unit("Mordekaiser"   , 5, ["LaserCorps", "Ace"])
NUNU_WILLUMP     = Unit("Nunu & Willump", 5, ["Gadgeteen", "Mascot"])
SYNDRA           = Unit("Syndra"        , 5, ["Star Guardian", "Heart"])
URGOT            = Unit("Urgot"         , 5, ["Threat"])

SET_8_UNITS = [ASHE, BLITZCRANK, GALIO, GANGPLANK, KAYLE, LULU, LUX, NASUS, POPPY, RENEKTON, SYLAS, TALON, WUKONG, ANNIE, CAMILLE, DRAVEN, EZREAL, FIORA, JINX, LEE_SIN, MALPHITE, RELL, SIVIR, VI, YASUO, YUUMI, ALISTAR, JAX, KAI_SA, LEBLANC, NILAH, RIVEN, SENNA, SONA, VAYNE, ZOE, EKKO, MISS_FORTUNE, SAMIRA, SEJUANI, SETT, SORAKA, TALIYAH, VIEGO, ZED, APHELIOS, FIDDLESTICKS, JANNA, LEONA, MORDEKAISER, NUNU_WILLUMP, SYNDRA]

## SYNERGY LEVELS DICT ###
synergy_levels = {
    "A.D.M.I.N"         : [2, 4, 6],
    "Anima Squad"       : [3, 5, 7],
    "Arsenal"           : [1],
    "Civilian"          : [1],
    "Gadgeteen"         : [3, 5],
    "LaserCorps"        : [3, 6, 9],
    "Mecha: PRIME"      : [3, 5],
    "Ox Force"          : [2, 4, 6, 8],
    "Star Guardian"     : [3, 5, 7, 9],
    "Supers"            : [3],
    "Threat"            : [0],
    "Underground"       : [3, 5],
    "Ace"               : [1, 0, 4],
    "Aegis"             : [2, 3, 4, 5],
    "Brawler"           : [2, 4, 6, 8],
    "Corrupted"         : [1],
    "Defender"          : [2, 4, 6],
    "Duelist"           : [2, 4, 6, 8],
    "Forecaster"        : [1],
    "Hacker"            : [2, 3, 4],
    "Heart"             : [2, 4, 6, 8],
    "Mascot"            : [2, 4, 6],
    "Prankster"         : [2, 3, 4],
    "Recon"             : [2, 3, 4],
    "Renegade"          : [2, 4, 6],
    "Spellslinger"      : [2, 4, 6],
    "Sureshot"          : [2, 4]
}

### ALL SYNERGIES ###

ADMIN           = Synergy("A.D.M.I.N"         , ["Blitzcrank", "Camille", "Leblanc", "Soraka"],                     [2, 4, 6])
ANIMA_SQUAD     = Synergy("Anima Squad"       , ["Nasus", "Sylas", "Jinx", "Riven", "Vayne", "Miss Fortune"], [3, 5, 7])
ARSENAL         = Synergy("Arsenal"           , ["Aphelios"], [1])
CIVILIAN        = Synergy("Civilian"          , ["Galio", "Sivir", "Janna"], [1])
GADGETEEN       = Synergy("Gadgeteen"         , ["Lulu", "Poppy", "Annie", "Zoe", "Nunu & Willump"], [3, 5])
LASERCORPS      = Synergy("LaserCorps"        , ["Ashe", "Renekton", "Yasuo", "Senna", "Sejuani", "Zed", "Mordekaiser"], [3, 6, 9])
MECHA_PRIME     = Synergy("Mecha: PRIME"      , ["Wukong", "Draven", "Jax", "Sett", "Leona"], [3, 5])
OX_FORCE        = Synergy("Ox Force"          , ["Talon", "Annie", "Fiora", "Alistar", "Viego", "Aphelios"], [2, 4, 6, 8])
STAR_GUARDIAN   = Synergy("Star Guardian"     , ["Lux", "Rell", "Yuumi", "Kai'sa", "Nilah", "Ekko", "Taliyah", "Syndra"],   [3, 5, 7, 9])
SUPERS          = Synergy("Supers"            , ["Gangplank", "Lee Sin", "Malphite"], [3])
THREAT          = Synergy("Threat"            , ["Vel'Koz", "Cho'gath", "Ramus", "Bel'Veth", "Zac", "Aurelion Sol", "Urgot", "Fiddlesticks"], [0])
UNDERGROUND     = Synergy("Underground"       , ["Kayle", "Ezreal", "Vi", "Sona", "Samira"], [3, 5])
ACE             = Synergy("Ace"               , ["Draven", "Miss Fortune", "Samira", "Mordekaiser"], [1, 0, 4])
AEGIS           = Synergy("Aegis"             , ["Vi", "Alistar", "Ekko", "Leona"], [2, 3, 4, 5])
BRAWLER         = Synergy("Brawler"           , ["Blitzcrank", "Renekton", "Lee Sin", "Vi", "Jax", "Riven", "Sejuani"], [2, 4, 6, 8])
CORRUPTED       = Synergy("Corrupted"         , ["Fiddlesticks"], [1])
DEFENDER        = Synergy("Defender"          , ["Poppy", "Wukong", "Rell", "Riven", "Sett"], [2, 4, 6])
DUELIST         = Synergy("Duelist"           , ["Kayle", "Gangplank", "Fiora", "Yasuo", "Nilah", "Vayne", "Zed"], [2, 4, 6, 8])
FORECASTER      = Synergy("Forecaster"        , ["Janna"], [1])
HACKER          = Synergy("Hacker"            , ["Leblanc", "Zoe", "Zed"], [2, 3, 4])
HEART           = Synergy("Heart"             , ["Lee Sin", "Yuumi", "Sona", "Soraka", "Syndra"], [2, 4, 6])
MASCOT          = Synergy("Mascot"            , ["Galio", "Nasus", "Malphite", "Yuumi", "Alistar", "Nunu & Willump"], [2, 4, 6, 8])
PRANKSTER       = Synergy("Prankster"         , ["Jinx", "Zoe", "Ekko"], [2, 3, 4])
RECON           = Synergy("Recon"             , ["Ashe", "Ezreal", "Kai'sa", "Vayne"], [2, 3, 4])
RENEGADE        = Synergy("Renegade"          , ["Talon", "Sylas", "Camille", "Viego", "Leona"], [2, 4, 6])
SPELLSLINGER    = Synergy("Spellslinger"      , ["Lux", "Annie", "Sona", "Leblanc", "Taliyah", "Janna"], [2, 4, 6])
SURESHOT        = Synergy("Sureshot"          , ["Sivir", "Senna", "Samira", "Aphelios"], [2, 4])

SET_8_SYNERGIE_NAMES = {"A.D.M.I.N", "Anima Squad", "Arsenal", "Civilian", "Gadgeteen", "LaserCorps", "Mecha: PRIME", "Ox Force", "Star Guardian", "Supers", "Threat", "Underground", "Ace", "Aegis", "Brawler", "Corrupted", "Defender", "Duelist", "Forecaster", "Hacker", "Heart", "Mascot", "Prankster", "Recon", "Renegade", "Spellslinger", "Sureshot"}
SET_8_SYNERGIES = [ADMIN, ANIMA_SQUAD, ARSENAL, CIVILIAN, GADGETEEN, LASERCORPS, MECHA_PRIME, OX_FORCE, STAR_GUARDIAN, SUPERS, THREAT, UNDERGROUND, ACE, AEGIS, BRAWLER, CORRUPTED, DEFENDER, DUELIST, FORECASTER, HACKER, HEART, MASCOT, PRANKSTER, RECON, RENEGADE, SPELLSLINGER, SURESHOT]

# Colors for printing
COLORS = ['Gray', 'Green', 'Orange', 'Purple', 'Cyan', 'Red']