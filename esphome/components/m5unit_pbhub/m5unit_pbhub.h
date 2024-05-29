#pragma once
#include "esphome.h"
#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace m5unit_pbhub {

class M5UnitPbHub : public Component, public i2c::I2CDevice {
 public:
  M5UnitPbHub(uint8_t address = 0x38) : i2c::I2CDevice(address) {}

  void setup() override {
    ESP_LOGCONFIG(TAG, "Setting up M5UnitPbHub at address 0x%02X", this->address_);
    // Initialization code here, if any
  }

  void loop() override {
    // Periodic tasks here, if any
  }

  void pinMode(uint8_t pin, uint8_t mode) {
    ESP_LOGD(TAG, "Setting pin mode: pin=%d, mode=%d", pin, mode);
    uint8_t data[] = {0x00, pin, mode};
    this->write_bytes(this->address_, data, sizeof(data));
  }

  void digitalWrite(uint8_t pin, uint8_t value) {
    ESP_LOGD(TAG, "Writing digital value: pin=%d, value=%d", pin, value);
    uint8_t data[] = {0x01, pin, value};
    this->write_bytes(this->address_, data, sizeof(data));
  }

  int digitalRead(uint8_t pin) {
    ESP_LOGD(TAG, "Reading digital value: pin=%d", pin);
    uint8_t data[] = {0x02, pin};
    this->write_bytes(this->address_, data, sizeof(data));
    uint8_t result;
    this->read_bytes(this->address_, &result, 1);
    ESP_LOGD(TAG, "Read value: %d", result);
    return result;
  }

  float get_setup_priority() const override {
    return setup_priority::DATA;
  }

  void dump_config() override {
    ESP_LOGCONFIG(TAG, "M5UnitPbHub:");
    ESP_LOGCONFIG(TAG, "  Address: 0x%02X", this->address_);
  }

 private:
  static const char *TAG;
};

const char *M5UnitPbHub::TAG = "m5unit_pbhub";

}  // namespace m5unit_pbhub
}  // namespace esphome
