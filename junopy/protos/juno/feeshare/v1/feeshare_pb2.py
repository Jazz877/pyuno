# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/feeshare/v1/feeshare.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fjuno/feeshare/v1/feeshare.proto\x12\x10juno.feeshare.v1\"Z\n\x08\x46\x65\x65Share\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\x12\x18\n\x10\x64\x65ployer_address\x18\x02 \x01(\t\x12\x1a\n\x12withdrawer_address\x18\x03 \x01(\tB2Z0github.com/CosmosContracts/juno/x/feeshare/typesb\x06proto3')



_FEESHARE = DESCRIPTOR.message_types_by_name['FeeShare']
FeeShare = _reflection.GeneratedProtocolMessageType('FeeShare', (_message.Message,), {
  'DESCRIPTOR' : _FEESHARE,
  '__module__' : 'juno.feeshare.v1.feeshare_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.FeeShare)
  })
_sym_db.RegisterMessage(FeeShare)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/CosmosContracts/juno/x/feeshare/types'
  _FEESHARE._serialized_start=53
  _FEESHARE._serialized_end=143
# @@protoc_insertion_point(module_scope)
