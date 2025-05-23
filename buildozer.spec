[app]
title = Elara
package.name = elara
package.domain = org.elara
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
default_icon = icon.png
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Permissions for Android
android.permissions = INTERNET

# Android settings
android.api = 31
android.minapi = 21
android.sdk = 33
android.ndk = 23b
android.ndk_path = 
android.private_storage = 1
android.archs = armeabi-v7a,arm64-v8a
android.build_tools = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1

[app.android.p4a]
p4a.branch = stable
