# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/oracle/v1/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bjuno/oracle/v1/events.proto\x12\x0ejuno.oracle.v1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\"r\n\x18\x45ventDelegateFeedConsent\x12*\n\x08operator\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\x12*\n\x08\x64\x65legate\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressString\"k\n\x0e\x45ventSetFxRate\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12J\n\x04rate\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x42\x34Z.github.com/CosmosContracts/juno/x/oracle/types\xc8\xe1\x1e\x00\x62\x06proto3')



_EVENTDELEGATEFEEDCONSENT = DESCRIPTOR.message_types_by_name['EventDelegateFeedConsent']
_EVENTSETFXRATE = DESCRIPTOR.message_types_by_name['EventSetFxRate']
EventDelegateFeedConsent = _reflection.GeneratedProtocolMessageType('EventDelegateFeedConsent', (_message.Message,), {
  'DESCRIPTOR' : _EVENTDELEGATEFEEDCONSENT,
  '__module__' : 'juno.oracle.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:juno.oracle.v1.EventDelegateFeedConsent)
  })
_sym_db.RegisterMessage(EventDelegateFeedConsent)

EventSetFxRate = _reflection.GeneratedProtocolMessageType('EventSetFxRate', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSETFXRATE,
  '__module__' : 'juno.oracle.v1.events_pb2'
  # @@protoc_insertion_point(class_scope:juno.oracle.v1.EventSetFxRate)
  })
_sym_db.RegisterMessage(EventSetFxRate)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/CosmosContracts/juno/x/oracle/types\310\341\036\000'
  _EVENTDELEGATEFEEDCONSENT.fields_by_name['operator']._options = None
  _EVENTDELEGATEFEEDCONSENT.fields_by_name['operator']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EVENTDELEGATEFEEDCONSENT.fields_by_name['delegate']._options = None
  _EVENTDELEGATEFEEDCONSENT.fields_by_name['delegate']._serialized_options = b'\322\264-\024cosmos.AddressString'
  _EVENTSETFXRATE.fields_by_name['rate']._options = None
  _EVENTSETFXRATE.fields_by_name['rate']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _EVENTDELEGATEFEEDCONSENT._serialized_start=96
  _EVENTDELEGATEFEEDCONSENT._serialized_end=210
  _EVENTSETFXRATE._serialized_start=212
  _EVENTSETFXRATE._serialized_end=319
# @@protoc_insertion_point(module_scope)
