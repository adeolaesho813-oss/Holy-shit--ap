[app]
title = My App
package.name = myapp
package.domain = org.test
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# (android) permissions if you need
#android.permissions = INTERNET

[app:android]
# If you get error about gradle, keep this
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
