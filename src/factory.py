from .package import Package

class Factory:
    def __init__(self, name):
        self.name = name

    def sort_package(self, width: float, height: float, length: float, mass: float) -> str:
        """
        This function will sort the given stack where a package with the input dimensions would go.

        @param: width; unit - cm {float}
        @param: height; unit - cm {float}
        @param: length; unit - cm {float}
        @param: mass; unit - kg {float}

        @returns: Stack.stack_type {str}
        """
        new_package = Package(width=width, height=height, length=length, mass=mass)

        # Standard Stack
        if not new_package.bulky and not new_package.heavy:
            return 'standard'

        if new_package.bulky and new_package.heavy:
            return 'rejected'

        if not new_package.bulky or not new_package.heavy:    # NOTE: This explicit conditional is not necessary but here to improve the readability of the code.
            return 'special'
