# Python stubs generated by omniidl from Crawler.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "server"
#
__name__ = "server"
_0_server = omniORB.openModule("server", r"Crawler.idl")
_0_server__POA = omniORB.openModule("server__POA", r"Crawler.idl")


# interface CrawlerWeb
_0_server._d_CrawlerWeb = (omniORB.tcInternal.tv_objref, "IDL:server/CrawlerWeb:1.0", "CrawlerWeb")
omniORB.typeMapping["IDL:server/CrawlerWeb:1.0"] = _0_server._d_CrawlerWeb
_0_server.CrawlerWeb = omniORB.newEmptyClass()
class CrawlerWeb :
    _NP_RepositoryId = _0_server._d_CrawlerWeb[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_server.CrawlerWeb = CrawlerWeb
_0_server._tc_CrawlerWeb = omniORB.tcInternal.createTypeCode(_0_server._d_CrawlerWeb)
omniORB.registerType(CrawlerWeb._NP_RepositoryId, _0_server._d_CrawlerWeb, _0_server._tc_CrawlerWeb)

# CrawlerWeb operations and attributes
CrawlerWeb._d_crawler_web = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_short), ((omniORB.tcInternal.tv_string,0), ), None)

# CrawlerWeb object reference
class _objref_CrawlerWeb (CORBA.Object):
    _NP_RepositoryId = CrawlerWeb._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def crawler_web(self, *args):
        return self._obj.invoke("crawler_web", _0_server.CrawlerWeb._d_crawler_web, args)

omniORB.registerObjref(CrawlerWeb._NP_RepositoryId, _objref_CrawlerWeb)
_0_server._objref_CrawlerWeb = _objref_CrawlerWeb
del CrawlerWeb, _objref_CrawlerWeb

# CrawlerWeb skeleton
__name__ = "server__POA"
class CrawlerWeb (PortableServer.Servant):
    _NP_RepositoryId = _0_server.CrawlerWeb._NP_RepositoryId


    _omni_op_d = {"crawler_web": _0_server.CrawlerWeb._d_crawler_web}

CrawlerWeb._omni_skeleton = CrawlerWeb
_0_server__POA.CrawlerWeb = CrawlerWeb
omniORB.registerSkeleton(CrawlerWeb._NP_RepositoryId, CrawlerWeb)
del CrawlerWeb
__name__ = "server"

#
# End of module "server"
#
__name__ = "Crawler_idl"

_exported_modules = ( "server", )

# The end.