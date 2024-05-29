import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import remote_base
from esphome.const import CONF_ID, CONF_PIN

from .. import pbhub_pin_ns, PbHubPinSchema, pb_hub_pin_to_code

PbHubPinRemoteReceiver = pbhub_pin_ns.class_('PbHubPinRemoteReceiver', remote_base.RemoteReceiver)

CONFIG_SCHEMA = remote_base.REMOTE_RECEIVER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(PbHubPinRemoteReceiver),
    cv.Required(CONF_PIN): PbHubPinSchema,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    pin = yield pb_hub_pin_to_code(config[CONF_PIN])
    cg.add(var.set_pin(pin))
    yield cg.register_component(var, config)
    yield remote_base.register_remote_receiver(var, config)
