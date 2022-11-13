from sqlalchemy import create_engine
from data.config import DATABASE_URI
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

class DNA(Base):
    __tablename__ = 'dna_bases'
    __tablearg__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    dna_base = Column(String)
    rna_base = relationship("RNA", uselist=False, back_populates="dna_base")
    rna_base_id = Column(Integer, ForeignKey("rna_bases.id"))  

    def __repr__(self) -> str:
        return f"{self.dna_base} {self.rna_base}"

class RNA(Base):
    __tablename__ = 'rna_bases'
    __tablearg__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    rna_base = Column(String) 
    dna_base = relationship("DNA", uselist=False, back_populates="rna_base")   

    def __repr__(self) -> str:
        return f"{self.rna_base}"

class Codon(Base):
    __tablename__ = 'codons'
    __tablearg__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    codon = Column(String)
    polypeptide = relationship("Polypeptide", back_populates="codon")
    polypeptide_id = Column(Integer, ForeignKey("polypeptides.id"))

    def __repr__(self) -> str:
        return f"{self.codon} {self.polypeptide}"

class Polypeptide(Base):
    __tablename__ = 'polypeptides'
    __tablearg__ = {"extend_existing": True}
    
    id = Column(Integer, primary_key=True)
    polypeptide = Column(String)
    codon = relationship("Codon", back_populates="polypeptide")

    def __repr__(self) -> str:
        return f"{self.polypeptide}"