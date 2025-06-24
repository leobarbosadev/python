import os
from abc import ABC, abstractmethod

# Classe abstrata
class MetodoPagamento(ABC):
    
    @abstractmethod
    def processar_pagament(self,)