import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor, remote_base
from esphome.const import CONF_ID, CONF_PIN

DEPENDENCIES = ['m5unit_pbhub']

pbhub_pin_ns = cg.esphome_ns.namespace('pbhub_pin')
PbHubPin = pbhub_pin_ns.class_('PbHubPin', cg.Component, binary_sensor.BinarySensor, remote_base.RemoteReceiver)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(PbHubPin),
    cv.Required(CONF_PIN): PbHubPinSchema,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    hub = yield cg.get_variable(config[CONF_ID])
    pin = yield pb_hub_pin_to_code(config[CONF_PIN])
    var = cg.new_Pvariable(config[CONF_ID], pin)
    cg.add(var.set_parent(hub))
    yield cg.register_component(var, config)
    yield binary_sensor.register_binary_sensor(var, config)
    yield remote_base.register_remote_receiver(var, config)
