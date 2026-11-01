# Уведомления о сторонних компонентах

Корневая лицензия MIT распространяется только на собственные материалы FMP;
она не заменяет лицензии сторонних проектов или их производных версий.

## SkullCreator / SkullCreatorAPI

- Исходный проект: https://github.com/nicholasveronico/SkullCreator (автор: diamondpixel).
- Лицензия оригинального проекта: MIT, см. [`SkullCreatorAPI-3.2.0/LICENSE`](SkullCreatorAPI-3.2.0/LICENSE).
- Изменённый бинарный файл: [`SkullCreatorAPI-3.2.0/SkullCreatorAPI-3.2.0-SkiF4er.jar`](SkullCreatorAPI-3.2.0/SkullCreatorAPI-3.2.0-SkiF4er.jar).
- Контрольная сумма: [`SkullCreatorAPI-3.2.0/SHA256SUMS.txt`](SkullCreatorAPI-3.2.0/SHA256SUMS.txt).
- Модификация: совместимость `TexturePropertyWriter` (SkiF4er).
- Формат: Java-библиотека, не автономный серверный плагин.

## ExcellentCrates

- Исходный проект: https://github.com/nulli0n/ExcellentCrates-spigot (NightExpress).
- Лицензия оригинального проекта: GNU GPL v3, см. [`ExcellentCrates-6.6.1/LICENSE`](ExcellentCrates-6.6.1/LICENSE).
- Изменённый бинарный файл: [`ExcellentCrates-6.6.1/ExcellentCrates-6.6.1-SkiF4er.jar`](ExcellentCrates-6.6.1/ExcellentCrates-6.6.1-SkiF4er.jar).
- Контрольная сумма: [`ExcellentCrates-6.6.1/SHA256SUMS.txt`](ExcellentCrates-6.6.1/SHA256SUMS.txt).
- Изменённый Java-файл: [`ExcellentCrates-6.6.1/src/main/java/su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.java`](ExcellentCrates-6.6.1/src/main/java/su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.java).
- Патч: [`ExcellentCrates-6.6.1/patches/hologram-vector-fix.patch`](ExcellentCrates-6.6.1/patches/hologram-vector-fix.patch).
- Модификация: 07.06.2026, SkiF4er — ненулевой вектор скорости голограммы PacketEvents.

**Важно:** распространение изменённого ExcellentCrates JAR регулируется GPL-3.0.
Один изменённый Java-файл и патч не заменяют предоставление соответствующего
исходного кода в объёме, требуемом GPL. Наличие JAR в этом репозитории само по
себе не доказывает соблюдение всех условий распространения.
