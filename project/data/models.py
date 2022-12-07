from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

'''
Main database related file for PostgreSQL database, tables creation.
Tables are configured with required relationships as mentioned in Task 2
'''

Base = declarative_base()


class DNA(Base):
    '''DNA Table model with one-to-one relationship to RNA table'''
    __tablename__ = 'dna_bases'
    __tablearg__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    dna_base = Column(String(1))
    rna_base = relationship("RNA", uselist=False, back_populates="dna_base")
    rna_base_id = Column(Integer, ForeignKey("rna_bases.id"))

    def __repr__(self) -> str:
        return f"{self.dna_base} {self.rna_base}"


class RNA(Base):
    '''RNA Table model with one-to-one relationship to DNA table'''
    __tablename__ = 'rna_bases'
    __tablearg__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    rna_base = Column(String(1))
    dna_base = relationship("DNA", uselist=False, back_populates="rna_base")

    def __repr__(self) -> str:
        return f"{self.rna_base}"


class Codon(Base):
    '''Codon Table model with many-to-one relationship to Polypeptide table'''
    __tablename__ = 'codons'
    __tablearg__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    codon = Column(String(3))
    polypeptide = relationship("Polypeptide", back_populates="codon")
    polypeptide_id = Column(Integer, ForeignKey("polypeptides.id"))

    def __repr__(self) -> str:
        return f"{self.codon} {self.polypeptide}"


class Polypeptide(Base):
    '''Polypeptide Table model with one-to-many relationship to Codon table'''
    __tablename__ = 'polypeptides'
    __tablearg__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    polypeptide = Column(String(1))
    codon = relationship("Codon", back_populates="polypeptide")

    def __repr__(self) -> str:
        return f"{self.polypeptide}"
