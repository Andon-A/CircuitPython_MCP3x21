### CircuitPython module for the MCP3021 and MCP3221 ADCs
## Dependencies
This driver depends on:
* [Adafruit CircuitPython](https://github.com/adafruit/circuitpython)
* [Bus Device](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice)

Please ensure all dependencies are available on the CircuitPython filesystem. This is easily achieved by downloading [the Adafruit library and driver bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle).

## Usage Example
See examples/mcp3x21_simple.py for a complete demo. The MCP3021 and MCP3221 function identically as long as the correct class is used.
```
import board
import cp_mcp3x21
import time

i2c = board.I2C()
mcp = cp_mcp3x21.MCP3021(i2c)

while True:
	print(mcp.value)
	time.sleep(0.5)
```

## Contributing
Contributions are welcome! This module uses [Adafruit's code of Conduct](https://github.com/adafruit/circuitpython/blob/main/CODE_OF_CONDUCT.md), so please read this before contributing to help this project stay welcoming. 