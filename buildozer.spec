[app]
title = ElaraLite
package.name = elaralite
package.domain = org.elara
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 0

[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_path = /home/runner/android-ndk-r25b
android.sdk_path = /home/runner/android-sdk
android.build_tools = 33.0.2
android.arch = armeabi-v7a
