# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/mint/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from juno.mint import mint_pb2 as juno_dot_mint_dot_mint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17juno/mint/genesis.proto\x12\tjuno.mint\x1a\x14gogoproto/gogo.proto\x1a\x14juno/mint/mint.proto\"`\n\x0cGenesisState\x12\'\n\x06minter\x18\x01 \x01(\x0b\x32\x11.juno.mint.MinterB\x04\xc8\xde\x1f\x00\x12\'\n\x06params\x18\x02 \x01(\x0b\x32\x11.juno.mint.ParamsB\x04\xc8\xde\x1f\x00\x42.Z,github.com/CosmosContracts/juno/x/mint/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'juno.mint.genesis_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/CosmosContracts/juno/x/mint/types'
  _GENESISSTATE.fields_by_name['minter']._options = None
  _GENESISSTATE.fields_by_name['minter']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=82
  _GENESISSTATE._serialized_end=178
# @@protoc_insertion_point(module_scope)
