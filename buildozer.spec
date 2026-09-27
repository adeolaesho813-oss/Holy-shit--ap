[app]
title = Holy Shit Ap
package.name = holyshitap
package.domain = com.adeola.holyshitap

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:android]
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
