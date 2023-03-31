# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/mint/mint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x14juno/mint/mint.proto\x12\tjuno.mint\x1a\x14gogoproto/gogo.proto"\xd9\x02\n\x06Minter\x12\x41\n\tinflation\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\r\n\x05phase\x18\x02 \x01(\x04\x12\x37\n\x11start_phase_block\x18\x03 \x01(\x04\x42\x1c\xf2\xde\x1f\x18yaml:"start_phase_block"\x12\x65\n\x11\x61nnual_provisions\x18\x04 \x01(\tBJ\xf2\xde\x1f\x18yaml:"annual_provisions"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12]\n\rtarget_supply\x18\x05 \x01(\tBF\xf2\xde\x1f\x14yaml:"target_supply"\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00"W\n\x06Params\x12\x12\n\nmint_denom\x18\x01 \x01(\t\x12\x33\n\x0f\x62locks_per_year\x18\x02 \x01(\x04\x42\x1a\xf2\xde\x1f\x16yaml:"blocks_per_year":\x04\x98\xa0\x1f\x00\x42.Z,github.com/CosmosContracts/juno/x/mint/typesb\x06proto3'
)


_MINTER = DESCRIPTOR.message_types_by_name["Minter"]
_PARAMS = DESCRIPTOR.message_types_by_name["Params"]
Minter = _reflection.GeneratedProtocolMessageType(
    "Minter",
    (_message.Message,),
    {
        "DESCRIPTOR": _MINTER,
        "__module__": "juno.mint.mint_pb2"
        # @@protoc_insertion_point(class_scope:juno.mint.Minter)
    },
)
_sym_db.RegisterMessage(Minter)

Params = _reflection.GeneratedProtocolMessageType(
    "Params",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARAMS,
        "__module__": "juno.mint.mint_pb2"
        # @@protoc_insertion_point(class_scope:juno.mint.Params)
    },
)
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z,github.com/CosmosContracts/juno/x/mint/types"
    _MINTER.fields_by_name["inflation"]._options = None
    _MINTER.fields_by_name[
        "inflation"
    ]._serialized_options = (
        b"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000"
    )
    _MINTER.fields_by_name["start_phase_block"]._options = None
    _MINTER.fields_by_name[
        "start_phase_block"
    ]._serialized_options = b'\362\336\037\030yaml:"start_phase_block"'
    _MINTER.fields_by_name["annual_provisions"]._options = None
    _MINTER.fields_by_name[
        "annual_provisions"
    ]._serialized_options = b'\362\336\037\030yaml:"annual_provisions"\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
    _MINTER.fields_by_name["target_supply"]._options = None
    _MINTER.fields_by_name[
        "target_supply"
    ]._serialized_options = b'\362\336\037\024yaml:"target_supply"\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000'
    _PARAMS.fields_by_name["blocks_per_year"]._options = None
    _PARAMS.fields_by_name[
        "blocks_per_year"
    ]._serialized_options = b'\362\336\037\026yaml:"blocks_per_year"'
    _PARAMS._options = None
    _PARAMS._serialized_options = b"\230\240\037\000"
    _MINTER._serialized_start = 58
    _MINTER._serialized_end = 403
    _PARAMS._serialized_start = 405
    _PARAMS._serialized_end = 492
# @@protoc_insertion_point(module_scope)