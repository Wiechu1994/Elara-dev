[app]
title = Elara Lite
package.name = elara
package.domain = org.elara
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, \
READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, RECORD_AUDIO, \
MODIFY_AUDIO_SETTINGS, WAKE_LOCK, BLUETOOTH, BLUETOOTH_ADMIN, VIBRATE

[buildozer]
log_level = 2
warn_on_root = 1
android.api = 33
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
