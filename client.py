#!/usr/bin/env python

import sys
from omniORB import CORBA
import CosNaming, server

# Initialize the ORB
orb = CORBA.ORB_init( sys.argv, CORBA.ORB_ID )

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow( CosNaming.NamingContext )

if rootContext is None:
	print( "Failed to narrow the root naming context" )
	sys.exit(1)

# Resolve the name "test.my_context/ExampleEcho.Object"
name = [CosNaming.NameComponent("Crawled", "my_context"),
        CosNaming.NameComponent("ExampleEcho", "Object")]
try:
    obj = rootContext.resolve(name)

except CosNaming.NamingContext.NotFound, ex:
    print "Name not found"
    sys.exit(1)

# Narrow the object to an Example::Echo
eo = obj._narrow(server.CrawlerWeb)

if eo is None:
    print "Object reference is not an Example::Echo"
    sys.exit(1)

# Invoke the echoString operation
result  = eo.crawler_web( "https://tunein.com", 5 )

print( result )