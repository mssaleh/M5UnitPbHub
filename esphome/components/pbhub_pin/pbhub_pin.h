#pragma once

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/remote_base/remote_receiver.h"
#include "m5unit_pbhub.h"

namespace esphome {
namespace m5unit_pbhub {

class PbHubPin : public Component, public binary_sensor::BinarySensor, public remote_base::RemoteReceiver {
 public:
  PbHubPin(M5UnitPbHub *parent, uint8_t pin, bool pullup)
      : parent_(parent), pin_(pin), pullup_(pullup) {}

  void setup() override {
    ESP_LOGCONFIG(TAG, "Setting up PbHubPin: pin=%d, pullup=%d", this->pin_, this->pullup_);
    this->parent_->pinMode(this->pin_, this->pullup_ ? INPUT_PULLUP : INPUT);
  }

  void loop() override {
    // Periodic tasks here, if any
  }

  void dump_config() override {
    ESP_LOGCONFIG(TAG, "PbHubPin:");
    ESP_LOGCONFIG(TAG, "  Pin: %d", this->pin_);
  }

  void update() override {
    int value = this->parent_->digitalRead(this->pin_);
    this->publish_state(value);
  }

 private:
  M5UnitPbHub *parent_;
  uint8_t pin_;
  bool pullup_;
  static const char *TAG;
};

const char *PbHubPin::TAG = "pbhub_pin";

}  // namespace m5unit_pbhub
}  // namespace esphome
