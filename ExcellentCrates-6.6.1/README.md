# ExcellentCrates 6.6.1 — Hologram Vector Fix

**Статус:** опубликованы исходный файл и патч, а также изменённый JAR.

## Исправление

Ошибка при создании hologram entity в PacketEvents могла приводить к сообщению
`Cannot read field "x" because "vector" is null` / `Failed to encode packet 'clientbound/minecraft:add_entity'`.

В `HologramPacketsHandler.java` аргумент velocity для `WrapperPlayServerSpawnEntity`
заменён с `null` на `new Vector3d(0.0D, 0.0D, 0.0D)`.

- Исправленный Java-файл: [`src/main/java/.../HologramPacketsHandler.java`](src/main/java/su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.java)
- Патч: [`patches/hologram-vector-fix.patch`](patches/hologram-vector-fix.patch)
- Исходная версия и контрольные значения: [`UPSTREAM.txt`](UPSTREAM.txt)
- Лицензия: [`LICENSE`](LICENSE) — GNU GPL v3

## Воссоздание полного дерева исходников

В корне публичного репозитория запустите:

```bash
bash scripts/reconstruct-excellentcrates.sh
```

Потребуется `git` и доступ к GitHub. Скрипт скачивает зафиксированный upstream-коммит,
проверяет исходный файл и применяет патч. Результат — каталог
`build/excellentcrates-6.6.1-source/`, а не готовый JAR. Для сборки необходимы
Java 21, Maven и доступные зависимости, указанные в upstream `pom.xml`.

## Авторство и публикация бинарника

Upstream: NightExpress / ExcellentCrates. Исправление: SkiF4er, 2026-06-07.
Код ExcellentCrates и производные модификации регулируются GPL, а не корневой MIT.