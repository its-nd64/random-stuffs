from machine import Pin, SPI
from nrf24l01 import NRF24L01

spi0 = SPI(0, baudrate=4000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
csn0 = Pin(17, mode=Pin.OUT, value=1)
ce0 = Pin(20, mode=Pin.OUT, value=0)
radio0 = NRF24L01(spi0, csn0, ce0)

# Disable Auto Acknowledgment (EN_AA)
radio0.reg_write(0x01, 0x00)

# Stop Listening (CONFIG)
config = radio0.reg_read(0x00)
radio0.reg_write(0x00, config & 0xFE)

# Set Retries to 0 (SETUP_RETR)
radio0.reg_write(0x04, 0x00)

# Set Power Level to Max and Data Rate to 2Mbps (RF_SETUP)
rf_setup = radio0.reg_read(0x06)
radio0.reg_write(0x06, (rf_setup & 0b11110000) | 0b00001110)  # PWR_MAX and SPEED_2MBPS

# Disable CRC (CONFIG)
config = radio0.reg_read(0x00)
radio0.reg_write(0x00, config & 0xF3)

# Start Constant Carrier Transmission
radio0.reg_write(0x07, 0x70)  # Clear any pending interrupts
radio0.reg_write(0x05, 27)  # Set RF Channel to 0
radio0.reg_write(0x00, 0x02)  # Set PWR_UP and PLL_LOCK

ce0.on()  # Start transmission


# while True:
#     for i in range(12, 73, 5):
#         radio0.reg_write(0x05, i)
