import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID, CONF_PIN

DEPENDENCIES = ['m5unit_pbhub']

pbhub_pin_ns = cg.esphome_ns.namespace('pbhub_pin')
PbHubPinBinarySensor = pbhub_pin_ns.class_('PbHubPinBinarySensor', binary_sensor.BinarySensor)

CONFIG_SCHEMA = binary_sensor.BINARY_SENSOR_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(PbHubPinBinarySensor),
    cv.Required(CONF_PIN): cv.int_,
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_parent(hub))
    cg.add(var.set_pin(config[CONF_PIN]))
    await cg.register_component(var, config)
    await binary_sensor.register_binary_sensor(var, config)
