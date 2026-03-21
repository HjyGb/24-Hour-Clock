[app]
# ========== 基础信息（无路径/版本风险） ==========
title = 24HourClock
package.name = clock24
package.domain = org.example
package.version = 0.1

# ========== 源码配置（绝对路径防错） ==========
source.dir = .  # 根目录（GitHub Actions中代码会检出到工作目录，. 是绝对安全的）
source.include_main = main.py  # 主程序文件名（确保你的主文件确实叫main.py）
source.exclude_dirs = venv,.git,.github,build,dist  # 排除无关目录，减少打包体积+防冲突

# ========== 依赖版本（锁定稳定版，避免自动升级） ==========
requirements = python3==3.9.19,kivy==2.2.1,plyer==2.1.0,pillow==9.5.0
# 解释：锁定Python3.9（Kivy最稳定版本）、Kivy2.2.1（避开2.3.0的兼容性问题）

# ========== 安卓SDK/NDK（锁定兼容版本，避免路径/版本报错） ==========
android.api = 33  # 固定API版本，Buildozer可自动下载
android.ndk = 25b  # 与API33匹配的稳定NDK版本
android.ndk_path =  # 留空=Buildozer自动下载到默认路径，手动填路径易出错
android.sdk_path =  # 留空=自动管理，避免手动配置路径错误

# ========== 安卓架构（兼容主流设备，无版本坑） ==========
android.arch = arm64-v8a,armeabi-v7a
android.minapi = 21  # 最低支持安卓5.0，覆盖99%设备

# ========== 构建配置（防错关键） ==========
android.build_type = debug  # 测试阶段用debug，发布时改release
android.ndk_cflags = -Wno-error=format-security  # 关闭NDK编译警告，避免警告变错误
android.add_assets =  # 无额外资源则留空，避免路径错误
android.add_jars =  # 无额外jar包则留空
android.add_libs =  # 无额外so库则留空

# ========== 权限/其他（基础配置，无风险） ==========
android.permissions = INTERNET,WAKE_LOCK
android.icon =  # 无图标则留空，避免"找不到icon.png"报错
android.presplash_color = #FFFFFF  # 启动页颜色，避免缺省值报错

[buildozer]
log_level = 2  # 详细日志，方便排查问题
warn_on_root = 1
android.accept_sdk_license = True  # 自动接受SDK许可，避免交互报错
p4a.bootstrap = sdl2  # 固定bootstrap，避免自动切换导致兼容问题
p4a.version = 2023.07.09  # 锁定python-for-android版本，避免版本漂移