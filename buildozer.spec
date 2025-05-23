[app]
title = Elara
package.name = elara
package.domain = org.elara.dev
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
osx.python_version = 3
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.api = 33
android.minapi = 21
android.sdk = 24
android.ndk = 23b
android.ndk_path = /home/runner/.buildozer/android/platform/ndk
android.private_storage = 1
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = 1
android.require_android = 21

[app.android.ndk]
# Optional: extra flags to avoid missing symbols
# ndk_platform = android-21

[app.android.p4a]
p4a.branch = stable

[app.android.packaging]
# Optional: increase timeout for large builds
timeout = 600

[app.android.setuptools]
# Optional: if custom modules are needed

[app.android.whitelist]
# If needed, specify domains for network requests

[app.android.additional_dependencies]
# Optional: add here

[app.android.meta_data]
# Optional: metadata to insert in manifest
