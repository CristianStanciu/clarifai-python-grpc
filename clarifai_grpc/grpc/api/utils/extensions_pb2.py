# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/utils/extensions.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/utils/extensions.proto',
  package='clarifai.api.utils',
  syntax='proto3',
  serialized_options=b'\n\033com.clarifai.grpc.api.utilsP\001Zugithub.com/Clarifai/clarifai-go-grpc/proto/clarifai/api/github.com/Clarifai/clarifai-go-grpc/proto/clarifai/api/utils\242\002\004CAIP',
  serialized_pb=b'\n)proto/clarifai/api/utils/extensions.proto\x12\x12\x63larifai.api.utils\x1a google/protobuf/descriptor.proto:9\n\x10\x63l_show_if_empty\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x08:4\n\x0b\x63l_moretags\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\t:9\n\x10\x63l_default_float\x12\x1d.google.protobuf.FieldOptions\x18\xda\x86\x03 \x01(\x02\x42\x9d\x01\n\x1b\x63om.clarifai.grpc.api.utilsP\x01Zugithub.com/Clarifai/clarifai-go-grpc/proto/clarifai/api/github.com/Clarifai/clarifai-go-grpc/proto/clarifai/api/utils\xa2\x02\x04\x43\x41IPb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


CL_SHOW_IF_EMPTY_FIELD_NUMBER = 50000
cl_show_if_empty = _descriptor.FieldDescriptor(
  name='cl_show_if_empty', full_name='clarifai.api.utils.cl_show_if_empty', index=0,
  number=50000, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
CL_MORETAGS_FIELD_NUMBER = 50001
cl_moretags = _descriptor.FieldDescriptor(
  name='cl_moretags', full_name='clarifai.api.utils.cl_moretags', index=1,
  number=50001, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
CL_DEFAULT_FLOAT_FIELD_NUMBER = 50010
cl_default_float = _descriptor.FieldDescriptor(
  name='cl_default_float', full_name='clarifai.api.utils.cl_default_float', index=2,
  number=50010, type=2, cpp_type=6, label=1,
  has_default_value=False, default_value=float(0),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['cl_show_if_empty'] = cl_show_if_empty
DESCRIPTOR.extensions_by_name['cl_moretags'] = cl_moretags
DESCRIPTOR.extensions_by_name['cl_default_float'] = cl_default_float
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(cl_show_if_empty)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(cl_moretags)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(cl_default_float)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
