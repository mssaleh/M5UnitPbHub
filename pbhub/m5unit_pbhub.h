#pragma once

#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"
#include "esphome/components/output/binary_output.h"

namespace esphome {
namespace m5unit_pbhub {

class M5UnitPbHubOutput : public output::BinaryOutput, public i2c::I2CDevice {
 public:
  void setup() override;
  void dump_config() override;
  void write_state(bool state) override;

  void set_channel(uint8_t channel) { channel_ = channel; }

 protected:
  uint8_t channel_;

  bool write_byte(uint8_t reg, uint8_t data);
};

}  // namespace m5unit_pbhub
}  // namespace esphome