from django.db import models
from .base import Base
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxLengthValidator
from relacionamentos.validators.validar_cpf import valida_cpf
from relacionamentos.managers.reporter_manager import ReporterManager


class Reporter(Base): 

    name = models.CharField(max_length=100,
                            verbose_name=_("Name"), 
                            help_text=_("Digite o nome do reporter"))
    
    email = models.EmailField(max_length=100,
                              verbose_name=_("Email"),
                              help_text=_("Digite o email do reporter"))
    
    cod = models.CharField(max_length=100,
                           verbose_name=_("Código"),
                           help_text=_("Informe um codigo aleatorio"),
                           default="")
    
    cpf = models.CharField(max_length=11, 
                           verbose_name=_("CPF"),
                           help_text='Digite o CPF do reporter',
                           validators=[MaxLengthValidator(11), valida_cpf],
                           unique=True)

    objects = ReporterManager()

    # Adicionar uma Permissao personalizada

    class Meta:
        # Permissoes devem seguir -> permissao_model
        permissions = [
            ("generate_code_reporter", "Pode gerar codigo para reporter"),
        ]

    def __str__(self):
        return f"{self.name} - {self.cpf}"