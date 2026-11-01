# ExcellentCrates 6.6.1 — Hologram Vector Fix

**Статус:** неофициальная модификация; в каталоге находятся изменённый JAR,
изменённый Java-файл и патч.

## Исправление

Ошибка при создании hologram entity в PacketEvents могла приводить к сообщениям
`Cannot read field "x" because "vector" is null` и
`Failed to encode packet 'clientbound/minecraft:add_entity'`.

В `HologramPacketsHandler.java` вместо отсутствующего вектора скорости (`null`)
в `WrapperPlayServerSpawnEntity` передаётся `new Vector3d(0.0D, 0.0D, 0.0D)`.

## Файлы

- Исправленный JAR: [`ExcellentCrates-6.6.1-SkiF4er.jar`](ExcellentCrates-6.6.1-SkiF4er.jar)
- SHA-256: [`SHA256SUMS.txt`](SHA256SUMS.txt)
- Изменённый Java-файл: [`HologramPacketsHandler.java`](src/main/java/su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.java)
- Патч изменений: [`hologram-vector-fix.patch`](patches/hologram-vector-fix.patch)
- Лицензия: [`LICENSE`](LICENSE) — GNU GPL v3

## Авторство и условия распространения

Исходный проект: [NightExpress / ExcellentCrates](https://github.com/nulli0n/ExcellentCrates-spigot).
Исправление: SkiF4er, 2026-06-07. Это неофициальная версия.

Исправленный JAR является производным от GPL-3.0-проекта. Если он
распространяется, необходимо выполнить требования GPL к соответствующему
исходному коду и остальные применимые условия. Приведённые в каталоге
отдельный Java-файл и патч не заменяют полный соответствующий исходный код.
