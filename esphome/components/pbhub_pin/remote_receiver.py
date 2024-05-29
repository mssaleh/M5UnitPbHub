import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import remote_base
from esphome.const import CONF_ID, CONF_PIN, CONF_MODE, CONF_PULLUP

from .. import pbhub_pin_ns, PbHubPin

PbHubPinRemoteReceiver = pbhub_pin_ns.class_('PbHubPinRemoteReceiver', remote_base.RemoteReceiver)

CONFIG_SCHEMA = remote_base.REMOTE_RECEIVER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(PbHubPinRemoteReceiver),
    cv.Required(CONF_PIN): cv.int_,
    cv.Optional(CONF_MODE, default='INPUT'): cv.one_of('INPUT', 'INPUT_PULLUP', lower=True),
    cv.Optional(CONF_PULLUP, default=False): cv.boolean,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    hub = yield cg.get_variable(config[CONF_ID])
    var = cg.new_Pvariable(config[CONF_ID], hub, config[CONF_PIN], config[CONF_PULLUP])
    cg.add(var.set_parent(hub))
    yield cg.register_component(var, config)
    yield remote_base.register_remote_receiver(var, config)
