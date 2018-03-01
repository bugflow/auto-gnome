import sys
import abc

class Policy(abc.ABC):
    # __metaclass__ =  abc.ABCMeta
    """
    Abstract base-class. Inherited by policies that actually do stuff.

    Don't put this in your `.gnome.yml`, it's ignored.
    """
    def __init__(self, config, callback):
        self.config = config
        self.callback = callback

    # this should probably accept arbitrary kw arguments
    @abc.abstractmethod
    def dispatch_gnome(self):
        """
        The method that does the stuff you want done.

        This method must be over-ridden in actual policies.
        """
        class AbstractBaseGnomePolicyCanNotBeDispatchedError(Exception): pass
        raise AbstractBaseGnomePolicyCanNotBeDispatchedError()


# this is where policies are registered
from plugins.verbose_callback_logging import VerboseCallbackLogging
from plugins.sorting_hat import SortingHat
from plugins.propagate_milestones import PropagateMilestones

MANIFEST = {
    'SortingHat': SortingHat,
    'VerboseCallbackLogging': VerboseCallbackLogging,
    'PropagateMilestones': PropagateMilestones
}