import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.const import CONF_ID, CONF_ADDRESS, CONF_CHANNEL

DEPENDENCIES = ['i2c']

m5unit_pbhub_ns = cg.esphome_ns.namespace('m5unit_pbhub')
M5UnitPbHub = m5unit_pbhub_ns.class_('M5UnitPbHub', cg.Component, i2c.I2CDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(M5UnitPbHub),
    cv.Optional(CONF_ADDRESS, default=0x61): cv.i2c_address,
    cv.Optional(CONF_CHANNEL, default=0): cv.int_,
}).extend(cv.COMPONENT_SCHEMA).extend(i2c.i2c_device_schema(0x61))

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_ADDRESS], config[CONF_CHANNEL])
    yield cg.register_component(var, config)
    yield i2c.register_i2c_device(var, config)
