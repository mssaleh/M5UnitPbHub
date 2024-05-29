import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID, CONF_ADDRESS

DEPENDENCIES = ['i2c']

m5unit_pbhub_ns = cg.esphome_ns.namespace('m5unit_pbhub')
M5UnitPbHub = m5unit_pbhub_ns.class_('M5UnitPbHub', cg.Component, i2c.I2CDevice)
PbHubPin = m5unit_pbhub_ns.class_('PbHubPin')

CONF_M5UNIT_PBHUB = 'm5unit_pbhub'
CONF_NUMBER = 'number'
CONF_MODE = 'mode'
CONF_INVERTED = 'inverted'
CONF_CHANNEL = 'channel'

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(M5UnitPbHub),
    cv.Optional(CONF_ADDRESS, default=0x38): cv.i2c_address,
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x38))

PbHubPinSchema = cv.Schema({
    cv.Required(CONF_M5UNIT_PBHUB): cv.use_id(M5UnitPbHub),
    cv.Required(CONF_NUMBER): cv.int_,
    cv.Required(CONF_CHANNEL): cv.int_,
    cv.Optional(CONF_MODE, default='INPUT'): cv.Schema({
        cv.Required('input'): cv.boolean,
        cv.Optional('pullup', default=False): cv.boolean,
    }),
    cv.Optional(CONF_INVERTED, default=False): cv.boolean,
})

def pb_hub_pin_to_code(config):
    hub = yield cg.get_variable(config[CONF_M5UNIT_PBHUB])
    pin = cg.new_Pvariable(hub, config[CONF_CHANNEL], config[CONF_NUMBER], config[CONF_MODE]['pullup'])
    cg.add(pin.set_parent(hub))
    cg.add(pin.set_inverted(config[CONF_INVERTED]))
    return pin

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_ADDRESS])
    yield cg.register_component(var, config)
    yield i2c.register_i2c_device(var, config)
