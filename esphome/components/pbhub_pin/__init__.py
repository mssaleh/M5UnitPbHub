import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import remote_base
from esphome.const import CONF_ID, CONF_PIN

DEPENDENCIES = ['m5unit_pbhub']

pbhub_pin_ns = cg.esphome_ns.namespace('pbhub_pin')
PbHubPin = pbhub_pin_ns.class_('PbHubPin', remote_base.RemoteReceiver)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(PbHubPin),
    cv.Required(CONF_PIN): cv.int_,
}).extend(remote_base.REMOTE_RECEIVER_SCHEMA)

def to_code(config):
    hub = yield cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(config[CONF_ID])
    cg.add(var.set_parent(hub))
    cg.add(var.set_pin(config[CONF_PIN]))
    yield cg.register_component(var, config)
    yield remote_base.register_remote_receiver(var, config)
