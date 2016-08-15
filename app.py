#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):    # things that show at index
	return web.Response(body=b'<h1>Awesome</h1>')    # show 'Awesome'

async def init(loop):    # asynchro
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)    # add the method and route
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)  # define ip and port
	logging.info('server started at http://127.0.0.1:9000...')  # print message
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever  # the init should be accessed at all time


