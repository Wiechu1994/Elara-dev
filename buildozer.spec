name: Build APK

on: push: branches: - master

jobs: build_apk: name: Build APK using Buildozer runs-on: ubuntu-latest

steps:
  - name: Checkout repo
    uses: actions/checkout@v3

  - name: Set up Python
    uses: actions/setup-python@v4
    with:
      python-version: "3.10"

  - name: Install system dependencies
    run: |
      sudo apt update
      sudo apt install -y \
        zip \
        unzip \
        git \
        ccache \
        build-essential \
        libffi-dev \
        libssl-dev \
        liblzma-dev \
        libjpeg-dev \
        zlib1g-dev \
        libgl1-mesa-dev \
        libncursesw5 \
        openjdk-17-jdk \
        python3-pip \
        python3-setuptools \
        python3-wheel

  - name: Install Android SDK
    run: |
      mkdir -p $HOME/android-sdk/cmdline-tools
      cd $HOME/android-sdk/cmdline-tools
      curl -o sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-10406996_latest.zip
      unzip sdk.zip -d latest
      echo "ANDROID_SDK_ROOT=$HOME/android-sdk" >> $GITHUB_ENV
      echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH
      echo "$HOME/android-sdk/platform-tools" >> $GITHUB_PATH
      yes | $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses
      $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager \
        "platform-tools" \
        "platforms;android-31" \
        "build-tools;33.0.2"

  - name: Install Python deps
    run: |
      python -m pip install --upgrade pip
      pip install cython virtualenv buildozer

  - name: Build
