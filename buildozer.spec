[app]
title = 24 小时制时钟
package.name = clock24
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,kivy==2.3.0,cython==0.29.33

# 添加可能的额外依赖
# p4a.local_recipes = # 如果需要本地配方可以取消注释
orientation = portrait
fullscreen = 1

android.permissions = INTERNET,VIBRATE
android.api = 31
android.minapi = 21
android.sdk = 24
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accept_any_license = True

[buildozer]
log_level = 2
warn_on_root = 1
