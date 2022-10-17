##!pip install pandas
import pandas as pd
atbats = pd.read_csv("atbats.csv")
pitches = pd.read_csv("pitches.csv")
atbats = atbats.loc[:,["ab_id","g_id"]]
Npitches = atbats.merge(pitches,how = "inner", on = "ab_id")
Npitches = Npitches.loc[:,["g_id","ab_id", "pitch_num", "start_speed", "end_speed", "spin_rate", "spin_dir", "type", "b_score", "b_count", "s_count", "outs" ]]
Npitches.to_csv("Npitches.csv" , index = False)

player_names = pd.read_csv("player_names.csv")
infopn = pd.read_csv("infopn.csv")
infopn["team"] = infopn['team'].str.lower()
player_names["name"] = player_names["first_name"] +" "+ player_names["last_name"]
Nplayer_names = infopn.merge(player_names,how = "inner", on = "name")
Nplayer_names.head()
Nplayer_names = Nplayer_names.loc[:,["id" , "name", "team", "year", "war", "sal", "exp" ]]
Nplayer_names.to_csv("Nplayer_names.csv", index = False)
ejections = pd.read_csv("ejections.csv")
aNplayer_names = Nplayer_names.loc[:,["id", "year", "team"]]
Nejections = aNplayer_names.merge(ejections,how = "inner", on = ["id", "team"])
Nejections.to_csv("Nejections.csv", index = False)
Nejections = Nejections.dropna(subset=["ab_id" , "g_id"])

atbats = pd.read_csv("atbats.csv")
atbats = atbats.loc[:,["batter_id", "g_id" , "ab_id"]]
Bplayer_names = Nplayer_names
Bplayer_names = Bplayer_names.rename(columns = {"id": "batter_id"} )
batea = atbats.merge(Bplayer_names,how = "inner", on = ["batter_id"])
batea = atbats.rename(columns = {"batter_id": "id"} )
batea = batea.loc[:,["id", "year", "team", "ab_id", "g_id"]]


atbats = pd.read_csv("atbats.csv")
atbats = atbats.loc[:,["pitcher_id", "g_id" , "ab_id"]]
Pplayer_names = Nplayer_names
Pplayer_names = Pplayer_names.rename(columns = {"id": "pitcher_id"} )
lanza = atbats.merge(Pplayer_names,how = "inner", on = ["pitcher_id"])
lanza = lanza.rename(columns = {"pitcher_id": "id"} )
pitches = pd.read_csv("Npitches.csv")
pitches = pitches.loc[:,[ "ab_id", "g_id" , "pitch_num"]]
lanza = lanza.merge(pitches,how = "inner", on = ["g_id", "ab_id"])
lanza = lanza.loc[:,[ "pitcher_id", "year" , "team", "pitch_num", "ab_id", "g_id"]]
