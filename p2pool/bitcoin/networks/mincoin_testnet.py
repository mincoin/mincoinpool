import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '8080d8e9'.decode('hex')
P2P_PORT = 19334
ADDRESS_VERSION = 111
RPC_PORT = 19335
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '195b2e22e075bcd8bf4379b872a279e8974a066a6b3c56bb3f2b20c22b3c3721')) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'test'
        ))
SUBSIDY_FUNC = lambda height: 2*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'tMNC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Mincoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Mincoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mincoin'), 'mincoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://testnet.mincoinexplorer.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://testnet.mincoinexplorer.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://testnet.mincoinexplorer.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.00000546e8
