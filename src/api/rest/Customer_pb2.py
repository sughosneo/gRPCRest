# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Customer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Customer.proto',
  package='CustomerInfoSvc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x43ustomer.proto\x12\x0f\x43ustomerInfoSvc\"@\n\x08\x43ustomer\x12\x11\n\tfirstName\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t\x12\x0f\n\x07\x65mailId\x18\x03 \x01(\tb\x06proto3')
)




_CUSTOMER = _descriptor.Descriptor(
  name='Customer',
  full_name='CustomerInfoSvc.Customer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstName', full_name='CustomerInfoSvc.Customer.firstName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='CustomerInfoSvc.Customer.lastName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emailId', full_name='CustomerInfoSvc.Customer.emailId', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=99,
)

DESCRIPTOR.message_types_by_name['Customer'] = _CUSTOMER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Customer = _reflection.GeneratedProtocolMessageType('Customer', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMER,
  __module__ = 'Customer_pb2'
  # @@protoc_insertion_point(class_scope:CustomerInfoSvc.Customer)
  ))
_sym_db.RegisterMessage(Customer)


# @@protoc_insertion_point(module_scope)