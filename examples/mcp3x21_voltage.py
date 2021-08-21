# An intro to getting a voltage value.
# This can either be "raw" voltage fed into the chip at the operating voltage
# Which will often be your microcontroller's 3.3 or 5v, since it works with both.
# Or you can run it through a voltage divider to get a range you need.
# This example assumes you know about voltage dividers, as there's better sources
# than me to explain them.

import board
import cp_mcp3x21
import time

i2c = board.I2C()

# Change this to whichever chip you have.
mcp = cp_mcp3x21.MCP3021(i2c, 0x4d)
# mcp = cp_mcp3x21.MCP3221(i2c, 0x4d)

# Now we want our voltage calculator.
def get_voltage(value, ref, max_value=1024):
    # Our value will be between 0 and either 1024 or 4096, depending.
    # We'll default to the max being 1024, but that can be changed.
    value = float(value) # We want the final result to be a float anyway.
    # What we do here is take the proportion of the value to the max value
    # And multiply that by the voltage we're measuring.
    # So if we have a lipo battery that tops out at 4.2v, we'd use 4.2 as
    # the reference. If our reading is 900 out of 1024, that's 0.88 (ish),
    # multiplied by 4.2 gives us 3.7v, or a usual battery charge. If it was
    # around 780, that'd be at 3.2 volts, or worryingly dead.
    volts = (value / max_value) * ref
    return volts

# And our loop.
while True:
    value = mcp.value
    # We'll presume we're using a 3.3v microcontroller and are using this
    # to read a 3.3v input.
    print(value, get_voltage(value, 3.3, 1024)
    # If you're using an MCP3221, use the following
    # print(value, get_voltage(value, 3.3, 4096)
    time.sleep(0.5)
    