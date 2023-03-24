# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: juno/feeshare/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from juno.feeshare.v1 import genesis_pb2 as juno_dot_feeshare_dot_v1_dot_genesis__pb2
from juno.feeshare.v1 import feeshare_pb2 as juno_dot_feeshare_dot_v1_dot_feeshare__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cjuno/feeshare/v1/query.proto\x12\x10juno.feeshare.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1ejuno/feeshare/v1/genesis.proto\x1a\x1fjuno/feeshare/v1/feeshare.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\"S\n\x15QueryFeeSharesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x89\x01\n\x16QueryFeeSharesResponse\x12\x32\n\x08\x66\x65\x65share\x18\x01 \x03(\x0b\x32\x1a.juno.feeshare.v1.FeeShareB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"0\n\x14QueryFeeShareRequest\x12\x18\n\x10\x63ontract_address\x18\x01 \x01(\t\"K\n\x15QueryFeeShareResponse\x12\x32\n\x08\x66\x65\x65share\x18\x01 \x01(\x0b\x32\x1a.juno.feeshare.v1.FeeShareB\x04\xc8\xde\x1f\x00\"\x14\n\x12QueryParamsRequest\"E\n\x13QueryParamsResponse\x12.\n\x06params\x18\x01 \x01(\x0b\x32\x18.juno.feeshare.v1.ParamsB\x04\xc8\xde\x1f\x00\"u\n\x1dQueryDeployerFeeSharesRequest\x12\x18\n\x10\x64\x65ployer_address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"y\n\x1eQueryDeployerFeeSharesResponse\x12\x1a\n\x12\x63ontract_addresses\x18\x01 \x03(\t\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"y\n\x1fQueryWithdrawerFeeSharesRequest\x12\x1a\n\x12withdrawer_address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"{\n QueryWithdrawerFeeSharesResponse\x12\x1a\n\x12\x63ontract_addresses\x18\x01 \x03(\t\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\x8a\x06\n\x05Query\x12\x84\x01\n\tFeeShares\x12\'.juno.feeshare.v1.QueryFeeSharesRequest\x1a(.juno.feeshare.v1.QueryFeeSharesResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/juno/feeshare/v1/fee_shares\x12\x94\x01\n\x08\x46\x65\x65Share\x12&.juno.feeshare.v1.QueryFeeShareRequest\x1a\'.juno.feeshare.v1.QueryFeeShareResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//juno/feeshare/v1/fee_shares/{contract_address}\x12w\n\x06Params\x12$.juno.feeshare.v1.QueryParamsRequest\x1a%.juno.feeshare.v1.QueryParamsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/juno/feeshare/v1/params\x12\xaf\x01\n\x11\x44\x65ployerFeeShares\x12/.juno.feeshare.v1.QueryDeployerFeeSharesRequest\x1a\x30.juno.feeshare.v1.QueryDeployerFeeSharesResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//juno/feeshare/v1/fee_shares/{deployer_address}\x12\xb7\x01\n\x13WithdrawerFeeShares\x12\x31.juno.feeshare.v1.QueryWithdrawerFeeSharesRequest\x1a\x32.juno.feeshare.v1.QueryWithdrawerFeeSharesResponse\"9\x82\xd3\xe4\x93\x02\x33\x12\x31/juno/feeshare/v1/fee_shares/{withdrawer_address}B2Z0github.com/CosmosContracts/juno/x/feeshare/typesb\x06proto3')



_QUERYFEESHARESREQUEST = DESCRIPTOR.message_types_by_name['QueryFeeSharesRequest']
_QUERYFEESHARESRESPONSE = DESCRIPTOR.message_types_by_name['QueryFeeSharesResponse']
_QUERYFEESHAREREQUEST = DESCRIPTOR.message_types_by_name['QueryFeeShareRequest']
_QUERYFEESHARERESPONSE = DESCRIPTOR.message_types_by_name['QueryFeeShareResponse']
_QUERYPARAMSREQUEST = DESCRIPTOR.message_types_by_name['QueryParamsRequest']
_QUERYPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['QueryParamsResponse']
_QUERYDEPLOYERFEESHARESREQUEST = DESCRIPTOR.message_types_by_name['QueryDeployerFeeSharesRequest']
_QUERYDEPLOYERFEESHARESRESPONSE = DESCRIPTOR.message_types_by_name['QueryDeployerFeeSharesResponse']
_QUERYWITHDRAWERFEESHARESREQUEST = DESCRIPTOR.message_types_by_name['QueryWithdrawerFeeSharesRequest']
_QUERYWITHDRAWERFEESHARESRESPONSE = DESCRIPTOR.message_types_by_name['QueryWithdrawerFeeSharesResponse']
QueryFeeSharesRequest = _reflection.GeneratedProtocolMessageType('QueryFeeSharesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYFEESHARESREQUEST,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryFeeSharesRequest)
  })
_sym_db.RegisterMessage(QueryFeeSharesRequest)

QueryFeeSharesResponse = _reflection.GeneratedProtocolMessageType('QueryFeeSharesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYFEESHARESRESPONSE,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryFeeSharesResponse)
  })
_sym_db.RegisterMessage(QueryFeeSharesResponse)

QueryFeeShareRequest = _reflection.GeneratedProtocolMessageType('QueryFeeShareRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYFEESHAREREQUEST,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryFeeShareRequest)
  })
