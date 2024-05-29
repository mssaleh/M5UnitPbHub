import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output, i2c
from esphome.const import CONF_CHANNEL, CONF_ID, CONF_I2C_ADDRESS

DEPENDENCIES = ["i2c"]

m5unit_pbhub_ns = cg.esphome_ns.namespace("m5unit_pbhub")
M5UnitPbHubOutput = m5unit_pbhub_ns.class_("M5UnitPbHubOutput", output.BinaryOutput, i2c.I2CDevice)

CONFIG_SCHEMA = output.BINARY_OUTPUT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(M5UnitPbHubOutput),
        cv.Optional(CONF_I2C_ADDRESS, default=0x61): cv.i2c_address,
        cv.Required(CONF_CHANNEL): cv.int_range(min=0, max=5),
    }
).extend(i2c.i2c_device_schema(0x61))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await output.register_output(var, config)
    await i2c.register_i2c_device(var, config)

    cg.add(var.set_channel(config[CONF_CHANNEL]))