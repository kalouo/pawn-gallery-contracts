from chinstrap.originations import getContract


def deploy(chinstrapState, network, accounts):
    contract = getContract("test_currency")
    initial_storage = contract.storage.encode(
        {
            "administrator": accounts[0].key.public_key_hash(),
            "last_token_id": 1,
            "ledger": {
                (accounts[1].key.public_key_hash(), 0): 1000*(10**18)
            },
            "metadata": {'': '0x687474703a2f2f6578616d706c652e636f6d'},
            "operators": {},
            "supply": {0: 1000*(10**18)},
            "token_metadata": {
                0: {
                    "token_id": 0,
                    "token_info": {
                        'decimals': '0x3138',
                        'name': '0x4578616d706c6520464132',
                        'symbol': '0x454641322d32'
                    }
                }
            }
        }
    )
    return initial_storage, contract
