import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID, CONF_PIN

from .. import pbhub_pin_ns, PbHubPin, PbHubPinSchema, pb_hub_pin_to_code

DEPENDENCIES = ['m5unit_pbhub']

PbHubPinBinarySensor = pbhub_pin_ns.class_('PbHubPinBinarySensor', binary_sensor.BinarySensor)

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema(PbHubPinBinarySensor).extend({
    cv.GenerateID(): cv.declare_id(PbHubPinBinarySensor),
    cv.Required(CONF_PIN): PbHubPinSchema,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    pin = yield pb_hub_pin_to_code(config[CONF_PIN])
    var = cg.new_Pvariable(config[CONF_ID], pin)
    yield cg.register_component(var, config)
    yield binary_sensor.register_binary_sensor(var, config)
