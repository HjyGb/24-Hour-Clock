[app]
# 最低 Android API 版本（需和上面配置的 ANDROIDAPI 匹配）
android.api = 33
# Build-Tools 版本（需和上面的 BUILD_TOOLS 匹配）
android.build_tools = 33.0.2
# NDK 版本（需和上面安装的 NDK 版本匹配）
android.ndk = 25c
# SDK 路径（上面的脚本会自动填充，也可手动写死）
android.sdk_path = /home/runner/android-sdk

[buildozer]
# 禁止自动下载 SDK（避免冲突）
android.autoconfig = 0