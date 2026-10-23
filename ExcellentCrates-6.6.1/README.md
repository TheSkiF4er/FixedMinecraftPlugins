# ExcellentCrates 6.6.1 — SkiF4er Hologram Vector Fix

## Что исправлено

Исправлен кик игроков рядом с голограммами ExcellentCrates на новых Paper/Minecraft-сборках, связанный с ошибкой вида:

```text
Cannot read field "x" because "vector" is null
Failed to encode packet 'clientbound/minecraft:add_entity'
```

## Изменённый файл внутри jar

```text
su/nightexpress/excellentcrates/hologram/handler/HologramPacketsHandler.class
```

## Суть фикса

В PacketEvents-ветке hologram spawn packet ExcellentCrates 6.6.1 передавал `null` как velocity/vector в `WrapperPlayServerSpawnEntity`.
Фикс заменяет `null` на нулевой вектор:

```java
new Vector3d(0.0D, 0.0D, 0.0D)
```

## Авторский фикс

Фикс подготовлен: Дмитрий "SkiF4er" Ефимов / SkiF4er Development.
Дата: 2026-06-07.

## Установка

1. Остановить сервер.
2. Сделать резервную копию текущего `ExcellentCrates-6.6.1.jar`.
3. Заменить jar на `ExcellentCrates-6.6.1-SkiF4er-HologramVectorFix.jar`.
4. Запустить сервер.
5. Проверить подход к crate/hologram, где раньше происходил кик.

## Важно

Это авторский бинарный фикс конкретной версии ExcellentCrates 6.6.1. Оригинальные права на плагин остаются у исходных авторов. Не распространяйте исправленный jar публично без разрешения правообладателя оригинального плагина.
