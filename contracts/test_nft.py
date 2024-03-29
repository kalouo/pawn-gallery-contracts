import smartpy as sp

LibFA2 = sp.io.import_script_from_url("file:""contracts/lib/FA2_lib.py")
Constants = sp.io.import_script_from_url("file:contracts/lib/constants.py")


class TestNFT(LibFA2.OwnableFA2NFT):

    def __init__(self, admin, metadata, token_metadata={}, ledger={}, policy=None, metadata_base=None):
        LibFA2.OwnableFA2NFT.__init__(
            self, admin, metadata, token_metadata, ledger, policy, metadata_base)


NFT1 = LibFA2.Utils.make_metadata(
    name="Example FA2",
    decimals=0,
    symbol="EFA2-2")


sp.add_compilation_target(
    "test_nft",
    TestNFT(
        admin=Constants.NULL_ADDRESS,
        metadata=sp.utils.metadata_of_url("http://example.com"),
        ledger={0: Constants.NULL_ADDRESS},
        token_metadata=[NFT1]
    ))
