# Disconnected Review-Log Cleaner

**Bug Report:** [https://github.com/cjdduarte/Disconnected_Review_Log_Cleaner/issues](https://github.com/cjdduarte/Disconnected_Review_Log_Cleaner/issues)

## **Description**

The Disconnected Review-Log Cleaner add-on is designed to identify and remove orphaned review log entries that accumulate in the database over time. When cards are deleted, their associated review histories can become disconnected, meaning they're no longer linked to any active card. This tool efficiently cleans these orphaned entries, ensuring a tidier and more optimized database.

## **Usage**

1. Navigate to the **Tools** menu in Anki
2. Select **"Cleanup Deleted Card Reviews"** (or translated equivalent)
3. Review the count of orphaned entries found
4. Confirm the prompt to clean the orphaned review log entries
5. A full synchronization will be automatically triggered

![Screenshot](https://i.ibb.co/JcsDryY/image.png)

## **Supported Languages**

- **English**: "Cleanup Deleted Card Reviews"
- **Português (BR)**: "Limpar Revisões de Cartões Excluídos"  
- **Español**: "Limpiar Revisiones de Tarjetas Eliminadas"

*Language is automatically detected from Anki settings or system locale.*

## **Important Notes**

- After cleaning, a **full synchronization** is automatically required
- The operation runs in the background without freezing Anki
- All changes are properly tracked for multi-device sync compatibility
- Modern error handling prevents data corruption

## **Installation**

1. Download the add-on from AnkiWeb or GitHub
2. Install through Anki's Add-ons manager
3. Restart Anki
4. The menu item will appear in **Tools** menu in your language

## **Changelog**

- **v2.0 - 2025-06-10 - Modern Translation System & API Updates**
    - **NEW:** Complete multi-language support (EN, PT-BR, ES)
    - **NEW:** Automatic language detection from Anki/system settings
    - **BREAKING:** Updated to modern `CollectionOp` API (Anki 25.06+ compatible)
    - **IMPROVED:** Better error handling with user-friendly messages
    - **IMPROVED:** Background processing prevents UI freezing
    - **IMPROVED:** Proper `OpChanges` return object for sync compatibility
    - **COMPATIBILITY:** Full support for Anki 25.06+ (no more deprecation warnings)
    - **FIXED:** Replaced deprecated `modSchema`, `setMod()`, `save()`, `requireReset()`
    - Renamed menu items for clarity: "Cleanup Deleted Card Reviews"
    - Enhanced confirmation and success messages
    - Modern translation system with fallback support
- **v1.1 - 2024-08-19 - Improved Messaging**
    - Improved success message after cleaning logs
- **v1.0 - 2023-08-19 - Initial Release**
    - Basic disconnected review log cleaning functionality

## **License & Credits**

- **Copyright(C)**: Carlos Duarte
- **License**: [GNU AGPL](http://www.gnu.org/licenses/agpl.html), version 3 or later
- **Source**: [GitHub Repository](https://github.com/cjdduarte/Disconnected_Review_Log_Cleaner)
