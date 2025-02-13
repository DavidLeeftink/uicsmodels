from abc import ABC, abstractmethod
import jax.numpy as jnp

class MeanFunction(ABC):

    @abstractmethod
    def mean(self, params, x):
        pass

    #
#

class Zero(MeanFunction):

    def mean(self, params, x):
        return jnp.zeros_like(x)
    
    #
#

class Constant(MeanFunction):

    def mean(self, params, x):
        return params['c'] * jnp.ones_like(x)

    #
#