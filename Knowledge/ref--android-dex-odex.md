---
category: knowledge
tags:
  - reference
platform: n/a
status: done
created: 2026-06-17
aliases:
  - Java
---

# Java
When we compile java code we get a java bytecode but that file is much more resource intensive so we cannot use that directly on our phones which use ARM architecture.
So we have to compile it in a way that it's dalvik executable which gives us a *.dex* file
Odex stands for optimized dex
![[images/android_dex_odex.png]]

# Multidexing
classes.dex file can only contain 65535 methods. So if an application contains more methods than that (includes frameworks, libraries) the classes file has to be seperated into multiple files like classes.dex, classes2.dex, classes3.dex etc which is multidexing.
# [[Classes.dex]]
We can use tools like **ghex** to get a hexadecimal view of the dex file. But ghex cannot do anything more than that. To do more than that we need to use **dexdump**.
We can decompile classes.dex file using the program dexdump in following way after extracting the apk
```bash
dexdump -d 
```
