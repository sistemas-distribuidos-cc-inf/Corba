#!/usr/bin/env python
# -*- coding: utf-8 -*-

from omniORB import CORBA, PortableServer
import server, server__POA
import urllib
import sys
import CosNaming

class Crawler_i( server__POA.CrawlerWeb ):

    def get_page( self, url ):
        self.url = url
        try:
            return urllib.urlopen( url ).read()
        except:
            return ""

    def get_next_target( self, page ):
        self.page = page
        start_link = self.page.find( '<a href=' )

        if ( start_link == -1 ):
            return None, 0

        start_quote = self.page.find( '"', start_link )
        end_quote   = self.page.find( '"', start_quote + 1 )
        url = self.page[start_quote+1:end_quote]
        return url, end_quote

    def get_all_links( self, page ):
        self.page = page
        links = []
        while True:
            url,endpos = self.get_next_target( self.page )
            if url:
                links.append( url )
                self.page = self.page[endpos:]
            else:
                break
        return links

    def union( self, p, q ):
        self.p = p
        self.q = q
        for e in self.q:
            if e not in self.p:
                self.p.append( e )

    def crawler_web( self, seed, max_page ):

        self.seed = seed
        self.max_page = max_page
        linksCraled = ''

        tocrawl = [self.seed]
        crawled = []
        index   = []

        while tocrawl:
            page = tocrawl.pop()
            if page not in crawled and len( tocrawl ) < self.max_page:
                content_page = self.get_page( page )
                print ( self.get_page )
                self.union( tocrawl, self.get_all_links( content_page ) )
                crawled.append( page )

        print crawled
        for i in crawled:
            linksCraled = linksCraled + ' , ' + i
        return linksCraled


def main():

    # Initialise the ORB and find the root POA
    orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
    poa = orb.resolve_initial_references("RootPOA")

    # Create an instance of Crawler_i and an Crawler object reference
    ei = Crawler_i()
    eo = ei._this()

    # Obtain a reference to the root naming context
    obj         = orb.resolve_initial_references("NameService")
    rootContext = obj._narrow(CosNaming.NamingContext)

    if rootContext is None:
        print "Failed to narrow the root naming context"
        sys.exit(1)

    # Bind a context named "test.my_context" to the root context
    name = [CosNaming.NameComponent("Crawled", "my_context")]
    try:
        testContext = rootContext.bind_new_context(name)
        print "New Crawled context bound"

    except CosNaming.NamingContext.AlreadyBound, ex:
        print "Crawled context already exists"
        obj = rootContext.resolve(name)
        testContext = obj._narrow(CosNaming.NamingContext)
        if testContext is None:
            print "Crawled.mycontext exists but is not a NamingContext"
            sys.exit(1)

    # Bind the Echo object to the test context
    name = [CosNaming.NameComponent("ExampleEcho", "Object")]
    try:
        testContext.bind(name, eo)
        print "New ExampleEcho object bound"

    except CosNaming.NamingContext.AlreadyBound:
        testContext.rebind(name, eo)
        print "ExampleEcho binding already existed -- rebound"

    # Activate the POA
    poaManager = poa._get_the_POAManager()
    poaManager.activate()

    # Block for ever (or until the ORB is shut down)
    orb.run()


if __name__ == "__main__":
    main()
