# encoding: utf-8
# module _codecs_cn
# from (built-in)
# by generator 1.147
# no doc
# no imports

# functions

def getcodec(*args, **kwargs): # real signature unknown
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x000001794C4B3460>, 'find_spec': <classmethod object at 0x000001794C4B3490>, 'find_module': <classmethod object at 0x000001794C4B34C0>, 'create_module': <classmethod object at 0x000001794C4B34F0>, 'exec_module': <classmethod object at 0x000001794C4B3520>, 'get_code': <classmethod object at 0x000001794C4B35B0>, 'get_source': <classmethod object at 0x000001794C4B3640>, 'is_package': <classmethod object at 0x000001794C4B36D0>, 'load_module': <classmethod object at 0x000001794C4B3700>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__map_gb18030ext = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001794CEFBC60>'

__map_gb2312 = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001794CEFB930>'

__map_gbcommon = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001794CEFB810>'

__map_gbkext = None # (!) real value is '<capsule object "multibytecodec.__map_*" at 0x000001794CEFB2A0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_codecs_cn', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"
