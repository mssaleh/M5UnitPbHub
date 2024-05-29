#include "pbhub_pin.h"
#include "esphome/core/log.h"

namespace esphome {
namespace m5unit_pbhub {

static const char *TAG = "pbhub_pin";

void PbHubPin::setup() {
  ESP_LOGCONFIG(TAG, "Setting up PbHubPin: pin=%d, pullup=%d", this->pin_, this->pullup_);
  this->parent_->pinMode(this->pin_, this->pullup_ ? INPUT_PULLUP : INPUT);
}

void PbHubPin::loop() {
  // No periodic tasks for now
}

void PbHubPin::dump_config() {
  ESP_LOGCONFIG(TAG, "PbHubPin:");
  ESP_LOGCONFIG(TAG, "  Pin: %d", this->pin_);
}

void PbHubPin::update() {
  int value = this->parent_->digitalRead(this->pin_);
  this->publish_state(value);
}

}  // namespace m5unit_pbhub
}  // namespace esphome
