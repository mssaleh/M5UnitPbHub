#include "esphome.h"
#include "esphome/core/component.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace m5unit_pbhub {

class M5UnitPbHub : public Component, public i2c::I2CDevice {
public:
    M5UnitPbHub(uint8_t address = 0x38, uint8_t channel = 0)
        : address_(address), channel_(channel) {}

    void setup() override {
        ESP_LOGCONFIG(TAG, "Setting up M5UnitPbHub at address 0x%02X, channel %d", this->address_, this->channel_);
        this->begin();
    }

    void loop() override {
        for (auto &pin : this->virtual_pins_) {
            int value = this->digitalRead(pin.first);
            pin.second->publish_state(value);
        }
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

    void add_virtual_pin(uint8_t pin, BinarySensor *sensor) {
        ESP_LOGCONFIG(TAG, "Adding virtual pin: pin=%d", pin);
        this->virtual_pins_[pin] = sensor;
        this->pinMode(pin, INPUT);
    }

    void dump_config() override {
        ESP_LOGCONFIG(TAG, "M5UnitPbHub:");
        ESP_LOGCONFIG(TAG, "  Address: 0x%02X", this->address_);
        ESP_LOGCONFIG(TAG, "  Channel: %d", this->channel_);
        for (const auto &pin : this->virtual_pins_) {
            ESP_LOGCONFIG(TAG, "  Virtual Pin: %d", pin.first);
        }
    }

private:
    uint8_t address_;
    uint8_t channel_;
    std::map<uint8_t, BinarySensor*> virtual_pins_;
    static const char *TAG;
};

const char *M5UnitPbHub::TAG = "m5unit_pbhub";

}  // namespace m5unit_pbhub
}  // namespace esphome
