import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import remote_base
from esphome.const import CONF_ID, CONF_PIN, CONF_MODE, CONF_PULLUP

DEPENDENCIES = ['m5unit_pbhub']

pbhub_pin_ns = cg.esphome_ns.namespace('pbhub_pin')
PbHubPinRemoteReceiver = pbhub_pin_ns.class_('PbHubPinRemoteReceiver', remote_base.RemoteReceiver)

CONF_M5UNIT_PBHUB = 'm5unit_pbhub'
CONF_NUMBER = 'number'
CONF_INVERTED = 'inverted'

PbHubPinSchema = cv.Schema({
    cv.GenerateID(): cv.use_id('m5unit_pbhub', 'M5UnitPbHub'),
    cv.Required(CONF_NUMBER): cv.int_,
    cv.Optional(CONF_MODE, default='INPUT'): cv.Schema({
        'input': cv.boolean,
        'pullup': cv.boolean,
    }),
    cv.Optional(CONF_INVERTED, default=False): cv.boolean,
})

CONFIG_SCHEMA = remote_base.REMOTE_RECEIVER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(PbHubPinRemoteReceiver),
    cv.Required(CONF_PIN): PbHubPinSchema,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    hub = yield cg.get_variable(config[CONF_PIN][CONF_M5UNIT_PBHUB])
    pin_mode = config[CONF_PIN][CONF_MODE]
    var = cg.new_Pvariable(config[CONF_ID], hub, config[CONF_PIN][CONF_NUMBER], pin_mode['pullup'])
    cg.add(var.set_parent(hub))
    cg.add(var.set_inverted(config[CONF_PIN][CONF_INVERTED]))
    yield cg.register_component(var, config)
    yield remote_base.register_remote_receiver(var, config)