_sym_db.RegisterMessage(QueryFeeShareRequest)

QueryFeeShareResponse = _reflection.GeneratedProtocolMessageType('QueryFeeShareResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYFEESHARERESPONSE,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryFeeShareResponse)
  })
_sym_db.RegisterMessage(QueryFeeShareResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryDeployerFeeSharesRequest = _reflection.GeneratedProtocolMessageType('QueryDeployerFeeSharesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDEPLOYERFEESHARESREQUEST,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryDeployerFeeSharesRequest)
  })
_sym_db.RegisterMessage(QueryDeployerFeeSharesRequest)

QueryDeployerFeeSharesResponse = _reflection.GeneratedProtocolMessageType('QueryDeployerFeeSharesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDEPLOYERFEESHARESRESPONSE,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryDeployerFeeSharesResponse)
  })
_sym_db.RegisterMessage(QueryDeployerFeeSharesResponse)

QueryWithdrawerFeeSharesRequest = _reflection.GeneratedProtocolMessageType('QueryWithdrawerFeeSharesRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYWITHDRAWERFEESHARESREQUEST,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryWithdrawerFeeSharesRequest)
  })
_sym_db.RegisterMessage(QueryWithdrawerFeeSharesRequest)

QueryWithdrawerFeeSharesResponse = _reflection.GeneratedProtocolMessageType('QueryWithdrawerFeeSharesResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYWITHDRAWERFEESHARESRESPONSE,
  '__module__' : 'juno.feeshare.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:juno.feeshare.v1.QueryWithdrawerFeeSharesResponse)
  })
_sym_db.RegisterMessage(QueryWithdrawerFeeSharesResponse)

_QUERY = DESCRIPTOR.services_by_name['Query']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/CosmosContracts/juno/x/feeshare/types'
  _QUERYFEESHARESRESPONSE.fields_by_name['feeshare']._options = None
  _QUERYFEESHARESRESPONSE.fields_by_name['feeshare']._serialized_options = b'\310\336\037\000'
  _QUERYFEESHARERESPONSE.fields_by_name['feeshare']._options = None
  _QUERYFEESHARERESPONSE.fields_by_name['feeshare']._serialized_options = b'\310\336\037\000'
  _QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
  _QUERYPARAMSRESPONSE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _QUERY.methods_by_name['FeeShares']._options = None
  _QUERY.methods_by_name['FeeShares']._serialized_options = b'\202\323\344\223\002\036\022\034/juno/feeshare/v1/fee_shares'
  _QUERY.methods_by_name['FeeShare']._options = None
  _QUERY.methods_by_name['FeeShare']._serialized_options = b'\202\323\344\223\0021\022//juno/feeshare/v1/fee_shares/{contract_address}'
  _QUERY.methods_by_name['Params']._options = None
  _QUERY.methods_by_name['Params']._serialized_options = b'\202\323\344\223\002\032\022\030/juno/feeshare/v1/params'
  _QUERY.methods_by_name['DeployerFeeShares']._options = None
  _QUERY.methods_by_name['DeployerFeeShares']._serialized_options = b'\202\323\344\223\0021\022//juno/feeshare/v1/fee_shares/{deployer_address}'
  _QUERY.methods_by_name['WithdrawerFeeShares']._options = None
  _QUERY.methods_by_name['WithdrawerFeeShares']._serialized_options = b'\202\323\344\223\0023\0221/juno/feeshare/v1/fee_shares/{withdrawer_address}'
  _QUERYFEESHARESREQUEST._serialized_start=211
  _QUERYFEESHARESREQUEST._serialized_end=294
  _QUERYFEESHARESRESPONSE._serialized_start=297
  _QUERYFEESHARESRESPONSE._serialized_end=434
  _QUERYFEESHAREREQUEST._serialized_start=436
  _QUERYFEESHAREREQUEST._serialized_end=484
  _QUERYFEESHARERESPONSE._serialized_start=486
  _QUERYFEESHARERESPONSE._serialized_end=561
  _QUERYPARAMSREQUEST._serialized_start=563
  _QUERYPARAMSREQUEST._serialized_end=583
  _QUERYPARAMSRESPONSE._serialized_start=585
  _QUERYPARAMSRESPONSE._serialized_end=654
  _QUERYDEPLOYERFEESHARESREQUEST._serialized_start=656
  _QUERYDEPLOYERFEESHARESREQUEST._serialized_end=773
  _QUERYDEPLOYERFEESHARESRESPONSE._serialized_start=775
  _QUERYDEPLOYERFEESHARESRESPONSE._serialized_end=896
  _QUERYWITHDRAWERFEESHARESREQUEST._serialized_start=898
  _QUERYWITHDRAWERFEESHARESREQUEST._serialized_end=1019
  _QUERYWITHDRAWERFEESHARESRESPONSE._serialized_start=1021
  _QUERYWITHDRAWERFEESHARESRESPONSE._serialized_end=1144
  _QUERY._serialized_start=1147
  _QUERY._serialized_end=1925
# @@protoc_insertion_point(module_scope)
