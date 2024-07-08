from abc import ABC, abstractmethod
from typing import List

class DocumentPrototype(ABC):

    @abstractmethod
    def clone(self):
        pass

class Document(DocumentPrototype):
    def __init__(self, content: str, images: List[str], formatting: str, annotations: List[str]) -> None:
        self.__content = content
        self.__images = list(images)
        self.__formatting = formatting
        self.__annotations = list(annotations)

    def __str__(self) -> str:
        return f"Content: {self.__content}, Images: {self.__images}"
    
    def clone(self):
        return Document(self.__content, self.__images, self.__formatting, self.__annotations)

doc = Document("How a car works?", ["engine.png", "wheels.jpeg"], "utf8", ["some1", "some2"])
print(doc)
copied_doc = doc.clone()
print(copied_doc)