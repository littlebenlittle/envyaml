# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: env.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='env.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tenv.proto\"/\n\tValidator\x12\r\n\x05regex\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"V\n\x06\x45nvVar\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x10\n\x08required\x18\x03 \x01(\x08\x12\x1e\n\nvalidators\x18\x04 \x03(\x0b\x32\n.Validator\"\x1f\n\x06\x43onfig\x12\x15\n\x04\x65nvs\x18\x01 \x03(\x0b\x32\x07.EnvVarb\x06proto3')
)




_VALIDATOR = _descriptor.Descriptor(
  name='Validator',
  full_name='Validator',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='regex', full_name='Validator.regex', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Validator.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=60,
)


_ENVVAR = _descriptor.Descriptor(
  name='EnvVar',
  full_name='EnvVar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EnvVar.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='EnvVar.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required', full_name='EnvVar.required', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validators', full_name='EnvVar.validators', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=148,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='envs', full_name='Config.envs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=181,
)

_ENVVAR.fields_by_name['validators'].message_type = _VALIDATOR
_CONFIG.fields_by_name['envs'].message_type = _ENVVAR
DESCRIPTOR.message_types_by_name['Validator'] = _VALIDATOR
DESCRIPTOR.message_types_by_name['EnvVar'] = _ENVVAR
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Validator = _reflection.GeneratedProtocolMessageType('Validator', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATOR,
  '__module__' : 'env_pb2'
  # @@protoc_insertion_point(class_scope:Validator)
  })
_sym_db.RegisterMessage(Validator)

EnvVar = _reflection.GeneratedProtocolMessageType('EnvVar', (_message.Message,), {
  'DESCRIPTOR' : _ENVVAR,
  '__module__' : 'env_pb2'
  # @@protoc_insertion_point(class_scope:EnvVar)
  })
_sym_db.RegisterMessage(EnvVar)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'env_pb2'
  # @@protoc_insertion_point(class_scope:Config)
  })
_sym_db.RegisterMessage(Config)


# @@protoc_insertion_point(module_scope)
