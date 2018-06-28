# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from alephclient.services import common_pb2 as alephclient_dot_services_dot_common__pb2
from alephclient.services import entityextract_pb2 as alephclient_dot_services_dot_entityextract__pb2


class EntityExtractStub(object):
  """The EntityService provides a simple extractor for NLP services that
  accept a stream of text objects (with language metadata) and return
  a set of entities extracted from the source text.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Extract = channel.stream_unary(
        '/EntityExtract/Extract',
        request_serializer=alephclient_dot_services_dot_common__pb2.Text.SerializeToString,
        response_deserializer=alephclient_dot_services_dot_entityextract__pb2.ExtractedEntitySet.FromString,
        )


class EntityExtractServicer(object):
  """The EntityService provides a simple extractor for NLP services that
  accept a stream of text objects (with language metadata) and return
  a set of entities extracted from the source text.
  """

  def Extract(self, request_iterator, context):
    """Extract entities from the given text.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EntityExtractServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Extract': grpc.stream_unary_rpc_method_handler(
          servicer.Extract,
          request_deserializer=alephclient_dot_services_dot_common__pb2.Text.FromString,
          response_serializer=alephclient_dot_services_dot_entityextract__pb2.ExtractedEntitySet.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'EntityExtract', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
