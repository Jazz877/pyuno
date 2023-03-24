# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/mint/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from juno.mint import mint_pb2 as juno_dot_mint_dot_mint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15juno/mint/query.proto\x12\tjuno.mint\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x14juno/mint/mint.proto\"\x14\n\x12QueryParamsRequest\">\n\x13QueryParamsResponse\x12\'\n\x06params\x18\x01 \x01(\x0b\x32\x11.juno.mint.ParamsB\x04\xc8\xde\x1f\x00\"\x17\n\x15QueryInflationRequest\"[\n\x16QueryInflationResponse\x12\x41\n\tinflation\x18\x01 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x1e\n\x1cQueryAnnualProvisionsRequest\"j\n\x1dQueryAnnualProvisionsResponse\x12I\n\x11\x61nnual_provisions\x18\x01 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x32\x87\x03\n\x05Query\x12l\n\x06Params\x12\x1d.juno.mint.QueryParamsRequest\x1a\x1e.juno.mint.QueryParamsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/mint/v1beta1/params\x12x\n\tInflation\x12 .juno.mint.QueryInflationRequest\x1a!.juno.mint.QueryInflationResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/mint/v1beta1/inflation\x12\x95\x01\n\x10\x41nnualProvisions\x12\'.juno.mint.QueryAnnualProvisionsRequest\x1a(.juno.mint.QueryAnnualProvisionsResponse\".\x82\xd3\xe4\x93\x02(\x12&/cosmos/mint/v1beta1/annual_provisionsB.Z,github.com/CosmosContracts/juno/x/mint/typesb\x06proto3')



_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYINFLATIONREQUEST = DESCRIPTOR.message_types_by_name['QueryInflationRequest']
_QUERYINFLATIONRESPONSE = DESCRIPTOR.message_types_by_name['QueryInflationResponse']
_QUERYANNUALPROVISIONSREQUEST = DESCRIPTOR.message_types_by_name['QueryAnnualProvisionsRequest']
_QUERYANNUALPROVISIONSRESPONSE = DESCRIPTOR.message_types_by_name['QueryAnnualProvisionsResponse']
QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'juno.mint.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'juno.mint.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryInflationRequest = _reflection.GeneratedProtocolMessageType('QueryInflationRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINFLATIONREQUEST,
  '__module__' : 'juno.mint.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.QueryInflationRequest)
  })
_sym_db.RegisterMessage(QueryInflationRequest)

QueryInflationResponse = _reflection.GeneratedProtocolMessageType('QueryInflationResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYINFLATIONRESPONSE,
  '__module__' : 'juno.mint.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.QueryInflationResponse)
  })
_sym_db.RegisterMessage(QueryInflationResponse)

QueryAnnualProvisionsRequest = _reflection.GeneratedProtocolMessageType('QueryAnnualProvisionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYANNUALPROVISIONSREQUEST,
  '__module__' : 'juno.mint.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.QueryAnnualProvisionsRequest)
  })
_sym_db.RegisterMessage(QueryAnnualProvisionsRequest)

QueryAnnualProvisionsResponse = _reflection.GeneratedProtocolMessageType('QueryAnnualProvisionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYANNUALPROVISIONSRESPONSE,
  '__module__' : 'juno.mint.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.mint.QueryAnnualProvisionsResponse)
  })
_sym_db.RegisterMessage(QueryAnnualProvisionsResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/CosmosContracts/juno/x/mint/types'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERYINFLATIONRESPONSE.fields_by_name['inflation']._options = None
  _QUERYINFLATIONRESPONSE.fields_by_name['inflation']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERYANNUALPROVISIONSRESPONSE.fields_by_name['annual_provisions']._options = None
  _QUERYANNUALPROVISIONSRESPONSE.fields_by_name['annual_provisions']._serialized_options = b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\035\022\033/cosmos/mint/v1beta1/params'
  _QUERY.methods_by_name['Inflation']._options = None
  _QUERY.methods_by_name['Inflation']._serialized_options = b'\202\323\344\223\002 \022\036/cosmos/mint/v1beta1/inflation'
  _QUERY.methods_by_name['AnnualProvisions']._options = None
  _QUERY.methods_by_name['AnnualProvisions']._serialized_options = b'\202\323\344\223\002(\022&/cosmos/mint/v1beta1/annual_provisions'
  _QUERYPARAMSREQUEST._serialized_start=110
  _QUERYPARAMSREQUEST._serialized_end=130
  _QUERYPARAMSRESPONSE._serialized_start=132
  _QUERYPARAMSRESPONSE._serialized_end=194
  _QUERYINFLATIONREQUEST._serialized_start=196
  _QUERYINFLATIONREQUEST._serialized_end=219
  _QUERYINFLATIONRESPONSE._serialized_start=221
  _QUERYINFLATIONRESPONSE._serialized_end=312
  _QUERYANNUALPROVISIONSREQUEST._serialized_start=314
  _QUERYANNUALPROVISIONSREQUEST._serialized_end=344
  _QUERYANNUALPROVISIONSRESPONSE._serialized_start=346
  _QUERYANNUALPROVISIONSRESPONSE._serialized_end=452
  _QUERY._serialized_start=455
  _QUERY._serialized_end=846
# @@protoc_insertion_point(module_scope)
