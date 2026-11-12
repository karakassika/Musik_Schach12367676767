[app]
# (str) Titel deiner App
title = Schach Trainer

# (str) Paketname
package.name = schachtrainer

# (str) Paketdomäne (Domain)
package.domain = org.schach

# (list) Quelldateien (hier deine main.py)
source.include_exts = py,png,jpg,kv,atlas

# (list) Eintags-Hauptdatei
source.main_ext = py

# (list) Anwendungsversion
version = 0.1

# (list) Verwendete Python-Pakete (wichtig für Schach und Logik)
requirements = python3,chess,gtts

# (list) Android-Berechtigungen (INTERNET für Online/TTS, RECORD_AUDIO für die Spracheingabe!)
android.permissions = INTERNET, RECORD_AUDIO

# (str) Orientierung der App (hier Quer- oder Hochformat)
orientation = portrait