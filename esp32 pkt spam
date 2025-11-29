#include "Arduino.h"
#include "nvs_flash.h"
#include "esp_wifi.h"

extern "C" int ieee80211_raw_frame_sanity_check(int32_t arg, int32_t arg2, int32_t arg3) { return 0; }

uint8_t frame[] {
	0x48, 0x00,
	0x00, 0x00,
	0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
	0x00, 0x11, 0x22, 0x33, 0x44, 0x55,
	0x00, 0x11, 0x22, 0x33, 0x44, 0x55,
	0x10, 0x00
};

void setup() {
	nvs_flash_init();
	wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
	esp_wifi_init(&cfg);
	esp_wifi_set_storage(WIFI_STORAGE_RAM);
	esp_wifi_set_mode(WIFI_MODE_STA);
	esp_wifi_start();
}
void loop() {
	// ESP_ERROR_CHECK_WITHOUT_ABORT(esp_wifi_80211_tx(WIFI_IF_STA, frame, sizeof(frame), false));
	esp_wifi_80211_tx(WIFI_IF_STA, frame, sizeof(frame), false);
	delayMicroseconds(560);
}
