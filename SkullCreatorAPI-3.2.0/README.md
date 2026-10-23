# SkullCreatorAPI 3.2.0 — SkiF4er Custom Heads Fix

Автор исправления: **SkiF4er**

## Назначение

Фикс предназначен для сценариев, где кастомные головы / skull textures ломаются на новых версиях Minecraft/Paper 1.21.9+ / 1.21.11 из-за несовместимости путей записи texture properties, включая ошибки вокруг `GameProfile#getProperties`.

## Что изменено

Изменён класс:

```text
com/skullcreator/internal/util/TexturePropertyWriter.class
```

Добавлена более безопасная логика применения текстуры:

1. Приоритетно используется Bukkit `PlayerProfile` / `PlayerTextures`.
2. Поддержаны варианты `setSkin(URL)` и `setSkin(URL, SkinModel)`.
3. Добавлен безопасный fallback для `setProperty("textures", base64)`.
4. Добавлен fallback для Authlib `PropertyMap` без жёсткой бинарной зависимости от `GameProfile#getProperties`.
5. Ошибка применения текстуры не должна валить плагин, использующий API.

## Установка

1. Сделайте резервную копию старого `SkullCreatorAPI-3.2.0.jar`.
2. Остановите сервер.
3. Замените jar на `SkullCreatorAPI-3.2.0-SkiF4er-CustomHeadsFix.jar`.
4. Запустите сервер.
5. Проверьте меню, GUI, кейсы, профили и другие места, где используются кастомные головы.

## Важно

Фикс предназначен для конкретной версии `SkullCreatorAPI 3.2.0`. Перед установкой на production рекомендуется проверка на тестовом сервере.
