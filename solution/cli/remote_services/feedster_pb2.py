# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feedster.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='feedster.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=b'\n\x0e\x66\x65\x65\x64ster.proto\"\x92\x01\n\x04\x46\x65\x65\x64\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07website\x18\x03 \x01(\t\x12\x10\n\x08modified\x18\x04 \x01(\x05\x12\x0c\n\x04\x65tag\x18\x05 \x01(\t\x12\x10\n\x08interval\x18\x06 \x01(\x05\x12\x15\n\rlanguage_code\x18\x07 \x01(\t\x12\x14\n\x05posts\x18\x08 \x03(\x0b\x32\x05.Post\"x\n\x04Post\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x11\n\tfeed_hash\x18\x02 \x01(\t\x12\x11\n\tpublished\x18\x03 \x01(\x05\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0f\n\x07summary\x18\x05 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x06 \x01(\t\x12\x0c\n\x04tags\x18\x07 \x03(\t\"S\n\x12\x46\x65\x65\x64ParsingRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08modified\x18\x02 \x01(\x05\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\x10\n\x08interval\x18\x04 \x01(\x05\"j\n\x13\x46\x65\x65\x64ParsingResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x10\n\x08modified\x18\x02 \x01(\x05\x12\x0c\n\x04\x65tag\x18\x03 \x01(\t\x12\x10\n\x08interval\x18\x04 \x01(\x05\x12\x14\n\x05posts\x18\x05 \x03(\x0b\x32\x05.Post2A\n\x06Parser\x12\x37\n\x08\x44ownload\x12\x13.FeedParsingRequest\x1a\x14.FeedParsingResponse\"\x00\x62\x06proto3'
)

_FEED = _descriptor.Descriptor(
    name='Feed',
    full_name='Feed',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='url', full_name='Feed.url', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='title', full_name='Feed.title', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='website', full_name='Feed.website', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='modified', full_name='Feed.modified', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='etag', full_name='Feed.etag', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='interval', full_name='Feed.interval', index=5,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='language_code', full_name='Feed.language_code', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='posts', full_name='Feed.posts', index=7,
            number=8, type=11, cpp_type=10, label=3,
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
    serialized_start=19,
    serialized_end=165,
)

_POST = _descriptor.Descriptor(
    name='Post',
    full_name='Post',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='url', full_name='Post.url', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='feed_hash', full_name='Post.feed_hash', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='published', full_name='Post.published', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='title', full_name='Post.title', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='summary', full_name='Post.summary', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='content', full_name='Post.content', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='tags', full_name='Post.tags', index=6,
            number=7, type=9, cpp_type=9, label=3,
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
    serialized_start=167,
    serialized_end=287,
)

_FEEDPARSINGREQUEST = _descriptor.Descriptor(
    name='FeedParsingRequest',
    full_name='FeedParsingRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='url', full_name='FeedParsingRequest.url', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='modified', full_name='FeedParsingRequest.modified', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='etag', full_name='FeedParsingRequest.etag', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='interval', full_name='FeedParsingRequest.interval', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
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
    serialized_start=289,
    serialized_end=372,
)

_FEEDPARSINGRESPONSE = _descriptor.Descriptor(
    name='FeedParsingResponse',
    full_name='FeedParsingResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='url', full_name='FeedParsingResponse.url', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='modified', full_name='FeedParsingResponse.modified', index=1,
            number=2, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='etag', full_name='FeedParsingResponse.etag', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='interval', full_name='FeedParsingResponse.interval', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='posts', full_name='FeedParsingResponse.posts', index=4,
            number=5, type=11, cpp_type=10, label=3,
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
    serialized_start=374,
    serialized_end=480,
)

_FEED.fields_by_name['posts'].message_type = _POST
_FEEDPARSINGRESPONSE.fields_by_name['posts'].message_type = _POST
DESCRIPTOR.message_types_by_name['Feed'] = _FEED
DESCRIPTOR.message_types_by_name['Post'] = _POST
DESCRIPTOR.message_types_by_name['FeedParsingRequest'] = _FEEDPARSINGREQUEST
DESCRIPTOR.message_types_by_name['FeedParsingResponse'] = _FEEDPARSINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Feed = _reflection.GeneratedProtocolMessageType('Feed', (_message.Message,), {
    'DESCRIPTOR': _FEED,
    '__module__': 'feedster_pb2'
    # @@protoc_insertion_point(class_scope:Feed)
})
_sym_db.RegisterMessage(Feed)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), {
    'DESCRIPTOR': _POST,
    '__module__': 'feedster_pb2'
    # @@protoc_insertion_point(class_scope:Post)
})
_sym_db.RegisterMessage(Post)

FeedParsingRequest = _reflection.GeneratedProtocolMessageType('FeedParsingRequest', (_message.Message,), {
    'DESCRIPTOR': _FEEDPARSINGREQUEST,
    '__module__': 'feedster_pb2'
    # @@protoc_insertion_point(class_scope:FeedParsingRequest)
})
_sym_db.RegisterMessage(FeedParsingRequest)

FeedParsingResponse = _reflection.GeneratedProtocolMessageType('FeedParsingResponse', (_message.Message,), {
    'DESCRIPTOR': _FEEDPARSINGRESPONSE,
    '__module__': 'feedster_pb2'
    # @@protoc_insertion_point(class_scope:FeedParsingResponse)
})
_sym_db.RegisterMessage(FeedParsingResponse)

_PARSER = _descriptor.ServiceDescriptor(
    name='Parser',
    full_name='Parser',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=482,
    serialized_end=547,
    methods=[
        _descriptor.MethodDescriptor(
            name='Download',
            full_name='Parser.Download',
            index=0,
            containing_service=None,
            input_type=_FEEDPARSINGREQUEST,
            output_type=_FEEDPARSINGRESPONSE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_PARSER)

DESCRIPTOR.services_by_name['Parser'] = _PARSER

# @@protoc_insertion_point(module_scope)
