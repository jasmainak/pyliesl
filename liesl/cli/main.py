# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:48:56 2019

@author: Robert Guggenberger
"""


def get_args():
    import argparse    
    parser = argparse.ArgumentParser(prog='liesl')
    subparsers = parser.add_subparsers(dest="subcommand")
    
    helpstr = """initialize the lsl_api.cfg for all users with system,
                globally for this user with global or 
                locally in this folder with local"""
    parser_cfg = subparsers.add_parser('config', help=helpstr)    
    
    parser_cfg.add_argument('init', action="store_true", help=helpstr)
    parser_cfg.add_argument('--system', action="store_true", help="system-wide")
    parser_cfg.add_argument('--global', dest="_global", action="store_true", help="global")
    parser_cfg.add_argument('--local', action="store_true", help="local")
    

    
    helpstr = """mock a LSL stream"""
    parser_cfg = subparsers.add_parser('mock', help=helpstr)    
    parser_cfg.add_argument('--name', help="name of the stream", default="Liesl-Mock")
    parser_cfg.add_argument('--type', help="type of the stream", default="EEG")

    return parser.parse_known_args()
                   
def main():
    args, unknown = get_args()
    print(args)
    if args.subcommand == "config":
       if args.init:
            from liesl.cli.lsl_api import init_lsl_api_cfg
            if args.system:
                init_lsl_api_cfg("system")
            if args._global:
                init_lsl_api_cfg("global")
            if args.local:
                init_lsl_api_cfg("local")
    if args.subcommand == "mock":
        from liesl.test.mock import Mock
        m = Mock(name=args.name,
                 type=args.type)
        print(m)
        m.run()
    
if __name__ == '__main__':
    get_args()
