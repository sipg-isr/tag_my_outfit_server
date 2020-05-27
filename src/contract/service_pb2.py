# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contract/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contract/service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x16\x63ontract/service.proto\"T\n\x0ePredictRequest\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\x12\x16\n\x0e\x61ll_categories\x18\x02 \x01(\x08\x12\x16\n\x0e\x61ll_attributes\x18\x03 \x01(\x08\"o\n\x0fPredictResponse\x12-\n\x14predicted_categories\x18\x02 \x03(\x0b\x32\x0f.Correspondence\x12-\n\x14predicted_attributes\x18\x03 \x03(\x0b\x32\x0f.Correspondence\"9\n\x15StreamPredictResponse\x12 \n\x0bpredictions\x18\x01 \x03(\x0b\x32\x0b.Prediction\"j\n\nPrediction\x12-\n\x14predicted_categories\x18\x01 \x03(\x0b\x32\x0f.Correspondence\x12-\n\x14predicted_attributes\x18\x02 \x03(\x0b\x32\x0f.Correspondence\".\n\x0e\x43orrespondence\x12\r\n\x05label\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x32\x82\x01\n\x11PredictionService\x12.\n\x07predict\x12\x0f.PredictRequest\x1a\x10.PredictResponse\"\x00\x12=\n\x0estream_predict\x12\x0f.PredictRequest\x1a\x16.StreamPredictResponse\"\x00(\x01\x62\x06proto3')
)




_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_data', full_name='PredictRequest.image_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_categories', full_name='PredictRequest.all_categories', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_attributes', full_name='PredictRequest.all_attributes', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=26,
  serialized_end=110,
)


_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicted_categories', full_name='PredictResponse.predicted_categories', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predicted_attributes', full_name='PredictResponse.predicted_attributes', index=1,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=112,
  serialized_end=223,
)


_STREAMPREDICTRESPONSE = _descriptor.Descriptor(
  name='StreamPredictResponse',
  full_name='StreamPredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predictions', full_name='StreamPredictResponse.predictions', index=0,
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
  serialized_start=225,
  serialized_end=282,
)


_PREDICTION = _descriptor.Descriptor(
  name='Prediction',
  full_name='Prediction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='predicted_categories', full_name='Prediction.predicted_categories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='predicted_attributes', full_name='Prediction.predicted_attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=284,
  serialized_end=390,
)


_CORRESPONDENCE = _descriptor.Descriptor(
  name='Correspondence',
  full_name='Correspondence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='label', full_name='Correspondence.label', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Correspondence.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=392,
  serialized_end=438,
)

_PREDICTRESPONSE.fields_by_name['predicted_categories'].message_type = _CORRESPONDENCE
_PREDICTRESPONSE.fields_by_name['predicted_attributes'].message_type = _CORRESPONDENCE
_STREAMPREDICTRESPONSE.fields_by_name['predictions'].message_type = _PREDICTION
_PREDICTION.fields_by_name['predicted_categories'].message_type = _CORRESPONDENCE
_PREDICTION.fields_by_name['predicted_attributes'].message_type = _CORRESPONDENCE
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
DESCRIPTOR.message_types_by_name['StreamPredictResponse'] = _STREAMPREDICTRESPONSE
DESCRIPTOR.message_types_by_name['Prediction'] = _PREDICTION
DESCRIPTOR.message_types_by_name['Correspondence'] = _CORRESPONDENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTREQUEST,
  __module__ = 'contract.service_pb2'
  # @@protoc_insertion_point(class_scope:PredictRequest)
  ))
_sym_db.RegisterMessage(PredictRequest)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTRESPONSE,
  __module__ = 'contract.service_pb2'
  # @@protoc_insertion_point(class_scope:PredictResponse)
  ))
_sym_db.RegisterMessage(PredictResponse)

StreamPredictResponse = _reflection.GeneratedProtocolMessageType('StreamPredictResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMPREDICTRESPONSE,
  __module__ = 'contract.service_pb2'
  # @@protoc_insertion_point(class_scope:StreamPredictResponse)
  ))
_sym_db.RegisterMessage(StreamPredictResponse)

Prediction = _reflection.GeneratedProtocolMessageType('Prediction', (_message.Message,), dict(
  DESCRIPTOR = _PREDICTION,
  __module__ = 'contract.service_pb2'
  # @@protoc_insertion_point(class_scope:Prediction)
  ))
_sym_db.RegisterMessage(Prediction)

Correspondence = _reflection.GeneratedProtocolMessageType('Correspondence', (_message.Message,), dict(
  DESCRIPTOR = _CORRESPONDENCE,
  __module__ = 'contract.service_pb2'
  # @@protoc_insertion_point(class_scope:Correspondence)
  ))
_sym_db.RegisterMessage(Correspondence)



_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
  name='PredictionService',
  full_name='PredictionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=441,
  serialized_end=571,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict',
    full_name='PredictionService.predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_PREDICTRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='stream_predict',
    full_name='PredictionService.stream_predict',
    index=1,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_STREAMPREDICTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name['PredictionService'] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)
