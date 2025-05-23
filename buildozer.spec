[app]

title = ElaraDev
package.name = elaradev
package.domain = org.elara
source.dir = .
source.include_exts = py,kv,txt,png,jpg,md,json
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 1
osx.kivy_version = 2.1.0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.minapi = 21
android.api = 31
android.ndk = 23b
android.sdk = 24
android.arch = armeabi-v7a
copy_to_bin = 1

presplash.filename = %(source.dir)s/data/logo.png
icon.filename = %(source.dir)s/data/icon.png

[buildozer]

log_level = 2
warn_on_root = 0

[python]

use_kivy_settings = 0

[android]

android.allow_backup = True
android.support_old_jars = True
android.gradle_dependencies = 
    org.jetbrains.kotlin:kotlin-stdlib:1.6.10

android.extra_args = --no-version-vectors

# Jeśli w przyszłości dodasz TTS lub inne funkcje:
# android.add_jars = /path/to/some.jar
# android.add_src = /path/to/java/files
