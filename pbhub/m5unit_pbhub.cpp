#include "m5unit_pbhub.h"
#include "esphome/core/log.h"

namespace esphome {
namespace m5unit_pbhub {

static const char *const TAG = "m5unit_pbhub";

void M5UnitPbHubBinarySensor::setup() {
  ESP_LOGCONFIG(TAG, "Setting up M5Unit-PbHub Binary Sensor");
}

void M5UnitPbHubBinarySensor::dump_config() {
  ESP_LOGCONFIG(TAG, "M5Unit-PbHub Binary Sensor:");
  ESP_LOGCONFIG(TAG, "  I2C Address: 0x%02X", this->address_);
  ESP_LOGCONFIG(TAG, "  Channel: %u", channel_);
}

void M5UnitPbHubBinarySensor::loop() {
  bool state = read_gpio();
  publish_state(state);
}

bool M5UnitPbHubBinarySensor::read_gpio() {
  uint8_t ch = channel_;
  if (ch == 5) ch++;
  uint8_t reg = ((ch + 4) << 4) | 0x04;
  uint8_t data;
  if (!this->read_byte(reg, &data)) {
    return false;
  }
  return data;
}

}  // namespace m5unit_pbhub
}  // namespace esphome