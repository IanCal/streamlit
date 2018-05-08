# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Image.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Image.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0bImage.proto\"-\n\x05Image\x12\x13\n\x0b\x62\x61se_64_png\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x02 \x01(\t\"0\n\tImageList\x12\x14\n\x04imgs\x18\x01 \x03(\x0b\x32\x06.Image\x12\r\n\x05width\x18\x02 \x01(\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_64_png', full_name='Image.base_64_png', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caption', full_name='Image.caption', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=60,
)


_IMAGELIST = _descriptor.Descriptor(
  name='ImageList',
  full_name='ImageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='imgs', full_name='ImageList.imgs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='ImageList.width', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=110,
)

_IMAGELIST.fields_by_name['imgs'].message_type = _IMAGE
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['ImageList'] = _IMAGELIST

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'Image_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  ))
_sym_db.RegisterMessage(Image)

ImageList = _reflection.GeneratedProtocolMessageType('ImageList', (_message.Message,), dict(
  DESCRIPTOR = _IMAGELIST,
  __module__ = 'Image_pb2'
  # @@protoc_insertion_point(class_scope:ImageList)
  ))
_sym_db.RegisterMessage(ImageList)


# @@protoc_insertion_point(module_scope)