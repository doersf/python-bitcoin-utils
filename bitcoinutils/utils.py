# Copyright (C) 2018-2020 The python-bitcoin-utils developers
#
# This file is part of python-bitcoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoin-utils, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from binascii import hexlify, unhexlify
from bitcoinutils.constants import SATOSHIS_PER_BITCOIN, AMOUNT_REGEX
from decimal import Decimal, localcontext

'''
Converts from any number type (int/float/Decimal) to satoshis (int)
'''
def to_satoshis(num):
    if (isinstance(num, str) == False):
        raise Exception("Must specify a string for to_satoshis")

    if (AMOUNT_REGEX.match(num) is None):
        raise Exception("Invalid number specified")
    
    with localcontext() as ctx:
        ctx.prec = 28
        return int(Decimal(num) * Decimal("100000000"))


'''
Counts bytes and returns them with their compact size (or varint) prepended.
Accepts bytes and returns bytes.

https://bitcoin.org/en/developer-reference#compactsize-unsigned-integers
'''
def prepend_compact_size(data):
    prefix = encode_var_int(len(data))
    return prefix + data


'''
Returns if an address (string) is bech32 or not
TODO improve by checking if valid, etc.
'''
def is_address_bech32(address):
    if (address.startswith('bc') or
        address.startswith('tb')):
        return True

    return False


def encode_var_int(i):
    """ Encodes integers into variable length integers, which are used in
        Bitcoin in order to save space.
    """
    if not isinstance(i, int) and not isinstance(i, long):
        raise Exception('i must be an integer')
    
    if i <= 0xfc:
        return (i).to_bytes(1, byteorder="little")
    elif i <= 0xffff:
        return b'\xfd' + (i).to_bytes(2, byteorder="little")
    elif i <= 0xffffffff:
        return b'\xfe' + (i).to_bytes(4, byteorder="little")
    elif i <= 0xffffffffffffffff:
        return b'\xff' + (i).to_bytes(8, byteorder="little")
    else:
        raise Exception('Integer cannot exceed 8 bytes in length.')
    
