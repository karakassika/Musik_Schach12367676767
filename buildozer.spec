[app]

title = Schach Trainer
package.name = schachtrainer
package.domain = org.schach

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.main_ext = py
version = 0.1

requirements = python3,chess
android.permissions = INTERNET
orientation = portrait
android.api = 33
android.min_api = 21
android.accept_sdk_license = True
android.build_tools_version = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1
