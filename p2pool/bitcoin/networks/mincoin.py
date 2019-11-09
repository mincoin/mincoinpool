import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '6342212c'.decode('hex')
P2P_PORT = 9334
ADDRESS_VERSION = 50
RPC_PORT = 9335
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '12a765e31ffd4059bada1e25190f6e98c99d9714d334efa41a195a7e7e04bfe2')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 2*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'MNC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Mincoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Mincoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mincoin'), 'mincoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://www.mincoinexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://www.mincoinexplorer.com/address/'
TX_EXPLORER_URL_PREFIX = 'https://www.mincoinexplorer.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.00000546e8
