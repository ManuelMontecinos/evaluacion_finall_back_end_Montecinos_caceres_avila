class NoEncontradoError(Exception):
    """El registro pedido no existe."""


class DuplicadoError(Exception):
    """Un dato que debe ser único ya está usado."""


class ReglaNegocioError(Exception):
    """La operación no está permitida por una regla de negocio."""


class PlanNoEncontradoError(NoEncontradoError):
    pass


class PlanDuplicadoError(DuplicadoError):
    pass


class PlanConSociosError(ReglaNegocioError):
    pass


class SocioNoEncontradoError(NoEncontradoError):
    pass


class SocioConInscripcionesError(ReglaNegocioError):
    pass


class InstructorNoEncontradoError(NoEncontradoError):
    pass


class InstructorConClasesError(ReglaNegocioError):
    pass


class ClaseNoEncontradaError(NoEncontradoError):
    pass


class InscripcionNoEncontradaError(NoEncontradoError):
    pass


class RutDuplicadoError(DuplicadoError):
    pass


class EmailDuplicadoError(DuplicadoError):
    pass


class UsuarioDuplicadoError(DuplicadoError):
    pass


class InscripcionDuplicadaError(DuplicadoError):
    pass


class ClaseLlenaError(ReglaNegocioError):
    pass


class ClaseNoProgramadaError(ReglaNegocioError):
    pass


class MembresiaVencidaError(ReglaNegocioError):
    pass


class LimiteSemanalError(ReglaNegocioError):
    pass


class CambioEstadoInvalidoError(ReglaNegocioError):
    pass
