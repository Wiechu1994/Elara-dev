[app]
title = Elara
package.name = elara
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Permissions
android.permissions = INTERNET

# Android-specific
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_path = 
android.private_storage = True
android.target = android-33
android.build_tools = 33.0.2
android.archs = armeabi-v7a,arm64-v8a
android.accept_sdk_license = True

# If using kivy launcher
# android.entrypoint = org.kivy.android.PythonActivity
# android.manifest.intent_filters =

[buildozer]
log_level = 2
warn_on_root = 1
