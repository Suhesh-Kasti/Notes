---
category: knowledge
tags:
  - python
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Getting the apk
---

# Getting the apk
Before decompiling an application we first need to get the application. For that we use the following command
```python
adb shell
pm list packages
pm path 
adb pull <PATH>
```
# Decompiling
We can use an application like apktool to decompile an application
`apktool d <APK>` -> Used to decompile an application
`apktool b <APK_PATH>` -> Used to build the application
