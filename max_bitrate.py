# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
#  Calculates the maximum achievable bitrate
# Parameters:
#  tx_w: Transmitter power in watts
#  tx_gain_db: Transmitter gain in dB
#  freq_hz: Frequency of the transmission in Hz
#  dist_km: Distance between the transmitter and receiver in km
#  rx_gain_db: Receiver gain in dB
#  n0_j: Noise power desnity in W/Hz
#  bw_hz: Bandwidth of the channel in Hz
#  ...
# Output:
#  Outputs the maximum achievable bitrate
#
# Written by Evan Schlein
# Other contributors: None

# import Python modules
import math # math module
import sys # argv

# "constants"
c = 2.99792458e8 # m/s

# initialize script arguments
tx_w = float('nan') # Transmitter power in watts
tx_gain_db = float('nan') # Transmitter gain in dB
freq_hz = float('nan') # Frequency of the transmission in Hz
dist_km = float('nan') # Distance between the transmitter and receiver in km
rx_gain_db = float('nan') # Receiver gain in dB
n0_j = float('nan') # Noise power desnity in W/Hz
bw_hz = float('nan') # Bandwidth of the channel in Hz

# parse script arguments
if len(sys.argv)==8:
  tx_w = float(sys.argv[1])
  tx_gain_db = float(sys.argv[2])
  freq_hz = float(sys.argv[3])
  dist_km = float(sys.argv[4])
  rx_gain_db = float(sys.argv[5])
  n0_j = float(sys.argv[6])
  bw_hz = float(sys.argv[7])
  ...
else:
  print(\
   'Usage: '\
   'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
  )
  exit()

# write script below this line
lam = c/freq_hz

Line_loss = 10**(-1/10)
Atm_loss = 10**(0/10)
tx_gain_linear = 10**(tx_gain_db/10)
rx_gain_linear = 10**(rx_gain_db/10)

C = tx_w * Line_loss * tx_gain_linear * (lam/(4*math.pi*(dist_km*1000)))**2 * Atm_loss * rx_gain_linear
N = n0_j * bw_hz
r_max = bw_hz * math.log2(1 + C/N)

print(math.floor(r_max))