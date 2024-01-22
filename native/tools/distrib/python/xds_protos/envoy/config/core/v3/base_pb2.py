# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/base.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import address_pb2 as envoy_dot_config_dot_core_dot_v3_dot_address__pb2
from envoy.config.core.v3 import backoff_pb2 as envoy_dot_config_dot_core_dot_v3_dot_backoff__pb2
from envoy.config.core.v3 import http_uri_pb2 as envoy_dot_config_dot_core_dot_v3_dot_http__uri__pb2
from envoy.type.v3 import percent_pb2 as envoy_dot_type_dot_v3_dot_percent__pb2
from envoy.type.v3 import semantic_version_pb2 as envoy_dot_type_dot_v3_dot_semantic__version__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from xds.core.v3 import context_params_pb2 as xds_dot_core_dot_v3_dot_context__params__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x65nvoy/config/core/v3/base.proto\x12\x14\x65nvoy.config.core.v3\x1a\"envoy/config/core/v3/address.proto\x1a\"envoy/config/core/v3/backoff.proto\x1a#envoy/config/core/v3/http_uri.proto\x1a\x1b\x65nvoy/type/v3/percent.proto\x1a$envoy/type/v3/semantic_version.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a xds/core/v3/context_params.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"]\n\x08Locality\x12\x0e\n\x06region\x18\x01 \x01(\t\x12\x0c\n\x04zone\x18\x02 \x01(\t\x12\x10\n\x08sub_zone\x18\x03 \x01(\t:!\x9a\xc5\x88\x1e\x1c\n\x1a\x65nvoy.api.v2.core.Locality\"\x91\x01\n\x0c\x42uildVersion\x12/\n\x07version\x18\x01 \x01(\x0b\x32\x1e.envoy.type.v3.SemanticVersion\x12)\n\x08metadata\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.api.v2.core.BuildVersion\"\xcf\x01\n\tExtension\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x02 \x01(\t\x12$\n\x0ftype_descriptor\x18\x03 \x01(\tB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12\x33\n\x07version\x18\x04 \x01(\x0b\x32\".envoy.config.core.v3.BuildVersion\x12\x10\n\x08\x64isabled\x18\x05 \x01(\x08\x12\x11\n\ttype_urls\x18\x06 \x03(\t:\"\x9a\xc5\x88\x1e\x1d\n\x1b\x65nvoy.api.v2.core.Extension\"\x8a\x05\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x63luster\x18\x02 \x01(\t\x12)\n\x08metadata\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12M\n\x12\x64ynamic_parameters\x18\x0c \x03(\x0b\x32\x31.envoy.config.core.v3.Node.DynamicParametersEntry\x12\x30\n\x08locality\x18\x04 \x01(\x0b\x32\x1e.envoy.config.core.v3.Locality\x12\x17\n\x0fuser_agent_name\x18\x06 \x01(\t\x12\x1c\n\x12user_agent_version\x18\x07 \x01(\tH\x00\x12\x46\n\x18user_agent_build_version\x18\x08 \x01(\x0b\x32\".envoy.config.core.v3.BuildVersionH\x00\x12\x33\n\nextensions\x18\t \x03(\x0b\x32\x1f.envoy.config.core.v3.Extension\x12\x17\n\x0f\x63lient_features\x18\n \x03(\t\x12G\n\x13listening_addresses\x18\x0b \x03(\x0b\x32\x1d.envoy.config.core.v3.AddressB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x1aT\n\x16\x44ynamicParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.xds.core.v3.ContextParams:\x02\x38\x01:\x1d\x9a\xc5\x88\x1e\x18\n\x16\x65nvoy.api.v2.core.NodeB\x19\n\x17user_agent_version_typeJ\x04\x08\x05\x10\x06R\rbuild_version\"\xf4\x02\n\x08Metadata\x12K\n\x0f\x66ilter_metadata\x18\x01 \x03(\x0b\x32\x32.envoy.config.core.v3.Metadata.FilterMetadataEntry\x12V\n\x15typed_filter_metadata\x18\x02 \x03(\x0b\x32\x37.envoy.config.core.v3.Metadata.TypedFilterMetadataEntry\x1aN\n\x13\x46ilterMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01\x1aP\n\x18TypedFilterMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01:!\x9a\xc5\x88\x1e\x1c\n\x1a\x65nvoy.api.v2.core.Metadata\"l\n\rRuntimeUInt32\x12\x15\n\rdefault_value\x18\x02 \x01(\r\x12\x1c\n\x0bruntime_key\x18\x03 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.api.v2.core.RuntimeUInt32\"]\n\x0eRuntimePercent\x12-\n\rdefault_value\x18\x01 \x01(\x0b\x32\x16.envoy.type.v3.Percent\x12\x1c\n\x0bruntime_key\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\"l\n\rRuntimeDouble\x12\x15\n\rdefault_value\x18\x01 \x01(\x01\x12\x1c\n\x0bruntime_key\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.api.v2.core.RuntimeDouble\"\x9c\x01\n\x12RuntimeFeatureFlag\x12;\n\rdefault_value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x1c\n\x0bruntime_key\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01:+\x9a\xc5\x88\x1e&\n$envoy.api.v2.core.RuntimeFeatureFlag\"5\n\x0eQueryParameter\x12\x14\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\r\n\x05value\x18\x02 \x01(\t\"s\n\x0bHeaderValue\x12\x1e\n\x03key\x18\x01 \x01(\tB\x11\xfa\x42\x0er\x0c\x10\x01(\x80\x80\x01\xc0\x01\x01\xc8\x01\x00\x12\x1e\n\x05value\x18\x02 \x01(\tB\x0f\xfa\x42\x0cr\n(\x80\x80\x01\xc0\x01\x02\xc8\x01\x00:$\x9a\xc5\x88\x1e\x1f\n\x1d\x65nvoy.api.v2.core.HeaderValue\"\x92\x03\n\x11HeaderValueOption\x12;\n\x06header\x18\x01 \x01(\x0b\x32!.envoy.config.core.v3.HeaderValueB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x37\n\x06\x61ppend\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12[\n\rappend_action\x18\x03 \x01(\x0e\x32:.envoy.config.core.v3.HeaderValueOption.HeaderAppendActionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x18\n\x10keep_empty_value\x18\x04 \x01(\x08\"d\n\x12HeaderAppendAction\x12\x1b\n\x17\x41PPEND_IF_EXISTS_OR_ADD\x10\x00\x12\x11\n\rADD_IF_ABSENT\x10\x01\x12\x1e\n\x1aOVERWRITE_IF_EXISTS_OR_ADD\x10\x02:*\x9a\xc5\x88\x1e%\n#envoy.api.v2.core.HeaderValueOption\"c\n\tHeaderMap\x12\x32\n\x07headers\x18\x01 \x03(\x0b\x32!.envoy.config.core.v3.HeaderValue:\"\x9a\xc5\x88\x1e\x1d\n\x1b\x65nvoy.api.v2.core.HeaderMap\")\n\x10WatchedDirectory\x12\x15\n\x04path\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\"\xba\x01\n\nDataSource\x12\x1b\n\x08\x66ilename\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00\x12\x16\n\x0cinline_bytes\x18\x02 \x01(\x0cH\x00\x12\x17\n\rinline_string\x18\x03 \x01(\tH\x00\x12\'\n\x14\x65nvironment_variable\x18\x04 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00:#\x9a\xc5\x88\x1e\x1e\n\x1c\x65nvoy.api.v2.core.DataSourceB\x10\n\tspecifier\x12\x03\xf8\x42\x01\"\xba\x01\n\x0bRetryPolicy\x12=\n\x0eretry_back_off\x18\x01 \x01(\x0b\x32%.envoy.config.core.v3.BackoffStrategy\x12\x46\n\x0bnum_retries\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x13\xf2\x98\xfe\x8f\x05\r\n\x0bmax_retries:$\x9a\xc5\x88\x1e\x1f\n\x1d\x65nvoy.api.v2.core.RetryPolicy\"\xca\x01\n\x10RemoteDataSource\x12\x39\n\x08http_uri\x18\x01 \x01(\x0b\x32\x1d.envoy.config.core.v3.HttpUriB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x17\n\x06sha256\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x37\n\x0cretry_policy\x18\x03 \x01(\x0b\x32!.envoy.config.core.v3.RetryPolicy:)\x9a\xc5\x88\x1e$\n\"envoy.api.v2.core.RemoteDataSource\"\xba\x01\n\x0f\x41syncDataSource\x12\x31\n\x05local\x18\x01 \x01(\x0b\x32 .envoy.config.core.v3.DataSourceH\x00\x12\x38\n\x06remote\x18\x02 \x01(\x0b\x32&.envoy.config.core.v3.RemoteDataSourceH\x00:(\x9a\xc5\x88\x1e#\n!envoy.api.v2.core.AsyncDataSourceB\x10\n\tspecifier\x12\x03\xf8\x42\x01\"\x9d\x01\n\x0fTransportSocket\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12,\n\x0ctyped_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00:(\x9a\xc5\x88\x1e#\n!envoy.api.v2.core.TransportSocketB\r\n\x0b\x63onfig_typeJ\x04\x08\x02\x10\x03R\x06\x63onfig\"\xa5\x01\n\x18RuntimeFractionalPercent\x12\x41\n\rdefault_value\x18\x01 \x01(\x0b\x32 .envoy.type.v3.FractionalPercentB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x13\n\x0bruntime_key\x18\x02 \x01(\t:1\x9a\xc5\x88\x1e,\n*envoy.api.v2.core.RuntimeFractionalPercent\"I\n\x0c\x43ontrolPlane\x12\x12\n\nidentifier\x18\x01 \x01(\t:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.api.v2.core.ControlPlane*(\n\x0fRoutingPriority\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04HIGH\x10\x01*\x89\x01\n\rRequestMethod\x12\x16\n\x12METHOD_UNSPECIFIED\x10\x00\x12\x07\n\x03GET\x10\x01\x12\x08\n\x04HEAD\x10\x02\x12\x08\n\x04POST\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\x0b\n\x07\x43ONNECT\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07\x12\t\n\x05TRACE\x10\x08\x12\t\n\x05PATCH\x10\t*>\n\x10TrafficDirection\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07INBOUND\x10\x01\x12\x0c\n\x08OUTBOUND\x10\x02\x42}\n\"io.envoyproxy.envoy.config.core.v3B\tBaseProtoP\x01ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.core.v3.base_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"io.envoyproxy.envoy.config.core.v3B\tBaseProtoP\001ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\272\200\310\321\006\002\020\002'
  _LOCALITY._options = None
  _LOCALITY._serialized_options = b'\232\305\210\036\034\n\032envoy.api.v2.core.Locality'
  _BUILDVERSION._options = None
  _BUILDVERSION._serialized_options = b'\232\305\210\036 \n\036envoy.api.v2.core.BuildVersion'
  _EXTENSION.fields_by_name['type_descriptor']._options = None
  _EXTENSION.fields_by_name['type_descriptor']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _EXTENSION._options = None
  _EXTENSION._serialized_options = b'\232\305\210\036\035\n\033envoy.api.v2.core.Extension'
  _NODE_DYNAMICPARAMETERSENTRY._options = None
  _NODE_DYNAMICPARAMETERSENTRY._serialized_options = b'8\001'
  _NODE.fields_by_name['listening_addresses']._options = None
  _NODE.fields_by_name['listening_addresses']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _NODE._options = None
  _NODE._serialized_options = b'\232\305\210\036\030\n\026envoy.api.v2.core.Node'
  _METADATA_FILTERMETADATAENTRY._options = None
  _METADATA_FILTERMETADATAENTRY._serialized_options = b'8\001'
  _METADATA_TYPEDFILTERMETADATAENTRY._options = None
  _METADATA_TYPEDFILTERMETADATAENTRY._serialized_options = b'8\001'
  _METADATA._options = None
  _METADATA._serialized_options = b'\232\305\210\036\034\n\032envoy.api.v2.core.Metadata'
  _RUNTIMEUINT32.fields_by_name['runtime_key']._options = None
  _RUNTIMEUINT32.fields_by_name['runtime_key']._serialized_options = b'\372B\004r\002\020\001'
  _RUNTIMEUINT32._options = None
  _RUNTIMEUINT32._serialized_options = b'\232\305\210\036!\n\037envoy.api.v2.core.RuntimeUInt32'
  _RUNTIMEPERCENT.fields_by_name['runtime_key']._options = None
  _RUNTIMEPERCENT.fields_by_name['runtime_key']._serialized_options = b'\372B\004r\002\020\001'
  _RUNTIMEDOUBLE.fields_by_name['runtime_key']._options = None
  _RUNTIMEDOUBLE.fields_by_name['runtime_key']._serialized_options = b'\372B\004r\002\020\001'
  _RUNTIMEDOUBLE._options = None
  _RUNTIMEDOUBLE._serialized_options = b'\232\305\210\036!\n\037envoy.api.v2.core.RuntimeDouble'
  _RUNTIMEFEATUREFLAG.fields_by_name['default_value']._options = None
  _RUNTIMEFEATUREFLAG.fields_by_name['default_value']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RUNTIMEFEATUREFLAG.fields_by_name['runtime_key']._options = None
  _RUNTIMEFEATUREFLAG.fields_by_name['runtime_key']._serialized_options = b'\372B\004r\002\020\001'
  _RUNTIMEFEATUREFLAG._options = None
  _RUNTIMEFEATUREFLAG._serialized_options = b'\232\305\210\036&\n$envoy.api.v2.core.RuntimeFeatureFlag'
  _QUERYPARAMETER.fields_by_name['key']._options = None
  _QUERYPARAMETER.fields_by_name['key']._serialized_options = b'\372B\004r\002\020\001'
  _HEADERVALUE.fields_by_name['key']._options = None
  _HEADERVALUE.fields_by_name['key']._serialized_options = b'\372B\016r\014\020\001(\200\200\001\300\001\001\310\001\000'
  _HEADERVALUE.fields_by_name['value']._options = None
  _HEADERVALUE.fields_by_name['value']._serialized_options = b'\372B\014r\n(\200\200\001\300\001\002\310\001\000'
  _HEADERVALUE._options = None
  _HEADERVALUE._serialized_options = b'\232\305\210\036\037\n\035envoy.api.v2.core.HeaderValue'
  _HEADERVALUEOPTION.fields_by_name['header']._options = None
  _HEADERVALUEOPTION.fields_by_name['header']._serialized_options = b'\372B\005\212\001\002\020\001'
  _HEADERVALUEOPTION.fields_by_name['append']._options = None
  _HEADERVALUEOPTION.fields_by_name['append']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _HEADERVALUEOPTION.fields_by_name['append_action']._options = None
  _HEADERVALUEOPTION.fields_by_name['append_action']._serialized_options = b'\372B\005\202\001\002\020\001'
  _HEADERVALUEOPTION._options = None
  _HEADERVALUEOPTION._serialized_options = b'\232\305\210\036%\n#envoy.api.v2.core.HeaderValueOption'
  _HEADERMAP._options = None
  _HEADERMAP._serialized_options = b'\232\305\210\036\035\n\033envoy.api.v2.core.HeaderMap'
  _WATCHEDDIRECTORY.fields_by_name['path']._options = None
  _WATCHEDDIRECTORY.fields_by_name['path']._serialized_options = b'\372B\004r\002\020\001'
  _DATASOURCE.oneofs_by_name['specifier']._options = None
  _DATASOURCE.oneofs_by_name['specifier']._serialized_options = b'\370B\001'
  _DATASOURCE.fields_by_name['filename']._options = None
  _DATASOURCE.fields_by_name['filename']._serialized_options = b'\372B\004r\002\020\001'
  _DATASOURCE.fields_by_name['environment_variable']._options = None
  _DATASOURCE.fields_by_name['environment_variable']._serialized_options = b'\372B\004r\002\020\001'
  _DATASOURCE._options = None
  _DATASOURCE._serialized_options = b'\232\305\210\036\036\n\034envoy.api.v2.core.DataSource'
  _RETRYPOLICY.fields_by_name['num_retries']._options = None
  _RETRYPOLICY.fields_by_name['num_retries']._serialized_options = b'\362\230\376\217\005\r\n\013max_retries'
  _RETRYPOLICY._options = None
  _RETRYPOLICY._serialized_options = b'\232\305\210\036\037\n\035envoy.api.v2.core.RetryPolicy'
  _REMOTEDATASOURCE.fields_by_name['http_uri']._options = None
  _REMOTEDATASOURCE.fields_by_name['http_uri']._serialized_options = b'\372B\005\212\001\002\020\001'
  _REMOTEDATASOURCE.fields_by_name['sha256']._options = None
  _REMOTEDATASOURCE.fields_by_name['sha256']._serialized_options = b'\372B\004r\002\020\001'
  _REMOTEDATASOURCE._options = None
  _REMOTEDATASOURCE._serialized_options = b'\232\305\210\036$\n\"envoy.api.v2.core.RemoteDataSource'
  _ASYNCDATASOURCE.oneofs_by_name['specifier']._options = None
  _ASYNCDATASOURCE.oneofs_by_name['specifier']._serialized_options = b'\370B\001'
  _ASYNCDATASOURCE._options = None
  _ASYNCDATASOURCE._serialized_options = b'\232\305\210\036#\n!envoy.api.v2.core.AsyncDataSource'
  _TRANSPORTSOCKET.fields_by_name['name']._options = None
  _TRANSPORTSOCKET.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _TRANSPORTSOCKET._options = None
  _TRANSPORTSOCKET._serialized_options = b'\232\305\210\036#\n!envoy.api.v2.core.TransportSocket'
  _RUNTIMEFRACTIONALPERCENT.fields_by_name['default_value']._options = None
  _RUNTIMEFRACTIONALPERCENT.fields_by_name['default_value']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RUNTIMEFRACTIONALPERCENT._options = None
  _RUNTIMEFRACTIONALPERCENT._serialized_options = b'\232\305\210\036,\n*envoy.api.v2.core.RuntimeFractionalPercent'
  _CONTROLPLANE._options = None
  _CONTROLPLANE._serialized_options = b'\232\305\210\036 \n\036envoy.api.v2.core.ControlPlane'
  _globals['_ROUTINGPRIORITY']._serialized_start=4367
  _globals['_ROUTINGPRIORITY']._serialized_end=4407
  _globals['_REQUESTMETHOD']._serialized_start=4410
  _globals['_REQUESTMETHOD']._serialized_end=4547
  _globals['_TRAFFICDIRECTION']._serialized_start=4549
  _globals['_TRAFFICDIRECTION']._serialized_end=4611
  _globals['_LOCALITY']._serialized_start=516
  _globals['_LOCALITY']._serialized_end=609
  _globals['_BUILDVERSION']._serialized_start=612
  _globals['_BUILDVERSION']._serialized_end=757
  _globals['_EXTENSION']._serialized_start=760
  _globals['_EXTENSION']._serialized_end=967
  _globals['_NODE']._serialized_start=970
  _globals['_NODE']._serialized_end=1620
  _globals['_NODE_DYNAMICPARAMETERSENTRY']._serialized_start=1457
  _globals['_NODE_DYNAMICPARAMETERSENTRY']._serialized_end=1541
  _globals['_METADATA']._serialized_start=1623
  _globals['_METADATA']._serialized_end=1995
  _globals['_METADATA_FILTERMETADATAENTRY']._serialized_start=1800
  _globals['_METADATA_FILTERMETADATAENTRY']._serialized_end=1878
  _globals['_METADATA_TYPEDFILTERMETADATAENTRY']._serialized_start=1880
  _globals['_METADATA_TYPEDFILTERMETADATAENTRY']._serialized_end=1960
  _globals['_RUNTIMEUINT32']._serialized_start=1997
  _globals['_RUNTIMEUINT32']._serialized_end=2105
  _globals['_RUNTIMEPERCENT']._serialized_start=2107
  _globals['_RUNTIMEPERCENT']._serialized_end=2200
  _globals['_RUNTIMEDOUBLE']._serialized_start=2202
  _globals['_RUNTIMEDOUBLE']._serialized_end=2310
  _globals['_RUNTIMEFEATUREFLAG']._serialized_start=2313
  _globals['_RUNTIMEFEATUREFLAG']._serialized_end=2469
  _globals['_QUERYPARAMETER']._serialized_start=2471
  _globals['_QUERYPARAMETER']._serialized_end=2524
  _globals['_HEADERVALUE']._serialized_start=2526
  _globals['_HEADERVALUE']._serialized_end=2641
  _globals['_HEADERVALUEOPTION']._serialized_start=2644
  _globals['_HEADERVALUEOPTION']._serialized_end=3046
  _globals['_HEADERVALUEOPTION_HEADERAPPENDACTION']._serialized_start=2902
  _globals['_HEADERVALUEOPTION_HEADERAPPENDACTION']._serialized_end=3002
  _globals['_HEADERMAP']._serialized_start=3048
  _globals['_HEADERMAP']._serialized_end=3147
  _globals['_WATCHEDDIRECTORY']._serialized_start=3149
  _globals['_WATCHEDDIRECTORY']._serialized_end=3190
  _globals['_DATASOURCE']._serialized_start=3193
  _globals['_DATASOURCE']._serialized_end=3379
  _globals['_RETRYPOLICY']._serialized_start=3382
  _globals['_RETRYPOLICY']._serialized_end=3568
  _globals['_REMOTEDATASOURCE']._serialized_start=3571
  _globals['_REMOTEDATASOURCE']._serialized_end=3773
  _globals['_ASYNCDATASOURCE']._serialized_start=3776
  _globals['_ASYNCDATASOURCE']._serialized_end=3962
  _globals['_TRANSPORTSOCKET']._serialized_start=3965
  _globals['_TRANSPORTSOCKET']._serialized_end=4122
  _globals['_RUNTIMEFRACTIONALPERCENT']._serialized_start=4125
  _globals['_RUNTIMEFRACTIONALPERCENT']._serialized_end=4290
  _globals['_CONTROLPLANE']._serialized_start=4292
  _globals['_CONTROLPLANE']._serialized_end=4365
# @@protoc_insertion_point(module_scope)
