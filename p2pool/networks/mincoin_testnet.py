from p2pool.bitcoin import networks

PARENT = networks.nets['mincoin_testnet']
SHARE_PERIOD = 6 # seconds
CHAIN_LENGTH =  1000 # shares
REAL_CHAIN_LENGTH = 1000 # shares
TARGET_LOOKBEHIND = 23 # shares
SPREAD = 6 # blocks
IDENTIFIER = '54835b40cea547fc'.decode('hex')
PREFIX = '11cdc73f5c97f4b4'.decode('hex')
P2P_PORT = 20334
MIN_TARGET = 0
MAX_TARGET = 2**256//2**12 - 1
PERSIST = True
WORKER_PORT = 20335
BOOTSTRAP_ADDRS = '3.224.251.96 3.9.203.237'.split(' ')
ANNOUNCE_CHANNEL = '#mincoinpool'
VERSION_CHECK = lambda v: None if 140300 <= v else 'Mincoin version too old. Upgrade to 0.14.3 or newer!'
VERSION_WARNING = lambda v: None
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
MINIMUM_PROTOCOL_VERSION = 1700
NEW_MINIMUM_PROTOCOL_VERSION = 1700
SEGWIT_ACTIVATION_VERSION = 17
