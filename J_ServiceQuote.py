class ServiceQuote:

    def __init__(self, pcharge, lcharge, stax):
        self.__parts_charges = pcharge
        self.__labor_charges = lcharge
        self.__sales_tax = stax

    def set_parts_charges(self, pcharge):
        self.__parts_charges = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charges = lcharge

    def set_sales_tax(self, stax):
        self.__sales_tax = stax


    def get_parts_charges(self):
        return self.__parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return self.__sales_tax