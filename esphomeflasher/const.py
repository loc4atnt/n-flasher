import re

__version__ = "1.4.0"

ESP32_DEFAULT_OTA_DATA = "https://raw.githubusercontent.com/espressif/arduino-esp32/1.0.0/tools/partitions/boot_app0.bin"
ESP32_DEFAULT_BOOTLOADER_FORMAT = (
    "https://raw.githubusercontent.com/espressif/arduino-esp32/"
    "1.0.4/tools/sdk/bin/bootloader_$FLASH_MODE$_$FLASH_FREQ$.bin"
)
ESP32_DEFAULT_PARTITIONS = (
    "https://raw.githubusercontent.com/loc4atnt/n-flasher/main/partitions.min_spiffs.bin"
)

# https://stackoverflow.com/a/3809435/8924614
HTTP_REGEX = re.compile(
    r"https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)"
)

ESP32_FLASH_SCHEME_MAP = {
    "4M - 1.9M App & OTA - 190K SPIFFS": {
        "path": "https://raw.githubusercontent.com/loc4atnt/n-flasher/main/partitions.min_spiffs.bin",
    },
    "4M - 1.2M App - 1.5M SPIFFS": {
        "path": "https://raw.githubusercontent.com/loc4atnt/n-flasher/main/partitions-4m-1.2m_app-1.5m_spiffs.bin",
    },
    "8M - 2M App - 3.9M SPIFFS": {
        "path": "https://raw.githubusercontent.com/loc4atnt/n-flasher/main/partitions_app2m_spiffs3.9M.bin",
    },
    "16M - 2M App - 12.5M SPIFFS": {
        "path": "https://raw.githubusercontent.com/loc4atnt/n-flasher/main/partitions-16m-2m_app-12.5m_spiffs.bin",
    },
}

WINDOW_HEIGHT = 725
WINDOW_WIDTH = 725