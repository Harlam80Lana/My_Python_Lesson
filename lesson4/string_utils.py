class StringUtils:

    # The CAPITAL LETTER

    # Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст.

    def capitilize(self, string: str) -> str:
        return string.capitalize()
    
    
    # A SPACE AT THE BEGINNING OF A WORD

    # Принимает на вход текст и удаляет ПРОБЕЛЫ В НАЧАЛЕ, если они есть.

    def trim(self, string: str) -> str:
        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string
    

    # The DELIMITER

    # Принимает на вход текст с разделителем и возвращает список строк.
    # Параметры: 
    # `string` - строка для обработки/
    # `delimeter` - разделитель строк. По умолчанию запятая (",").

    def to_list(self, string: str, delimeter = ",") -> list[str]:
        if(self.is_empty(string)):
            return []
        return string.split(delimeter)
    

    # THE DESIRED SYMBOL

    # Возвращает `True`, если строка содержит искомый символ и `False` - если нет. 
    # Параметры: 
    # `string` - строка для обработки.
    # `symbol` - искомый символ.

    def contains(self, string: str, symbol: str) -> bool:
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res
    
    
    # DELETING A SYMBOL

    # Удаляет все подстроки из переданной строки.
    # Параметры:
    # `string` - строка для обработки.
    # `symbol` - искомый символ для удаления.

    def delete_symbol(self, string: str, symbol: str) -> str:
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "")
        return string
    

    # THE SYMBOL AT THE BEGINNING OF THE LINE

     # Возвращает `True`, если строка начинается с заданного символа и `False` - если нет.
        # Параметры:
        # `string` - строка для обработки.
        # `symbol` - искомый символ.
            
    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)
    

    # THE SYMBOL AT THE END OF THE LINE

    # Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет.
    # Параметры: 
    # `string` - строка для обработки.
    # `symbol` - искомый символ.

    def end_with(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)
    
    
    # AN EMPTY LINE

    # возвращает `True`, если строка пустая и `False` - если нет.
    
    def is_empty(self, string: str) -> bool:
        string = self.trim(string)
        return string == ""
    
    
    # A STRING WITH THE SPECIFIED JOINER

    # Преобразует список элементов в строку с указанным разделителем.
    # Параметры:
    # `lst` - список элементов.
    # `joiner` - разделитель элементов в строке. По умолчанию запятая (", ").

    def list_to_string(self, lst: list, joiner=",") -> str:
        string = ""
        length = len(lst)    
        if length == 0: 
            return string 
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        return string + str(lst[-1])