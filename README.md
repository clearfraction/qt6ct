# qt6ct

### How to test

- extract the package from artifacts to `/tmp/usr`
- extract [Qt libs](https://download.clearlinux.org/releases/38390/clear/x86_64/os/Packages/qt6base-lib-6.2.1-61.x86_64.rpm) to `/tmp/usr/lib64`
- run: `env QT_QPA_PLATFORMTHEME=qt6ct QT_PLUGIN_PATH=/tmp/usr/lib64/qt5/plugins/ LD_LIBRARY_PATH=/tmp/usr/lib64/:$LD_LIBRARY_PATH /tmp/usr/bin/qt6ct`
