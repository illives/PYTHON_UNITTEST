class Calculadora:

    def soma(x, y):
        """
        >>> Calculadora.soma(10,20)
        30
        """
        assert isinstance(x, (int, float)),'x precisa ser numero.'
        assert isinstance(y, (int, float)),'y precisa ser numero.'
        return x + y

    def subtrair(x, y):
        """
        >>> Calculadora.subtrair(30, 10)
        20

        >>> Calculadora.subtrair(-30, 10)
        -40

        >>> Calculadora.subtrair(30, '-10')
        Traceback (most recent call last):
        ...
        AssertionError
        """
        assert isinstance(x, (int, float))
        assert isinstance(y, (int, float))
        return x - y


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)