import argparse

from pkg_resources import resource_filename

from .base import set_base_parser
from .helper import add_arg_group, _SHOW_ALL_ARGS
from ..helper import random_identity


def mixin_hw_base_parser(parser):
    gp = add_arg_group(parser, title='General')
    gp.add_argument('--workdir', type=str, default=random_identity(),
                    help='The workdir for hello-world demo'
                         'all data, indices, shards and outputs will be saved there')
    gp.add_argument('--download-proxy', type=str,
                    help='The proxy when downloading sample data')


def set_hw_parser(parser=None):
    if not parser:
        parser = set_base_parser()

    mixin_hw_base_parser(parser)
    gp = add_arg_group(parser, title='Scalability')
    gp.add_argument('--shards', type=int,
                    default=2,
                    help='The number of shards when index and query')
    gp.add_argument('--parallel', type=int,
                    default=2,
                    help='The number of parallel when index and query')
    gp = add_arg_group(parser, title='Index')
    gp.add_argument('--uses-index', type=str,
                    default=resource_filename('jina', '/'.join(('resources', 'helloworld.flow.index.yml'))),
                    help='The yaml path of the index flow')
    gp.add_argument('--index-data-url', type=str,
                    default='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz',
                    help='The url of index data (should be in idx3-ubyte.gz format)')
    gp.add_argument('--index-labels-url', type=str,
                    default='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz',
                    help='The url of index labels data (should be in idx3-ubyte.gz format)')
    gp.add_argument('--index-request-size', type=int,
                    default=1024,
                    help='The request size in indexing (the maximum number of documents that will be included in a '
                         'Request before sending it)')

    gp = add_arg_group(parser, title='Search')
    gp.add_argument('--uses-query', type=str,
                    default=resource_filename('jina', '/'.join(('resources', 'helloworld.flow.query.yml'))),
                    help='The yaml path of the query flow')
    gp.add_argument('--query-data-url', type=str,
                    default='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz',
                    help='The url of query data (should be in idx3-ubyte.gz format)')
    gp.add_argument('--query-labels-url', type=str,
                    default='http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz',
                    help='The url of query labels data (should be in idx3-ubyte.gz format)')
    gp.add_argument('--query-request-size', type=int,
                    default=32,
                    help='The request size in searching (the maximum number of documents that will be included in a '
                         'Request before sending it)')
    gp.add_argument('--num-query', type=int, default=128,
                    help='The number of queries to visualize')
    gp.add_argument('--top-k', type=int, default=50,
                    help='Top-k results to retrieve and visualize')
    return parser


def set_hw_chatbot_parser(parser=None):
    if not parser:
        parser = set_base_parser()

    mixin_hw_base_parser(parser)
    parser.add_argument('--uses', type=str,
                        default=resource_filename('jina', '/'.join(('resources', 'helloworld.flow.index.yml'))),
                        help='The yaml path of the index flow')
    parser.add_argument('--index-data-url', type=str,
                        default='https://api.jina.ai/demo/chatbot/dataset.csv',
                        help='The url of index csv data')
    parser.add_argument('--demo-url', type=str,
                        default='https://api.jina.ai/demo/chatbot/',
                        help='The url of chatbot demo page')
    parser.add_argument('--port-expose',
                        type=int,
                        default=8080,
                        help='The port of the host exposed to the public')
    parser.add_argument('--parallel', type=int,
                        default=2,
                        help='The number of parallel when index and query')
    parser.add_argument('--unblock-query-flow', action='store_true', default=False,
                        help='Do not block the query flow' if _SHOW_ALL_ARGS else argparse.SUPPRESS)
    return parser
