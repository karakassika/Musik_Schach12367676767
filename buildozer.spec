[app]

# (str) Titel deiner App
title = Schach Trainer

# (str) Paketname
package.name = schachtrainer

# (str) Paketdomäne (Domain)
package.domain = org.schach

# (list) Quelldateien (hier deine main.py und Assets)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# (list) Eintrags-Hauptdatei
source.main_ext = py

# (list) Anwendungsversion
version = 0.1

# (list) Verwendete Python-Pakete (wichtig für Schach und Logik)
requirements = python3,chess,gtts

# (list) Android-Berechtigungen (INTERNET für Online/TTS, RECORD_AUDIO für die Sprache)
android.permissions = INTERNET,RECORD_AUDIO

# (str) Orientierung der App (hier Quer- oder Hochformat)
orientation = portrait

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android SDK accept license (True or False)
android.accept_sdk_license = True

[buildozer]

# (int) Loglevel (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
