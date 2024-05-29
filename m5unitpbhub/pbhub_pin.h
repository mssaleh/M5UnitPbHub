#include "esphome.h"
#include "esphome/components/remote_base/remote_receiver.h"
#include "m5unit_pbhub.h"

namespace esphome {
namespace pbhub_pin {

class PbHubPin : public Component, public remote_base::RemoteReceiver {
public:
    void setup() override {
        ESP_LOGCONFIG(TAG, "Setting up PbHubPin: pin=%d", this->pin_);
        auto pbhub = this->parent_;
        pbhub->add_virtual_pin(this->pin_, this);
    }

    void loop() override {
        // Override if necessary
    }

    void set_parent(M5UnitPbHub *parent) {
        this->parent_ = parent;
    }

    void set_pin(uint8_t pin) {
        this->pin_ = pin;
    }

    void dump_config() override {
        ESP_LOGCONFIG(TAG, "PbHubPin:");
        ESP_LOGCONFIG(TAG, "  Pin: %d", this->pin_);
    }

protected:
    M5UnitPbHub *parent_;
    uint8_t pin_;
};

}  // namespace pbhub_pin
}  // namespace esphome
