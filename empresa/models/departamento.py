from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

@dataclass
class Departamento:
    numero: int
    nome: str
    descricao: Optional[str] = None
    criado_em: Optional[datetime] = None
    atualizado_em: Optional[datetime] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> 'Departamento':
        return cls(
            numero=data.get('numero'),
            nome=data.get('nome'),
            descricao=data.get('descricao'),
            criado_em=data.get('criado_em'),
            atualizado_em=data.get('atualizado_em')
        )