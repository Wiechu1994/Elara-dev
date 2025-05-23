[app]
title = Elara
package.name = elara
package.domain = org.yourdomain
source.dir = .
source.include_exts = py,kv,png,jpg,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[python]
# Domyślna wersja Pythona
version = 3

[android]
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.ndk_path = 
android.sdk_path = 
android.ndk_api = 21
p4a.branch = develop
