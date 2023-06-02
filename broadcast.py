# Wir importieren den Code von der lichess API
import berserk

# Wir kreieren eine TokenSession mit einem unter `"https://lichess.org/account/oauth/token/create"` erstellen API token.
session = berserk.TokenSession("lip_xxxxxxxxxxxxxxxxxxx")

# Wir initiieren den client, mit der session (also das Objekt welches via http mit der API kommuniziert)
client = berserk.Client(session=session)

# Wir fordern den Client auf Information über die API zu dem Broadcast xxxxxxxx abzufragen
#
# Die `broadcast_id` kann bei jedem Broadcast under dem Punkt "Broadcast URL" auf der Teilen Seite eines
# Spieles gefunden werden. Die `broadcast_id` von der DEM23 kann unter folgendem link gefunden werden:
# `"https://lichess.org/broadcast/dem-u10-und-u10w/u10-runde-1/cKRywR5b"`, sie lautet `"DB0R5egO"`
print(client.broadcasts.get("xxxxxxxx"))
