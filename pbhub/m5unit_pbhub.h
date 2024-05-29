#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/binary_sensor/binary_sensor.h"

namespace esphome {
namespace m5unit_pbhub {

class M5UnitPbHubBinarySensor : public binary_sensor::BinarySensor, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void loop() override;

  void set_channel(uint8_t channel) { channel_ = channel; }

 protected:
  uint8_t channel_;

  bool read_gpio();
};

}  // namespace m5unit_pbhub
}  // namespace esphome