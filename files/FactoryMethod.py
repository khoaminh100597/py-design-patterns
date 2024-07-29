from abc import ABC, abstractmethod

# The creator class
class Creator(ABC):
    '''
        The Creator class declares the factory method that is supposed to return an object of Product class.
        The Creator's subclasses usually provide the implementation of this method.
    '''

    @abstractmethod
    def factory_method(): # It supposed to return an object of Product class
        """
            Note that the Creator may also provide some default implementation of the factory method
        """
        pass

    def some_operation(self) -> str:
        """
            Also note that the Creator's primary responsibility is not creating products.
            Usually, it contains some core business logic that relies on Products objects, returned by the factory method.
            Subclasses can indirectly change that business logic by overriding the factory method and returning a differenty type of product from it
        """

        # Call the factory method to create a Product object
        product = self.factory_method()

        # Now use the product
        result = f"Creator: The same creator's code has just worked with {product.some_operation()}"

        return result

class Product(ABC):
    """
        The Product interface declares the operations that all concrete products
        must implement.
    """
    
    @abstractmethod
    def some_operation() -> str:
        pass

class ConcreteCreator1(Creator):
    """
        Note that the signature of method still uses the abstract product type.
        Even though the concrete product is actually returned from the method.
        This way the Creator can stay independent of concrete product class
    """

    def factory_method(self) -> Product: # The Creator still uses the abstract product type
        return ConcreteProduct1() # Even though the concrete product is actually returned from the method
    
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()
    
class ConcreteProduct1(Product):
    def some_operation(self) -> str:
        return f"Result of ConcreteProduct1"
    
class ConcreteProduct2(Product):
    def some_operation(self) -> str:
        return f"Result of ConcreteProduct2"
    
def client_code(creator: Creator) -> str:
    """
        The client code works with an instance of a concrete creator, albeit through
        its base interface. As long as the client keeps working with the creator via
        the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I am not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end='')
    
if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
