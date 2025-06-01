[app]
title = ElaraLite
package.name = elaralite
package.domain = org.elara
source.dir = .
# Dodano 'txt' dla pliku promptu
source.include_exts = py,png,jpg,kv,atlas,txt 
version = 1.0
requirements = python3,kivy
orientation = portrait
# fullscreen = 1 # Możesz to odkomentować, jeśli chcesz pełny ekran bez paska statusu

[buildozer]
log_level = 2
warn_on_root = 0 # Ustaw na 1 jeśli chcesz ostrzeżenia przy pracy jako root (niezalecane)

# === Android specific configuration ===
[app:android]
# --- Permissions ---
# Uprawnienie INTERNET jest już dodane.
# Jeśli Elara ma np. zapisywać pliki (np. wygenerowane obrazy w przyszłości),
# możesz potrzebować więcej uprawnień. Poniżej przykład.
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE
android.permissions = INTERNET

# --- SDK/NDK Versions ---
# Te wersje powinny być spójne z tym, co instaluje Twój GitHub Actions workflow
android.api = 33
android.minapi = 21 # Minimum API level
android.sdk = 33 # Target SDK version (powinno być aktualne)
android.ndk = 25b # Wersja NDK

# --- Ścieżki SDK/NDK ---
# Te ścieżki są istotne, jeśli budujesz lokalnie. 
# Dla GitHub Actions, workflow sam konfiguruje środowisko.
# Jeśli Buildozer nie znajdzie ich tutaj, spróbuje pobrać własne.
# android.ndk_path = /home/runner/android-ndk-r25b # Przykład dla GitHub Actions
# android.sdk_path = /home/runner/android-sdk # Przykład dla GitHub Actions

# --- Build Tools & Architecture ---
android.build_tools = 33.0.2 # Wersja Build Tools
# Dodano arm64-v8a dla nowoczesnych urządzeń, zachowując armeabi-v7a dla starszych
android.archs = armeabi-v7a,arm64-v8a 

# --- Inne ustawienia Android ---
# android.presplash_color = #000000
# android.icon_name = ElaraIcon # Nazwa dla ikony, jeśli dodasz ikony
# android.allow_backup = true
# android.backup_rules = <backup-rules>.xml
# android.manifest.application_label = Elara Lite
# android.manifest.theme = @android:style/Theme.NoTitleBar # Jeśli nie chcesz paska tytułowego
# android.wakelock = partial # Jeśli aplikacja ma działać w tle
