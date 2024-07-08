from abc import ABC, abstractmethod

class Image:
    def __init__(self, name: str) -> None:
        self.name = name
        self.type = "JPG"

class ImageToText(ABC):
    @abstractmethod
    def convert(self, image: Image) -> str:
        """
        Accepts an Image and converts it to text.
        """
        pass

class PNGImageToTextConverter(ImageToText):
    def convert(self, image: Image) -> str:
        if image.type != "PNG":
            return "Incompatible Image Type"
        else:
            return f"Image: {image.name}, successfully converted to text"

class JPEGToPNGAdapter(ImageToText):
    def __init__(self, png_converter: PNGImageToTextConverter) -> None:
        self.png_converter = png_converter

    def convert(self, image: Image) -> str:
        # Adapt JPEG to PNG
        if image.type == "JPG":
            image.type = "PNG"
        return self.png_converter.convert(image)

# Client code
my_img = Image("Avatar")
png_converter = PNGImageToTextConverter()
jpeg_adapter = JPEGToPNGAdapter(png_converter)

converted_img = jpeg_adapter.convert(my_img)
print(converted_img)