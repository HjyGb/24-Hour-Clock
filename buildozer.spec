[app]
title = 24 小时制时钟
package.name = clock24
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 1

android.permissions = INTERNET,VIBRATE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
