import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '80f3f8e2'.decode('hex')
P2P_PORT = 19445
ADDRESS_VERSION = 111
RPC_PORT = 19446
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'mincoinaddress' in (yield bitcoind.rpc_help())
        ))
SUBSIDY_FUNC = lambda height: 2*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'rMNC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Mincoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Mincoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mincoin'), 'mincoin.conf')
BLOCK_EXPLORER_URL_PREFIX = '#'
ADDRESS_EXPLORER_URL_PREFIX = '#'
TX_EXPLORER_URL_PREFIX = '#'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.00075e8