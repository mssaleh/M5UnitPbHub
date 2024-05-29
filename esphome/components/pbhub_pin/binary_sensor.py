import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ID, CONF_PIN, CONF_MODE, CONF_PULLUP

DEPENDENCIES = ['m5unit_pbhub']

pbhub_pin_ns = cg.esphome_ns.namespace('pbhub_pin')
PbHubPinBinarySensor = pbhub_pin_ns.class_('PbHubPinBinarySensor', binary_sensor.BinarySensor)

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

CONFIG_SCHEMA = binary_sensor.binary_sensor_schema(PbHubPinBinarySensor).extend({
    cv.GenerateID(): cv.declare_id(PbHubPinBinarySensor),
    cv.Required(CONF_PIN): PbHubPinSchema,
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    hub = yield cg.get_variable(config[CONF_PIN][CONF_M5UNIT_PBHUB])
    pin_mode = config[CONF_PIN][CONF_MODE]
    var = cg.new_Pvariable(config[CONF_ID], hub, config[CONF_PIN][CONF_NUMBER], pin_mode['pullup'])
    cg.add(var.set_parent(hub))
    cg.add(var.set_inverted(config[CONF_PIN][CONF_INVERTED]))
    yield cg.register_component(var, config)
    yield binary_sensor.register_binary_sensor(var, config)
