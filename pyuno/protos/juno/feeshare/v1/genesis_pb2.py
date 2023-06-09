# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/feeshare/v1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from juno.feeshare.v1 import feeshare_pb2 as juno_dot_feeshare_dot_v1_dot_feeshare__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1ejuno/feeshare/v1/genesis.proto\x12\x10juno.feeshare.v1\x1a\x1fjuno/feeshare/v1/feeshare.proto\x1a\x14gogoproto/gogo.proto"s\n\x0cGenesisState\x12.\n\x06params\x18\x01 \x01(\x0b\x32\x18.juno.feeshare.v1.ParamsB\x04\xc8\xde\x1f\x00\x12\x33\n\tfee_share\x18\x02 \x03(\x0b\x32\x1a.juno.feeshare.v1.FeeShareB\x04\xc8\xde\x1f\x00"\x84\x01\n\x06Params\x12\x18\n\x10\x65nable_fee_share\x18\x01 \x01(\x08\x12H\n\x10\x64\x65veloper_shares\x18\x02 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x16\n\x0e\x61llowed_denoms\x18\x03 \x03(\tB2Z0github.com/CosmosContracts/juno/x/feeshare/typesb\x06proto3'
)


_GENESISSTATE = DESCRIPTOR.message_types_by_name["GenesisState"]
_PARAMS = DESCRIPTOR.message_types_by_name["Params"]
GenesisState = _reflection.GeneratedProtocolMessageType(
    "GenesisState",
    (_message.Message,),
    {
        "DESCRIPTOR": _GENESISSTATE,
        "__module__": "juno.feeshare.v1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:juno.feeshare.v1.GenesisState)
    },
)
_sym_db.RegisterMessage(GenesisState)

Params = _reflection.GeneratedProtocolMessageType(
    "Params",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARAMS,
        "__module__": "juno.feeshare.v1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:juno.feeshare.v1.Params)
    },
)
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"Z0github.com/CosmosContracts/juno/x/feeshare/types"
    )
    _GENESISSTATE.fields_by_name["params"]._options = None
    _GENESISSTATE.fields_by_name["params"]._serialized_options = b"\310\336\037\000"
    _GENESISSTATE.fields_by_name["fee_share"]._options = None
    _GENESISSTATE.fields_by_name["fee_share"]._serialized_options = b"\310\336\037\000"
    _PARAMS.fields_by_name["developer_shares"]._options = None
    _PARAMS.fields_by_name[
        "developer_shares"
    ]._serialized_options = (
        b"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000"
    )
    _GENESISSTATE._serialized_start = 107
    _GENESISSTATE._serialized_end = 222
    _PARAMS._serialized_start = 225
    _PARAMS._serialized_end = 357
# @@protoc_insertion_point(module_scope)
