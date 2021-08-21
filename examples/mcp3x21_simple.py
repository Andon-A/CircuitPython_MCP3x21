# Basic intro to using the MCP3021 or MCP3221 analog-to-digital converters with CircuitPython
# This example covers basic reads.

# We'll need the board definition, the cp_mcp3x21 library, and time.
import board
import cp_mcp3x21
import time

# Set up our i2c
i2c = board.I2C()

# And set up our device.
# There are 8 chips: MCP3021A0T through MCP3021A7T, and also MCP3221A0T and MCP3221A7T
# The last letters determine the chip's i2c address: A0T with 0x48 through A7T with 0x4f
# Both chips use the same addresses. Microchip Technologies says the A5T is the default,
# so this module will default to the 0x4d address if none is given.
mcp = cp_mcp3x21.MCP3021(i2c)
# If you want to specify an address for another chip, you do it like this:
# mcp = cp_mcp3x21.MCP3021(i2c, 0x4b)
# Similarly, if you want a 3221 chip, you simply call the 3221 class.
# This defaults to the same address, and can take the same address argument.
# mcp = cp_mcp3x21.MCP3221(i2c, 0x4b)

# Now we need to get our value.
# The MCP3021 is 10-bit, so it'll be a value between 0 and 1024
# While the MCP3221 is 12-bit, which gives a value between 0 and 4096
# Either way, the code is the same. Just call mcp.value to get the value.
# The chips are super simple so there's no config or such to deal with.
while True:
    print(mcp.value)
    # No need to spam our serial output, so once every half second is fine.
    time.sleep(0.5)