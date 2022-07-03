import smartpy as sp

FA2Lib = sp.io.import_script_from_url(
    "https://smartpy.io/templates/fa2_lib.py")


class OwnableFA2NFT(FA2Lib.Admin,
                    FA2Lib.ChangeMetadata,
                    FA2Lib.WithdrawMutez,
                    FA2Lib.MintNft,
                    FA2Lib.BurnNft,
                    FA2Lib.OnchainviewBalanceOf,
                    FA2Lib.Fa2Nft
                    ):

    def __init__(self, admin, metadata, token_metadata={}, ledger={}, policy=None, metadata_base=None):
        FA2Lib.FA2NFT.__init__(self, metadata, token_metadata=token_metadata,
                               ledger=ledger, policy=policy, metadata_base=metadata_base)
        FA2Lib.Admin.__init__(self, admin)