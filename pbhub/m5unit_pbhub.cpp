#include "m5unit_pbhub.h"
#include "esphome/core/log.h"

namespace esphome {
namespace m5unit_pbhub {

static const char *const TAG = "m5unit_pbhub";

void M5UnitPbHubOutput::setup() {
  ESP_LOGCONFIG(TAG, "Setting up M5Unit-PbHub Output");
  if (!this->write_bytes(this->address_, {}, 0)) {
    this->mark_failed();
    return;
  }
}

void M5UnitPbHubOutput::dump_config() {
  ESP_LOGCONFIG(TAG, "M5Unit-PbHub Output:");
  ESP_LOGCONFIG(TAG, "  I2C Address: 0x%02X", this->address_);
  ESP_LOGCONFIG(TAG, "  Channel: %u", channel_);
}

void M5UnitPbHubOutput::write_state(bool state) {
  uint8_t ch = channel_;
  if (ch == 5) ch++;
  uint8_t reg = ((ch + 4) << 4) | 0x00;
  write_byte(reg, state);
}

bool M5UnitPbHubOutput::write_byte(uint8_t reg, uint8_t data) {
  return this->write_byte(reg, data);
}

}  // namespace m5unit_pbhub
}  // namespace esphome