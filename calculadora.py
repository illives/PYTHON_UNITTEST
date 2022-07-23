class Calculadora:

    def soma(x, y):
        """
        >>> Calculadora.soma(10,20)
        30
        """
        assert isinstance(x, (int, float)),'x precisa ser numero.'
        assert isinstance(y, (int, float)),'y precisa ser numero.'
        return x + y


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)