# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x0buserservice\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"#\n\x0fGetUserResponse\x12\x10\n\x08username\x18\x01 \x01(\t2S\n\x0bUserService\x12\x44\n\x07GetUser\x12\x1b.userservice.GetUserRequest\x1a\x1c.userservice.GetUserResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETUSERREQUEST']._serialized_start=35
  _globals['_GETUSERREQUEST']._serialized_end=68
  _globals['_GETUSERRESPONSE']._serialized_start=70
  _globals['_GETUSERRESPONSE']._serialized_end=105
  _globals['_USERSERVICE']._serialized_start=107
  _globals['_USERSERVICE']._serialized_end=190
# @@protoc_insertion_point(module_scope)
