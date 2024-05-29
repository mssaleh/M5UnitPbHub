import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import remote_base, binary_sensor
from esphome.const import CONF_ID, CONF_PIN

DEPENDENCIES = ['m5unit_pbhub']

pbhub_pin_ns = cg.esphome_ns.namespace('pbhub_pin')
PbHubPin = pbhub_pin_ns.class_('PbHubPin')

PbHubPinSchema = cv.Schema({
    cv.GenerateID(): cv.use_id('m5unit_pbhub', 'M5UnitPbHub'),
    cv.Required('number'): cv.int_,
    cv.Optional('mode', default='INPUT'): cv.one_of('INPUT', 'INPUT_PULLUP', lower=True),
    cv.Optional('pullup', default=False): cv.boolean,
})

def pb_hub_pin_to_code(config):
    hub = yield cg.get_variable(config[CONF_ID])
    pin = cg.new_Pvariable(config[CONF_ID], config['number'], config['mode'], config['pullup'])
    cg.add(pin.set_parent(hub))
    return pin
