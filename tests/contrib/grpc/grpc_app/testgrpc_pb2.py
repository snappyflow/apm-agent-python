# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x12\x04test\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"4\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x10\n\x08received\x18\x02 \x01(\x08\x32\x9a\x02\n\x0bTestService\x12;\n\x11GetServerResponse\x12\r.test.Message\x1a\x15.test.MessageResponse\"\x00\x12@\n\x16GetServerResponseAbort\x12\r.test.Message\x1a\x15.test.MessageResponse\"\x00\x12\x46\n\x1cGetServerResponseUnavailable\x12\r.test.Message\x1a\x15.test.MessageResponse\"\x00\x12\x44\n\x1aGetServerResponseException\x12\r.test.Message\x1a\x15.test.MessageResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=20
  _MESSAGE._serialized_end=46
  _MESSAGERESPONSE._serialized_start=48
  _MESSAGERESPONSE._serialized_end=100
  _TESTSERVICE._serialized_start=103
  _TESTSERVICE._serialized_end=385
# @@protoc_insertion_point(module_scope)
